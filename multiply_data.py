import os
import numpy as np

import IO_manager
from IO_manager import Directories


def mirror_states(game_state_sequence):
    """
    Spiegelung an der Längslinie von Tor zu Tor
    :param game_state_sequence:
    :return:
    """
    inverted_states = []
    for frame in game_state_sequence:
        new_frame = np.zeros(frame.shape)
        # ball
        coefs = np.array([
            # ball
            -1, 1, 1,  # pos
            -1, 1, 1,  # vel
            1, -1, -1,  # ang_vel
            # boost-pads
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            # car1
            -1, 1, 1,  # pos
            1, -1, -1,  # forward
            1, -1, -1,  # up
            -1, 1, 1,  # vel
            1, -1, -1,  # ang_vel
            # car2
            -1, 1, 1,  # pos
            1, -1, -1,  # forward
            1, -1, -1,  # up
            -1, 1, 1,  # vel
            1, -1, -1,  # ang_vel
            # inputs
            1, -1, 1, -1, -1, 1, 1, 1,  # car1
            1, -1, 1, -1, -1, 1, 1, 1  # car2
        ])
        new_frame[:85] = frame[:85] * coefs[:85]
        new_frame[85:] = frame[85:] * coefs[85:frame.shape[0]]

        # boost-pads
        new_frame[9] = frame[9]

        new_frame[10] = frame[11]
        new_frame[11] = frame[10]

        new_frame[12] = frame[13]
        new_frame[13] = frame[12]

        new_frame[14] = frame[15]
        new_frame[15] = frame[14]

        new_frame[16] = frame[16]

        new_frame[17] = frame[18]
        new_frame[18] = frame[17]

        new_frame[19] = frame[20]
        new_frame[20] = frame[19]

        new_frame[21:24] = frame[23:20:-1]

        new_frame[24:28] = frame[27:23:-1]

        new_frame[28:31] = frame[30:27:-1]

        new_frame[31] = frame[32]
        new_frame[32] = frame[31]

        new_frame[33] = frame[34]
        new_frame[34] = frame[33]

        new_frame[35] = frame[35]

        new_frame[36] = frame[37]
        new_frame[37] = frame[36]

        new_frame[38] = frame[39]
        new_frame[39] = frame[38]

        new_frame[40] = frame[41]
        new_frame[41] = frame[40]

        new_frame[42] = frame[42]
        inverted_states.append(new_frame)
    return inverted_states


def invert_states(game_state_sequence):
    '''
    Punktspiegelung (vertauschen von teams)
    :param game_state_sequence:
    :return:
    '''
    inverted_states = []
    for frame in game_state_sequence:
        new_frame = np.zeros(frame.shape)
        # ball
        coefs = np.array([
            # ball
            -1, -1, 1,  # pos
            -1, -1, 1,  # vel
            -1, 1, -1,  # ang_vel
            # boost-pads
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            # car1
            -1, -1, 1,  # pos
            -1, 1, -1,  # forward
            -1, 1, -1,  # up
            -1, -1, 1,  # vel
            -1, 1, -1,  # ang_vel
            # car2
            -1, -1, 1,  # pos
            -1, 1, -1,  # forward
            -1, 1, -1,  # up
            -1, -1, 1,  # vel
            -1, 1, -1,  # ang_vel
            # inputs
            1, 1, 1, 1, 1, 1, 1, 1,  # car1
            1, 1, 1, 1, 1, 1, 1, 1  # car2
        ])
        new_frame[:85] = frame[:85] * coefs[:85]
        new_frame[85:] = frame[85:] * coefs[85:frame.shape[0]]
        new_frame[9:35] = frame[34:8:-1]
        inverted_states.append(new_frame)
    return inverted_states


def invert_and_mirror_states(game_state_sequence):
    """
    Spiegelung an der Mittelinie
    :param game_state_sequence:
    :return:
    """
    return invert_states(mirror_states(game_state_sequence))


def multiply_all(files, invert=True, mirror=True, both=True):
    for file in files:
        s = IO_manager.load_game_state_sequence(file)
        if invert:
            IO_manager.save_game_state_sequence(invert_states(s), "(Inverted)" + file)
        if mirror:
            IO_manager.save_game_state_sequence(mirror_states(s), "(Mirrored)" + file)
        if both:
            IO_manager.save_game_state_sequence(invert_and_mirror_states(s), "(Inverted,Mirrored)" + file)


def main():
    dirs = Directories()
    files = os.listdir(dirs.FINISHED_INPUT_DIR)
    multiply_all(files)


if __name__ == '__main__':
    main()
