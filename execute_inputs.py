import os

import numpy as np
import rlgym
from rlgym.utils.obs_builders import DefaultObs
from rlgym.utils.terminal_conditions import common_conditions

import IO_manager
from spawn_setter import SpawnSetter


def execute_input_sequences(input_sequence_file_names: list, save_immediately=False, keep_saved_data_active=False):
    spawn_setter = SpawnSetter()
    env = rlgym.make(tick_skip=1,
                     team_size=1,
                     terminal_conditions=[common_conditions.GoalScoredCondition()],
                     state_setter=spawn_setter,
                     spawn_opponents=True,
                     obs_builder=DefaultObs(pos_coef=1, ang_coef=1, ang_vel_coef=1, lin_vel_coef=1)
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
    print("Input sequence with " + str(frame_count) + " frames.")
    game_states = [obs]
    for j in range(frame_count):
        frame = frames[j]
        inputs1 = frame["players"][0]["inputs"]
        inputs2 = frame["players"][1]["inputs"]
        action1 = np.array([inputs1[c] for c in controls])
        action2 = np.array([inputs2[c] for c in controls])
        actions = [action1, action2]
        new_obs, reward, done, game_info = env.step(actions)
        game_states.append(new_obs)
        if done:
            print("Goal in frame " + str(j + 1) + "/" + str(frame_count))
            break
    return game_states


def load_and_execute(input_sequence_file_names):
    input_sequences = [IO_manager.load_finished_input_sequence(name) for name in input_sequence_file_names]
    return execute_input_sequences(input_sequences)


def load_execute_save(input_sequence_file_names):
    game_states_sequences = load_and_execute(input_sequence_file_names)
    for i in len(input_sequence_file_names):
        IO_manager.save_game_state_sequence(game_states_sequences[i], input_sequence_file_names[i])


dirs = IO_manager.Directories()
input_files = os.listdir(dirs.FINISHED_INPUT_DIR)
#sequences = execute_input_sequences([dirs.TEST_INPUT_SEQUENCE], save_immediately=True)
game_states = IO_manager.load_game_state_sequence(dirs.TEST_INPUT_SEQUENCE)
inputs = IO_manager.load_finished_input_sequence(dirs.TEST_INPUT_SEQUENCE)
n = len(game_states)-1
player = 1
for i in range(n):
    k = 0
    for j in inputs["frames"][i]["players"][player]["inputs"]:
        if inputs["frames"][i]["players"][player]["inputs"][j] != game_states[i+1][player][9:17][k]:
            print(str(inputs["frames"][i]["players"][player]["inputs"][j]) + " vs " + str(game_states[i+1][player][9:17][k]))
        k = k+1
print("done")

