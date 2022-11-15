import math
import multiprocessing
import os

import IO_manager
import torch
from IO_manager import Directories
from convert_replays import get_time


class DataEnhancer:
    def __init__(self):
        self.normalize_coef = 1.0 / (120.0 * 10.0)
        self.n_features = 101
        self.long_time_frames = 240
        self.long_time = self.long_time_frames * self.normalize_coef
        self.old_pos_coef = 1.0 / 2300.0
        self.old_ang_coef = 1.0 / math.pi

    # assumes already normalized pos and vel, als well as no boostpads in obs
    def enhance_new_obs(self, tensor, i, obs):
        tensor[i, :30] = torch.from_numpy(obs[:30])
        tensor[i, 47:68] = torch.from_numpy(obs[64:85])
        if obs.shape[0] > 85:
            tensor[i, 85:] = torch.from_numpy(obs[85:])
        self.add_time_info(tensor, i)

    # for all the files generated before the change of mind
    def enhance_old_states(self, game_state_sequence: list):
        n_states = len(game_state_sequence)
        enhanced_states = torch.zeros(n_states, self.n_features, dtype=torch.float32)
        for i in range(n_states):
            enhanced_states[i, :9] = torch.from_numpy(game_state_sequence[i][:9])  # ball
            enhanced_states[i, 9:30] = torch.from_numpy(game_state_sequence[i][43:64])  # car1
            enhanced_states[i, 47:68] = torch.from_numpy(game_state_sequence[i][64:85])  # car2
            if game_state_sequence[i].shape[0] > 85:
                enhanced_states[i, 85:] = torch.from_numpy(game_state_sequence[i][85:])  # inputs
            enhanced_states[i, 9:12].mul_(self.old_pos_coef)
            enhanced_states[i, 18:21].mul_(self.old_pos_coef)
            enhanced_states[i, 21:24].mul_(self.old_ang_coef)
            enhanced_states[i, 47:50].mul_(self.old_pos_coef)
            enhanced_states[i, 56:59].mul_(self.old_pos_coef)
            enhanced_states[i, 59:62].mul_(self.old_ang_coef)
            self.add_time_info(enhanced_states, i)
        return enhanced_states

    def remove_normalization(self, tensor):
        tensor[:, 0:3].div_(self.old_pos_coef)
        tensor[:, 3:6].div_(self.old_pos_coef)
        tensor[:, 6:9].div_(self.old_ang_coef)

        tensor[:, 9:12].div_(self.old_pos_coef)
        tensor[:, 18:21].div_(self.old_pos_coef)
        tensor[:, 21:24].div_(self.old_ang_coef)

        tensor[:, 47:50].div_(self.old_pos_coef)
        tensor[:, 56:59].div_(self.old_pos_coef)
        tensor[:, 59:62].div_(self.old_ang_coef)
        return tensor

    def add_time_info(self, tensor, i):
        for x in range(2):
            o = x * 38  # offset car 2 state
            oi = x * 8  # offset car 2 input
            # frames since
            if i == 0:
                # initial state should look like the game has already went on for a time
                tensor[i, 30 + o] = self.long_time  # has_jump
                tensor[i, 31 + o] = self.long_time  # has_flip
                tensor[i, 32 + o] = self.long_time  # is_demoed
                tensor[i, 33 + o] = self.long_time  # jump input
                tensor[i, 34 + o] = self.long_time  # last jump
                tensor[i, 35 + o] = self.long_time  # last flip
                tensor[i, (36 + o): (45 + o)] = tensor[i, (12 + o): (21 + o)]
                tensor[i, 45 + o] = tensor[i, 87 + oi]
                tensor[i, 46 + o] = min(1,
                                        max(-1, tensor[i, 88 + oi] + tensor[i, 89 + oi]))
            else:
                tensor[i, 30 + o] = self.bool_frames(tensor, i, 27 + o, 30 + o)  # has_jump
                tensor[i, 31 + o] = self.bool_frames(tensor, i, 28 + o, 31 + o)  # has_flip
                tensor[i, 32 + o] = self.bool_frames(tensor, i, 29 + o, 32 + o)  # is_demoed
                tensor[i, 33 + o] = self.bool_frames(tensor, i, 90 + oi, 33 + o)  # jump input
                tensor[i, 34 + o] = self.frames_last_jump(tensor, i, 34 + o, 27 + o, 25 + o, 90 + oi,
                                                          33 + o)  # last jump
                tensor[i, 35 + o] = self.frames_last_flip(tensor, i, 35 + o, 28 + o, 25 + o, 90 + oi,
                                                          33 + o)  # last flip
                if tensor[i, 35 + o] == 0.0:
                    #  forward, up, lin_vel
                    tensor[i, (36 + o): (45 + o)] = tensor[i, (12 + o): (21 + o)]
                    #  pitch
                    tensor[i, 45 + o] = tensor[i, 87 + oi]
                    # combined yaw and roll
                    tensor[i, 46 + o] = min(1, max(-1, tensor[i, 88 + oi] + tensor[i, 89 + oi]))
                else:
                    tensor[i, (36 + o): (45 + o)] = tensor[i - 1, (36 + o): (45 + o)]
                    tensor[i, 45 + o] = tensor[i - 1, 45 + o]
                    tensor[i, 46 + o] = tensor[i - 1, 46 + o]

    def bool_frames(self, tensor, frame, b_index, f_index):
        f = 0.0
        if tensor[frame, b_index] == tensor[frame - 1, b_index]:
            f = tensor[frame - 1, f_index] + self.normalize_coef
        return f

    def frames_last_jump(self, tensor, frame, frames_last_jump_i, has_jump_i, on_ground_i, jump_i, f_jump_i):
        if bool(tensor[frame, has_jump_i]) and bool(tensor[frame, on_ground_i]) and bool(tensor[frame, jump_i]) and \
                tensor[
                    frame, f_jump_i] == 0:
            return 0.0
        else:
            return tensor[frame - 1, frames_last_jump_i] + self.normalize_coef

    def frames_last_flip(self, tensor, frame, frames_last_flip_i, has_flip_i, on_ground_i, jump_i, f_jump_i):
        if bool(tensor[frame, has_flip_i]) and not bool(tensor[frame, on_ground_i]) and bool(tensor[frame, jump_i]) and \
                tensor[frame, f_jump_i] == 0.0:
            return 0.0
        else:
            return tensor[frame - 1, frames_last_flip_i] + self.normalize_coef

    def multi_process(self, files):
        try:
            pool = multiprocessing.Pool()
            pool.map(self, files)
        finally:
            pool.close()
            pool.join()

    def enhance_old_file(self, file_name):
        base_name = os.path.splitext(os.path.basename(file_name))[0]
        dirs = Directories()
        if base_name + ".pt" in os.listdir(dirs.NEW_GAME_STATE_DIR):
            return
        sequence = IO_manager.load_game_state_sequence(file_name)
        print("Enhancing " + file_name)
        try:
            tensor = self.enhance_states(sequence)
        except Exception as e:
            print(e)
            return
        dirs = Directories()
        torch.save(tensor.clone(), dirs.NEW_GAME_STATE_DIR + "/" + base_name + ".pt")

    def enhance_new_old_file(self, file_name):
        base_name = os.path.splitext(os.path.basename(file_name))[0]
        dirs = Directories()
        if base_name + ".pt" in os.listdir(dirs.GAME_STATE_DIR):
            return
        tensor = torch.load(os.path.join(dirs.OLD_GAME_STATE_DIR, file_name))
        print("Enhancing " + file_name)
        try:
            new_tensor = self.remove_normalization(tensor)
            for i in range(new_tensor.shape[0]):
                self.add_time_info(new_tensor, i)
        except Exception as e:
            print(e)
            return
        dirs = Directories()
        torch.save(new_tensor.clone(), dirs.GAME_STATE_DIR + "/" + base_name + ".pt")

    def __call__(self, file_name):
        self.enhance_new_old_file(file_name)


