import numpy as np


def invert(game_state_sequence):
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
        ])
        new_frame[:85] = frame[:85] * coefs[:85]
        new_frame[9:35] = frame[9:35:-1]
        inverted_states.append(new_frame)
    return inverted_states


def mirror(game_state_sequence):
    '''
    Spiegelung an der Längslinie von Tor zu Tor
    :param game_state_sequence:
    :return:
    '''
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
            -1, 1, 1,   # pos
            1, -1, -1,  # forward
            1, -1, -1,  # up
            -1, 1, 1,   # vel
            1, -1, -1,  # ang_vel
            # car2
            -1, 1, 1,  # pos
            1, -1, -1,  # forward
            1, -1, -1,  # up
            -1, 1, 1,  # vel
            1, -1, -1,  # ang_vel
        ])
        new_frame[:85] = frame[:85] * coefs[:85]
        new_frame[9:35] = frame[9:35:-1]
        inverted_states.append(new_frame)
    return inverted_states


def invert_and_mirror(game_state_sequence):
    '''
    Spiegelung an der Mittelinie
    :param game_state_sequence:
    :return:
    '''
    return invert(mirror(game_state_sequence))
