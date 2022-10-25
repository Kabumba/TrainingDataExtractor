import math
import multiprocessing
import os
import numpy as np

import IO_manager
import torch
import numpy as np
from IO_manager import Directories
from convert_replays import get_time


class DataEnhancer:
    def __init__(self):
        self.normalize.coef = 1.0 / (120.0 * 10.0)

    # for all the files generated before the change of mind
    def enhance_states(self, game_state_sequence: list):
        n_states = len(game_state_sequence)
        n_features = 101 - 34 + 2 * (6 + 3 + 2 + 6)
        long_time_frames = 240.0
        pos_coef = 1.0 / 2300.0
        ang_coef = 1.0 / math.pi

        long_time = long_time_frames * self.normalize_coef
        enhanced_states = torch.zeros(n_states, n_features, dtype=torch.float32)
        for i in range(n_states):
            enhanced_states[i, :9] = game_state_sequence[i][:9]  # ball
            enhanced_states[i, 9:30] = game_state_sequence[i][43:64]  # car1
            enhanced_states[i, 47:68] = game_state_sequence[i][64:85]  # car2
            enhanced_states[i, 85:] = game_state_sequence[i][85:]  # inputs
            enhanced_states[i, 9:12].mul_(pos_coef)
            enhanced_states[i, 18:21].mul_(pos_coef)
            enhanced_states[i, 21:24].mul_(ang_coef)
            enhanced_states[i, 47:50].mul_(pos_coef)
            enhanced_states[i, 56:59].mul_(pos_coef)
            enhanced_states[i, 59:62].mul_(ang_coef)
            for x in range(2):
                o = x * 38  # offset car 2 state
                oi = x * 8  # offset car 2 input
                # frames since
                if i == 0:
                    # initial state should look like the game has already went on for a time
                    enhanced_states[i, 30 + o] = long_time  # has_jump
                    enhanced_states[i, 31 + o] = long_time  # has_flip
                    enhanced_states[i, 32 + o] = long_time  # is_demoed
                    enhanced_states[i, 33 + o] = long_time  # jump input
                    enhanced_states[i, 34 + o] = long_time  # last jump
                    enhanced_states[i, 35 + o] = long_time  # last flip
                    enhanced_states[i, (36 + o): (45 + o)] = enhanced_states[i, (12 + o): (21 + o)]
                    enhanced_states[i, 45 + o] = enhanced_states[i, 87 + oi]
                    enhanced_states[i, 46 + o] = min(1,
                                                     max(-1, enhanced_states[i, 88 + oi] + enhanced_states[i, 89 + oi]))
                else:
                    enhanced_states[i, 30 + o] = self.bool_frames(enhanced_states, i, 27 + o, 30 + o)  # has_jump
                    enhanced_states[i, 31 + o] = self.bool_frames(enhanced_states, i, 28 + o, 31 + o)  # has_flip
                    enhanced_states[i, 32 + o] = self.bool_frames(enhanced_states, i, 29 + o, 32 + o)  # is_demoed
                    enhanced_states[i, 33 + o] = self.bool_frames(enhanced_states, i, 90 + oi, 33 + o)  # jump input
                    enhanced_states[i, 34 + o] = self.frames_last_jump(enhanced_states, i, 34 + o, 27 + o, 25 + o,
                                                                       90 + oi,
                                                                       33 + o)  # last jump
                    enhanced_states[i, 35 + o] = self.frames_last_jump(enhanced_states, i, 35 + o, 28 + o, 25 + o,
                                                                       90 + oi,
                                                                       33 + o)  # last flip
                    if enhanced_states[i, 35 + o] == 0.0:
                        #  forward, up, lin_vel
                        enhanced_states[i, (36 + o): (45 + o)] = enhanced_states[i, (12 + o): (21 + o)]
                        #  pitch
                        enhanced_states[i, 45 + o] = enhanced_states[i, 87 + oi]
                        # combined yaw and roll
                        enhanced_states[i, 46 + o] = min(1,
                                                         max(-1,
                                                             enhanced_states[i, 88 + oi] + enhanced_states[i, 89 + oi]))
                    else:
                        enhanced_states[i, (36 + o): (45 + o)] = enhanced_states[i - 1, (36 + o): (45 + o)]
                        enhanced_states[i, 45 + o] = enhanced_states[i - 1, 45 + o]
                        enhanced_states[i, 46 + o] = enhanced_states[i - 1, 46 + o]
        return enhanced_states

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

    def enhance_file(self, file_name):
        sequence = IO_manager.load_game_state_sequence(file_name)
        base_name = os.path.splitext(os.path.basename(file_name))[0]
        tensor = self.enhance_states(sequence)
        dirs = Directories()
        torch.save(tensor.clone(), dirs.NEW_GAME_STATE_DIR + "/" + base_name + ".pt")

    def __call__(self, file_name):
        self.enhance_file(file_name)


def enhance_all_files():
    dirs = Directories()
    files = os.listdir(dirs.GAME_STATE_DIR)
    de = DataEnhancer()
    start_time = get_time()
    de.multi_process(files)
    end_time = get_time()
    print("============ Done enhancing! ===========")
    print("Started at " + start_time + " and ended at " + end_time)


def main():
    enhance_all_files()


if __name__ == '__main__':
    main()