def enhance_all_old_files():
    dirs = Directories()
    files = os.listdir(dirs.OLD_GAME_STATE_DIR)
    de = DataEnhancer()
    start_time = get_time()
    de.multi_process(files)
    end_time = get_time()
    print("============ Done enhancing! ===========")
    print("Started at " + start_time + " and ended at " + end_time)


def inspect_values():
    dirs = IO_manager.Directories()
    files = os.listdir(dirs.GAME_STATE_DIR)
    print(len(files))
    tensor = torch.load(os.path.join(dirs.GAME_STATE_DIR, files[0]))
    for i in range(tensor.shape[0]):
        # print(f'has_jump: {tensor[i, 27]} has_flip: {tensor[i, 28]} frames_last_jump: {tensor[i, 34]} frames_last_flip: {tensor[i, 35]} lin_vel_at_last_flip: {tensor[i, 42:45]}')
        # print(f'is_demo: {tensor[i, 29]} frames_is_demo: {tensor[i, 32]}')
        # print(f'jump: {tensor[i, 90]} frames_jump: {tensor[i, 33]}')
        # print(f'has_jump: {tensor[i, 27]} frames_has_jump: {tensor[i, 30]}')
        # print(f'on_ground: {tensor[i, 25]} has_jump: {tensor[i, 27]} has_flip: {tensor[i, 28]} jump {tensor[i, 90]}')
        print(f'pos: {tensor[i, 9:12]} vel: {tensor[i, 18:21]} ang_vel: {tensor[i, 21:24]}')
    print("done")


def main():
    inspect_values()


if __name__ == '__main__':
    main()
