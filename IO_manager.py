import bz2
import pickle
import shutil

import torch

import interpolation_manager
#from multiply_data import invert_states, invert_and_mirror_states, mirror_states


class Directories:
    def __init__(self):
        self.BASE_DIR = "C:/Users/Frederik/Masterarbeit/Data"
        self.REPLAY_DIR = self.BASE_DIR + "/Replays"
        self.CORRUPTED_REPLAY_DIR = self.BASE_DIR + "/CorruptedReplays"
        self.UNFINISHED_INPUT_DIR = self.BASE_DIR + "/UnalteredInputSequences"
        self.FINISHED_INPUT_DIR = self.BASE_DIR + "/InterpolatedInputSequences"
        self.OLD_GAME_STATE_DIR = self.BASE_DIR + "/GameStates"
        self.GAME_STATE_DIR = self.BASE_DIR + "/GameTickPackets"
        self.TEST_REPLAY_NAME = "test2"
        self.TEST_REPLAY = self.TEST_REPLAY_NAME + ".replay"
        self.TEST_INTERPOLATOR = interpolation_manager.ConstantSplit(1).to_string()
        self.TEST_INPUT_SEQUENCE = self.TEST_INTERPOLATOR + self.TEST_REPLAY_NAME + "_0.pbz2"


def move_corrupted_replay(replay_file_name):
    dirs = Directories()
    shutil.move(dirs.REPLAY_DIR + "/" + replay_file_name, dirs.CORRUPTED_REPLAY_DIR + "/" + replay_file_name)


def save_input_sequence(input_sequence, output_path):
    with bz2.BZ2File(output_path, 'w') as f:
        pickle.dump(input_sequence, f)


def save_game_state_sequence(game_state_sequence, sequence_file_name):
    dirs = Directories()
    path = dirs.GAME_STATE_DIR + "/"
    torch.save(game_state_sequence, path + sequence_file_name)


def load_game_state_sequence(sequence_file):
    dirs = Directories()
    with bz2.BZ2File(dirs.GAME_STATE_DIR + "/" + sequence_file, 'r') as f:
        game_state_sequence = pickle.load(f)
    return game_state_sequence


def save_unfinished_input_sequence(input_sequence, sequence_name):
    dirs = Directories()
    save_input_sequence(input_sequence, dirs.UNFINISHED_INPUT_DIR + "/" + sequence_name + ".pbz2")


def load_unfinished_input_sequence(sequence_file):
    dirs = Directories()
    with bz2.BZ2File(dirs.UNFINISHED_INPUT_DIR + "/" + sequence_file, 'r') as f:
        input_sequence = pickle.load(f)
    return input_sequence


def load_finished_input_sequence(sequence_file):
    dirs = Directories()
    with bz2.BZ2File(dirs.FINISHED_INPUT_DIR + "/" + sequence_file, 'r') as f:
        input_sequence = pickle.load(f)
    return input_sequence


def save_finished_input_sequence(input_sequence, sequence_name):
    dirs = Directories()
    save_input_sequence(input_sequence, dirs.FINISHED_INPUT_DIR + "/" + sequence_name + ".pbz2")
