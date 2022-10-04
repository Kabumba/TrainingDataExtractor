import bz2
import pickle


class Directories:
    def __init__(self):
        self.BASE_DIR = "C:/Users/Frederik/Masterarbeit/Data"
        self.REPLAY_DIR = self.BASE_DIR + "/Replays"
        self.UNFINISHED_INPUT_DIR = self.BASE_DIR + "/UnalteredInputSequences"
        self.FINISHED_INPUT_DIR = self.BASE_DIR + "/InterpolatedInputSequences"
        self.GAME_STATE_DIR = self.BASE_DIR + "/GameTickPackets"
        self.TEST_REPLAY = "test2.replay"


def save_input_sequence(input_sequence, output_path):
    with bz2.BZ2File(output_path, 'w') as f:
        pickle.dump(input_sequence, f)


def save_game_state_sequence(game_state_sequence, sequence_file_name):
    dirs = Directories()
    save_input_sequence(game_state_sequence, dirs.GAME_STATE_DIR + "/" + sequence_file_name)


def load_input_sequence(input_path):
    with bz2.BZ2File(input_path, 'r') as f:
        input_sequence = pickle.load(f)
    return input_sequence


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
