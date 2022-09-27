import multiprocessing
import os
from functools import partial

from IO_manager import Directories, save_unfinished_input_sequence, save_input_sequence, save_finished_input_sequence
from input_extractor import extract_inputs_per_goal
from interpolation_manager import Interpolator, ConstantSplit
from datetime import datetime


def convert_single_replay(replay_file, interpolator: Interpolator = None, save_uninterpolated: bool = False):
    if interpolator is None and not save_uninterpolated:
        return
    dirs = Directories()

    replay_name = os.path.splitext(os.path.basename(replay_file))[0]
    base_name = replay_name + "0" + ".pbz2"
    if (save_uninterpolated and base_name in os.listdir(dirs.UNFINISHED_INPUT_DIR)) and (
            (interpolator is None) or (interpolator.to_string() + base_name in os.listdir(dirs.FINISHED_INPUT_DIR))):
        print("Replay skipped, already exists")
        return

    _path = dirs.REPLAY_DIR + "/" + replay_file
    input_sequences = extract_inputs_per_goal(_path)
    print("[" + get_time() + "] Converting next Replay")
    for i in range(len(input_sequences)):
        if save_uninterpolated and \
                replay_name + str(i) + ".pbz2" not in os.listdir(dirs.UNFINISHED_INPUT_DIR):
            save_unfinished_input_sequence(input_sequences[i], replay_name + str(i))

        interpolated_sequence = interpolator.interpolate_all_frames(input_sequences[i])
        if interpolator is not None and \
                interpolator.to_string() + replay_name + str(i) + ".pbz2" not in os.listdir(dirs.FINISHED_INPUT_DIR):
            save_finished_input_sequence(interpolated_sequence, interpolator.to_string() + replay_name + str(i))


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def convert_all_replays(interpolator=None, save_uninterpolated=False):
    dirs = Directories()
    replays = os.listdir(dirs.REPLAY_DIR)
    n_processors = multiprocessing.cpu_count()
    print("Converting " + str(len(replays)) + " Replays")
    try:
        pool = multiprocessing.Pool(n_processors)
        for replay in replays:
            pool.apply(convert_single_replay, args=(replay, interpolator, save_uninterpolated,))
    finally:
        pool.close()
        pool.join()
    print("========= Done converting! =========")


def main():
    intp = ConstantSplit(120, 1)
    save_uninterpolated = True
    convert_all_replays(intp, save_uninterpolated)


if __name__ == '__main__':
    main()
