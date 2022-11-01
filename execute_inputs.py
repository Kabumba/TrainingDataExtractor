from datetime import datetime
import os
import random

import numpy as np
import rlgym
import torch
from rlgym.utils.obs_builders import DefaultObs
from rlgym.utils.terminal_conditions import common_conditions

import IO_manager
from enhance_data import DataEnhancer
from interpolation_manager import ConstantSplit, Randomizer, DirectedRandomizer, SmoothSteps, GaussSteps, Interpolator
from observation_builder_1v1 import ObservationBuilder1v1
from spawn_setter import SpawnSetter


def execute_input_sequences(input_sequence_file_names: list, save_immediately=False, keep_saved_data_active=False, waiting_frames=0, follow_up_frames=0):
    spawn_setter = SpawnSetter()
    env = rlgym.make(tick_skip=1,
                     team_size=1,
                     game_speed=100,
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
        game_states = execute_input_sequence(input_sequence, env, spawn_setter, waiting_frames, follow_up_frames)
        if save_immediately:
            IO_manager.save_game_state_sequence(game_states, input_sequence_file_names[i])
            if keep_saved_data_active:
                game_states_sequences.append(game_states)
        else:
            game_states_sequences.append(game_states)
    env.close()
    return game_states_sequences


def execute_input_sequence(input_sequence, env, state_setter, waiting_frames=0, follow_up_frames=0):
    controls = ["throttle", "steer", "pitch", "yaw", "roll", "jump", "boost", "handbrake"]
    state_setter.inject_new_spawn_info(input_sequence)
    obs = env.reset()
    frames = input_sequence["frames"]
    frame_count = len(frames)
    # print("Input sequence with " + str(frame_count) + " frames.")
    prev_obs = obs[0][:85]
    game_states = torch.zeros(frame_count, 101)
    de = DataEnhancer()
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
        de.enhance_new_obs(game_states, j, prev_obs)
        prev_obs = new_obs[0][:85]
        if done:
            # print("Goal in frame " + str(j + 1) + "/" + str(frame_count))
            interrupted = True
            break
    de.enhance_new_obs(game_states, frame_count-1, prev_obs)
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


def execute_all_inputs(input_files):
    dirs = IO_manager.Directories()
    start_time = get_time()
    for f in os.listdir(dirs.GAME_STATE_DIR):
        if f in input_files:
            input_files.remove(f)
    random.shuffle(input_files)
    execute_input_sequences(input_files, save_immediately=True, keep_saved_data_active=False)
    end_time = get_time()
    print("============ Done converting! ===========")
    print("Started at " + start_time + " and ended at " + end_time)


def test_pos():
    dirs = IO_manager.Directories()
    # sequences = execute_input_sequences([dirs.TEST_INPUT_SEQUENCE], save_immediately=True, keep_saved_data_active=False)
    # IO_manager.save_game_state_sequence(sequences, "mariachi.pbz2")
    sequences_slow = IO_manager.load_game_state_sequence("16er_test_1speed_uncapped_fps.pbz2")
    sequences_fast = IO_manager.load_game_state_sequence("16er_test_100speed_uncapped_fps.pbz2")
    # s_no_tick = IO_manager.load_game_state_sequence("nomoretickskip.pbz2")
    # game_states = IO_manager.load_game_state_sequence(dirs.TEST_INPUT_SEQUENCE)
    # inputs = IO_manager.load_finished_input_sequence(dirs.TEST_INPUT_SEQUENCE)
    # n = len(game_states) - 1
    start_frame = 0
    end_frame = 7663
    ball_pos = slice(0, 3)
    car1_pos = slice(43, 46)
    car2_pos = slice(64, 67)

    print("gamespeed=1, frame 0")
    print("i \t| ball_pos \t| blue_car_pos \t| orange_car_pos")
    for i in range(16):
        print(str(i) + " \t| " + str(sequences_slow[i][start_frame][ball_pos]) + " \t| " + str(
            sequences_slow[i][start_frame][car1_pos]) + " \t| " + str(sequences_slow[i][start_frame][car2_pos]))
    print("----")
    print("gamespeed=1, frame 7663")
    print("ball_pos | blue_car_pos | orange_car_pos")
    for i in range(16):
        print(str(i) + " \t| " + str(sequences_slow[i][end_frame][ball_pos]) + " \t| " + str(
            sequences_slow[i][end_frame][car1_pos]) + " \t| " + str(sequences_slow[i][end_frame][car2_pos]))
    print("----")
    print("gamespeed=100, frame 0")
    print("ball_pos | blue_car_pos | orange_car_pos")
    for i in range(16):
        print(str(i) + " \t| " + str(sequences_fast[i][start_frame][ball_pos]) + " | " + str(
            sequences_fast[i][start_frame][car1_pos]) + " \t| " + str(sequences_fast[i][start_frame][car2_pos]))
    print("----")
    print("gamespeed=100, frame 7663")
    print("ball_pos | blue_car_pos | orange_car_pos")
    for i in range(16):
        if len(sequences_fast[i]) >= end_frame:
            print(str(i) + " \t| " + str(sequences_fast[i][end_frame][ball_pos]) + " \t| " + str(
                sequences_fast[i][end_frame][car1_pos]) + " \t| " + str(sequences_fast[i][end_frame][car2_pos]))
    print("----")


def test16():
    dirs = IO_manager.Directories()
    sequences = execute_input_sequences([dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         dirs.TEST_INPUT_SEQUENCE,
                                         ], save_immediately=True, keep_saved_data_active=True)
    IO_manager.save_game_state_sequence(sequences, "16er_test_100speed_uncapped_fps.pbz2")


def test_boost():
    dirs = IO_manager.Directories()
    # sequences = execute_input_sequences([dirs.TEST_INPUT_SEQUENCE], save_immediately=True, keep_saved_data_active=False)
    # IO_manager.save_game_state_sequence(sequences, "mariachi.pbz2")
    sequences_slow = IO_manager.load_game_state_sequence("16er_test_1speed_uncapped_fps.pbz2")
    sequences_slow_capped = IO_manager.load_game_state_sequence("16er_test_1speed.pbz2")
    sequences_fast = IO_manager.load_game_state_sequence("16er_test_100speed_uncapped_fps.pbz2")
    sequences_fast_capped = IO_manager.load_game_state_sequence("16er_test_100speed.pbz2")
    # s_no_tick = IO_manager.load_game_state_sequence("nomoretickskip.pbz2")
    # game_states = IO_manager.load_game_state_sequence(dirs.TEST_INPUT_SEQUENCE)
    # inputs = IO_manager.load_finished_input_sequence(dirs.TEST_INPUT_SEQUENCE)
    # n = len(game_states) - 1
    check_frames = range(1, 7663)
    car1_boost_amount = slice(58, 59)
    car1_boost_input = slice(91, 92)
    car2_boost_amount = slice(79, 80)
    car2_boost_input = slice(99, 100)
    boostpad = slice(9, 43)
    sequences = [sequences_slow,
                 sequences_slow_capped,
                 sequences_fast,
                 sequences_fast_capped]
    for s in sequences:
        print(
            "i \t| frame \t| blue_car_boost_amount \t| blue_car_boost_input \t| orange_car_boost_amount \t| orange_car_boost_input \t|")
        for i in range(16):
            initial_pad_state = s[i][0][boostpad]
            for f in check_frames:
                if len(s[i]) > f:
                    boost_collected1 = s[i][f][car1_boost_amount] - s[i][f - 1][car1_boost_amount] > 0
                    boost_collected2 = s[i][f][car2_boost_amount] - s[i][f - 1][car2_boost_amount] > 0
                    pad_collected = np.any(s[i][f][boostpad] - s[i][f - 1][boostpad] == -1)
                    if pad_collected or boost_collected2 or boost_collected1:
                        printe = False
                        string = str(i) + "\t| " + str(f)
                        string = string + "\t| " + str(s[i][f][car1_boost_amount])
                        string = string + "\t| " + str(s[i][f][car2_boost_amount])
                        if boost_collected1 and not pad_collected:
                            printe = True
                            string = string + "\t| car1 collected falsely"
                        if boost_collected2 and not pad_collected:
                            printe = True
                            string = string + "\t| car2 collected falsely"
                        if pad_collected and not (boost_collected1 or boost_collected2):
                            printe = True
                            string = string + "\t| pad collected falsely"
                        if printe:
                            print(string)

def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def main():
    interpolators = \
        [ConstantSplit(1),
         # ConstantSplit(0.75),
         # ConstantSplit(0.5),
         # ConstantSplit(0),
         Randomizer(),
         # DirectedRandomizer(),
         # GaussSteps(),
         SmoothSteps(),
         # Interpolator(),
         ]
    interpolator_strings = [x.to_string() for x in interpolators]
    print([x.to_string() for x in interpolators])
    dirs = IO_manager.Directories()
    input_files = os.listdir(dirs.FINISHED_INPUT_DIR)
    start_time = get_time()
    for f in input_files:
        remove = True
        for i in interpolator_strings:
            if f.startswith(i):
                remove = False
                break
        if remove:
            input_files.remove(f)
    execute_all_inputs(input_files)
    end_time = get_time()
    print("============ Done converting! ===========")
    print("Started at " + start_time + " and ended at " + end_time)


if __name__ == '__main__':
    test_boost()
