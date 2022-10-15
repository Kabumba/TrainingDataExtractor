import multiprocessing.dummy
import os
from datetime import datetime

import IO_manager
from IO_manager import Directories, save_unfinished_input_sequence, save_finished_input_sequence
from input_extractor import extract_inputs_per_goal
from interpolation_manager import *

'''
This file is for automatically converting replays in one directory to the interpolated input sequences
'''



class ReplayConverter(object):
    def __init__(self, replays, interpolators: [Interpolator] = [], save_unaltered: bool = False):
        self.replays = replays
        self.interpolators = interpolators
        self.save_unaltered = save_unaltered

    def convert_single_replay(self, replay_file, interpolators: [Interpolator] = [], save_unaltered: bool = False):
        replay_name = os.path.splitext(os.path.basename(replay_file))[0]
        replay_flag = "[" + get_time() + "] " + replay_name + " "
        if len(interpolators) == 0 and not save_unaltered:
            #print(replay_flag + "skipped, because nothing should be saved.")
            return
        dirs = Directories()
        base_name = replay_name + "_0" + ".pbz2"
        all_exist = True
        for interpolator in interpolators:
            if interpolator.to_string() + base_name not in os.listdir(dirs.FINISHED_INPUT_DIR):
                all_exist = False
        if save_unaltered and base_name in os.listdir(dirs.UNFINISHED_INPUT_DIR) and all_exist:
            #print(replay_flag + "skipped, already exists.")
            return

        _path = dirs.REPLAY_DIR + "/" + replay_file
        input_sequences = []
        if base_name in os.listdir(dirs.UNFINISHED_INPUT_DIR):
            i = 0
            goal_name = base_name
            while goal_name in os.listdir(dirs.UNFINISHED_INPUT_DIR):
                input_sequences.append(IO_manager.load_unfinished_input_sequence(goal_name))
                i = i + 1
                goal_name = replay_name + "_" + str(i) + ".pbz2"
        else:
            try:
                print("[" + get_time() + "] Converting next Replay: " + replay_name)
                input_sequences = extract_inputs_per_goal(_path)
            except AttributeError as ab:
                print("Replay " + replay_name + " seems to be corrupted")
                print(ab)
                IO_manager.move_corrupted_replay(replay_file)
                return
            except ImportError as ip:
                print("Replay " + replay_name + " is corrupted on the deepest level, better delete it")
                print(ip)
                IO_manager.move_corrupted_replay(replay_file)
                return

        for i in range(len(input_sequences)):
            # print("Goal " + str(i + 1) + ": " + str(len(input_sequences[i]["frames"])) + " frames")
            if save_unaltered and \
                    replay_name + "_" + str(i) + ".pbz2" not in os.listdir(dirs.UNFINISHED_INPUT_DIR):
                # print([x["players"][0]["inputs"]["throttle"] for x in input_sequences[i]["frames"]])
                # print([x["players"][0]["inputs"]["steer"] for x in input_sequences[i]["frames"]])
                save_unfinished_input_sequence(input_sequences[i], replay_name + "_" + str(i))
                # print(replay_flag + "Saved unaltered.")
            # else:
                # if save_unaltered:
                    # print(replay_flag + "Unaltered already saved, skipped saving.")

            for interpolator in interpolators:
                interpolated_sequence = interpolator.interpolate_sequence(input_sequences[i])
                # print([x["players"][0]["inputs"]["steer"] for x in interpolated_sequence["frames"]])
                if interpolator.to_string() + replay_name + "_" + str(i) + ".pbz2" not in os.listdir(
                        dirs.FINISHED_INPUT_DIR):
                    save_finished_input_sequence(interpolated_sequence,
                                                 interpolator.to_string() + replay_name + "_" + str(i))
                    # print(replay_flag + interpolator.to_string() + " Saved interpolated.")
                # else:
                    # print(replay_flag + interpolator.to_string() + " Interpolated already saved, skipped saving.")

    def multi_process(self):
        try:
            pool = multiprocessing.Pool()
            # pool = ProcessingPool()
            '''for i in range(n):
                #pool.apipe(*(convert_single_replay, replays[i], interpolators, save_unaltered))
                pool.apply(convert_single_replay, (replays[i], interpolators, save_unaltered))'''
            pool.map(self, self.replays)
        finally:
            pool.close()
            pool.join()

    def multi_thread(self):
        try:
            pool = multiprocessing.dummy.Pool()
            # pool = ProcessingPool()
            '''for i in range(n):
                #pool.apipe(*(convert_single_replay, replays[i], interpolators, save_unaltered))
                pool.apply(convert_single_replay, (replays[i], interpolators, save_unaltered))'''
            pool.map(self, self.replays)
        finally:
            pool.close()
            pool.join()

    def __call__(self, replay_file):
        return self.convert_single_replay(replay_file, self.interpolators, self.save_unaltered)


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def convert_all_replays(interpolators, save_unaltered=False):
    '''
    Converts all replays in the designated replay directory to input_sequences, interpolated by all interpolators given
    and saves them in the respective directory as well as the unaltered input sequence if desired in the respective directory
    :param interpolators:
    :param save_unaltered:
    :return:
    '''
    dirs = Directories()
    replays = os.listdir(dirs.REPLAY_DIR)
    print("Converting " + str(len(replays)) + " Replays")
    n = len(replays)
    start_time = get_time()
    rc = ReplayConverter(interpolators, save_unaltered)
    try:
        pool = multiprocessing.Pool()
        # pool = ProcessingPool()
        '''for i in range(n):
            #pool.apipe(*(convert_single_replay, replays[i], interpolators, save_unaltered))
            pool.apply(convert_single_replay, (replays[i], interpolators, save_unaltered))'''
        pool.map(rc, replays)
    finally:
        pool.close()
        pool.join()
    end_time = get_time()
    print("============ Done converting! ===========")
    print("Started at " + start_time + " and ended at " + end_time)


def main():
    interpolators = \
        [ConstantSplit(1),
         ConstantSplit(0.75),
         ConstantSplit(0.5),
         ConstantSplit(0),
         Randomizer(),
         DirectedRandomizer(),
         GaussSteps(),
         SmoothSteps(),
         Interpolator()]
    print([x.to_string() for x in interpolators])
    save_unaltered = True
    dirs = Directories()
    replays = os.listdir(dirs.REPLAY_DIR)
    print("Converting " + str(len(replays)) + " Replays")
    start_time = get_time()
    rc = ReplayConverter(replays, interpolators, save_unaltered)
    rc.multi_process()
    end_time = get_time()
    print("============ Done converting! ===========")
    print("Started at " + start_time + " and ended at " + end_time)


if __name__ == '__main__':
    main()
