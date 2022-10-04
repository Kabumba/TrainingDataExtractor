import numpy as np
import rlgym
from rlgym.utils.state_setters import StateSetter
from rlgym.utils.common_values import BLUE_TEAM, ORANGE_TEAM, BALL_RADIUS
from rlgym.utils.state_setters import StateWrapper
from rlgym.utils.terminal_conditions import common_conditions

import IO_manager


def execute_input_sequence(input_sequence):
    frames = input_sequence["frames"]
    controls = ["throttle", "steer", "pitch", "yaw", "roll", "jump", "boost", "handbrake"]
    frame_count = 1  # len(frames)
    env = rlgym.make(tick_skip=1,
                     team_size=1,
                     terminal_conditions=[common_conditions.GoalScoredCondition()],
                     state_setter=SpawnSetter(input_sequence["player_info"]),
                     spawn_opponents=True
                     )
    obs = env.reset()
    game_states = [obs]
    for i in range(frame_count):
        frame = frames[i]
        inputs1 = frame[0]["inputs"]
        inputs2 = frame[1]["inputs"]
        action1 = np.array([inputs1[c] for c in controls])
        action2 = np.array([inputs2[c] for c in controls])
        actions = [action1, action2]
        new_obs, reward, done, game_info = env.step(actions)
        game_states.append(new_obs)
    env.close()
    return game_states


def load_and_execute(input_sequence_file_name):
    input_sequence = IO_manager.load_finished_input_sequence(input_sequence_file_name)
    return execute_input_sequence(input_sequence)


def load_execute_save(input_sequence_file_name):
    game_states = load_and_execute(input_sequence_file_name)
    IO_manager.save_game_state_sequence(game_states, input_sequence_file_name)


class SpawnSetter(StateSetter):

    def __init__(self, player_info):
        self.player_info = player_info
        self.blue_spawn_locations = [
            [-2048, -2560, 0.25 * np.pi],
            [2048, -2560, 0.75 * np.pi],
            [-256, -3840, 0.50 * np.pi],
            [256, -3840, 0.50 * np.pi],
            [0, -4608, 0.50 * np.pi],
        ]
        self.orange_spawn_locations = [
            [2048, 2560, -0.75 * np.pi],
            [-2048, 2560, -0.25 * np.pi],
            [256, 3840, -0.50 * np.pi],
            [-256, 3840, -0.50 * np.pi],
            [0, 4608, -0.50 * np.pi],
        ]

    def update_player_info(self, player_info):
        self.player_info = player_info

    def get_spawn_info(self):
        spawn_info = []
        for player in self.player_info:
            info = [player["index",
                           player["team"]]]
            location = [player["spawn_info"]["pos_x"],
                        player["spawn_info"]["pos_y"],
                        player["spawn_info"]["rot_y"]]
            if player["team"] == ORANGE_TEAM:
                team_locs = self.orange_spawn_locations
            else:
                team_locs = self.blue_spawn_locations
            i = np.argmin(np.array([loc[0] - location[0] for loc in team_locs]))
            # info.extend(location)
            info.extend(team_locs[i])
            spawn_info.append(info)
        return spawn_info

    def reset(self, state_wrapper: StateWrapper):
        spawn_info = self.get_spawn_info()
        z = 17
        start_boost = 0.33
        for car in state_wrapper.cars:
            info = spawn_info[0]
            if car.team_num == ORANGE_TEAM:
                for i in range(len(spawn_info)):
                    if spawn_info[i][1] == ORANGE_TEAM:
                        info = spawn_info[i]
                        break
            if car.team_num == BLUE_TEAM:
                for i in range(len(spawn_info)):
                    if spawn_info[i][1] == BLUE_TEAM:
                        info = spawn_info[i]
                        break
            x = info[2]
            y = info[3]
            yaw = info[4]
            car.set_pos(x, y, z)
            car.set_rot(0, yaw, 0)
            car.boost = start_boost
        state_wrapper.ball.set_pos(0, 0, BALL_RADIUS)
