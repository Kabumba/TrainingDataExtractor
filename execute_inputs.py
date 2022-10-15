import os

import numpy as np
import rlgym
from rlgym.utils.obs_builders import DefaultObs
from rlgym.utils.terminal_conditions import common_conditions

import IO_manager
from observation_builder_1v1 import ObservationBuilder1v1
from spawn_setter import SpawnSetter


def execute_input_sequences(input_sequence_file_names: list, save_immediately=False, keep_saved_data_active=False):
    spawn_setter = SpawnSetter()
    env = rlgym.make(tick_skip=1,
                     team_size=1,
                     game_speed=1,
                     terminal_conditions=[common_conditions.GoalScoredCondition()],
                     state_setter=spawn_setter,
                     spawn_opponents=True,
                     obs_builder=ObservationBuilder1v1(),
                     auto_minimize=False
                     )
    game_states_sequences = []
    for i in range(len(input_sequence_file_names)):
        input_sequence = IO_manager.load_finished_input_sequence(input_sequence_file_names[i])
        print("Executing sequence " + str(i + 1) + "/" + str(len(input_sequence_file_names)))
        game_states = execute_input_sequence(input_sequence, env, spawn_setter)
        if save_immediately:
            IO_manager.save_game_state_sequence(game_states, input_sequence_file_names[i])
            if keep_saved_data_active:
                game_states_sequences.append(game_states)
        else:
            game_states_sequences.append(game_states)
    env.close()
    return game_states_sequences


def execute_input_sequence(input_sequence, env, state_setter):
    controls = ["throttle", "steer", "pitch", "yaw", "roll", "jump", "boost", "handbrake"]
    state_setter.inject_new_spawn_info(input_sequence)
    obs = env.reset()
    frames = input_sequence["frames"]
    frame_count = len(frames)
    follow_up_frames = 0
    waiting_frames = 0
    print("Input sequence with " + str(frame_count) + " frames.")
    prev_obs = obs[0][:85]
    game_states = []
    interrupted = False
    for i in range(waiting_frames):
        new_obs, _, done, _ = env.step(np.zeros((16,)))
    for j in range(frame_count):
        frame = frames[j]
        inputs1 = frame["players"][0]["inputs"]
        inputs2 = frame["players"][1]["inputs"]
        action1 = np.array([inputs1[c] for c in controls])
        action2 = np.array([inputs2[c] for c in controls])
        actions = [action1, action2]
        new_obs, _, done, _ = env.step(actions)

        prev_obs = np.concatenate([prev_obs, new_obs[0][85:93], new_obs[1][85:93]])
        game_states.append(prev_obs)
        prev_obs = new_obs[0][:85]
        if done:
            print("Goal in frame " + str(j + 1) + "/" + str(frame_count))
            interrupted = True
            break
    game_states.append(prev_obs)
    if not interrupted and follow_up_frames > 0:
        print("No goal, continue for " + str(follow_up_frames) + " frames")
        for i in range(follow_up_frames):
            _, _, done, _ = env.step(np.zeros((16,)))
            if done:
                print("Goal in frame " + str(frame_count + 1 + i) + "/" + str(frame_count))
                interrupted = True
                break
        if not interrupted:
            print("Still no goal.")
    return game_states


def load_and_execute(input_sequence_file_names):
    input_sequences = [IO_manager.load_finished_input_sequence(name) for name in input_sequence_file_names]
    return execute_input_sequences(input_sequences)


def load_execute_save(input_sequence_file_names):
    game_states_sequences = load_and_execute(input_sequence_file_names)
    for i in len(input_sequence_file_names):
        IO_manager.save_game_state_sequence(game_states_sequences[i], input_sequence_file_names[i])


def test():
    dirs = IO_manager.Directories()
    # input_files = os.listdir(dirs.FINISHED_INPUT_DIR)
    sequences = execute_input_sequences([dirs.TEST_INPUT_SEQUENCE], save_immediately=False, keep_saved_data_active=True)
    IO_manager.save_game_state_sequence(sequences, "mariachi.pbz2")
    # sequences_slow = IO_manager.load_game_state_sequence("16er_test_1speed.pbz2")
    # sequences_fast = IO_manager.load_game_state_sequence("16er_test_100speed.pbz2")
    # s_no_tick = IO_manager.load_game_state_sequence("nomoretickskip.pbz2")
    # game_states = IO_manager.load_game_state_sequence(dirs.TEST_INPUT_SEQUENCE)
    # inputs = IO_manager.load_finished_input_sequence(dirs.TEST_INPUT_SEQUENCE)
    # n = len(game_states) - 1
    frame = 7663
    cut = slice(0, 3)
    print(sequences[0][frame][cut])
    '''
    
    for i in range(16):
        print(sequences_slow[i][frame][cut])
    print("-----")
    print(s_no_tick[0][frame][cut])
    print("----")
    for i in range(16):
        if len(sequences_fast[i]) > frame:
            print(sequences_fast[i][frame][cut])'''


test()
print("done")
