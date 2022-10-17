from rlgym.utils import StateSetter
import numpy as np
from rlgym.utils.common_values import ORANGE_TEAM, BLUE_TEAM, BALL_RADIUS
from rlgym.utils.state_setters import StateWrapper


class SpawnSetter(StateSetter):

    def __init__(self, player_infos=None):
        self.player_infos = player_infos
        self.current_info_index = 0
        self.current_player_info = None
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

    def inject_new_spawn_info(self, input_sequence):
        self.current_player_info = input_sequence["player_info"]

    def get_spawn_info(self):
        spawn_info = []
        if self.player_infos is None:
            info = self.current_player_info
        else:
            info = self.player_infos[self.current_info_index]
        for player in info:
            info = [player["index"], player["team"]]
            location = [player["spawn_info"]["pos_x"],
                        player["spawn_info"]["pos_y"],
                        player["spawn_info"]["rot_y"]]
            if player["team"] == ORANGE_TEAM:
                team_locs = self.orange_spawn_locations
            else:
                team_locs = self.blue_spawn_locations
            # i = np.argmin(np.array([abs(loc[0] - location[0]) for loc in team_locs]))
            # info.extend(team_locs[i])
            info.extend(location)
            spawn_info.append(info)
        return spawn_info

    def reset(self, state_wrapper: StateWrapper):
        spawn_info = self.get_spawn_info()
        z = 17.01
        start_boost = 0.33
        for i in range(len(state_wrapper.cars)):
            car = state_wrapper.cars[i]
            info = spawn_info[i]
            x = info[2]
            y = info[3]
            yaw = info[4]
            # print(x,y,z)
            car.set_pos(x, y, z)
            car.set_rot(0, yaw, 0)
            car.boost = start_boost
            car.set_ang_vel(0, 0, 0)
            car.set_lin_vel(0, 0, 0)
        state_wrapper.ball.set_pos(0, 0, BALL_RADIUS)
        state_wrapper.ball.set_lin_vel(0, 0, 0)
        state_wrapper.ball.set_ang_vel(0, 0, 0)
        self.current_info_index = self.current_info_index + 1
