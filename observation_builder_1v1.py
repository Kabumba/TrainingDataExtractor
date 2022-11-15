import math
import numpy as np
from typing import Any, List
from rlgym.utils import common_values
from rlgym.utils.gamestates import PlayerData, GameState

from rlgym.utils.obs_builders import ObsBuilder


class ObservationBuilder1v1(ObsBuilder):
    def __init__(self, pos_coef=1, ang_coef=1, lin_vel_coef=1, ang_vel_coef=1):
        """
        :param pos_coef: Position normalization coefficient
        :param ang_coef: Rotation angle normalization coefficient
        :param lin_vel_coef: Linear velocity normalization coefficient
        :param ang_vel_coef: Angular velocity normalization coefficient
        """
        super().__init__()
        self.POS_COEF = pos_coef
        self.ANG_COEF = ang_coef
        self.LIN_VEL_COEF = lin_vel_coef
        self.ANG_VEL_COEF = ang_vel_coef

    def reset(self, initial_state: GameState):
        pass

    def build_obs(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> Any:
        ball = state.ball
        # pads = state.boost_pads
        obs = [ball.position * self.POS_COEF,
               ball.linear_velocity * self.LIN_VEL_COEF,
               ball.angular_velocity * self.ANG_VEL_COEF]

        cars = []
        self._add_player_to_obs(cars, player, False)
        for other in state.players:
            if other.car_id == player.car_id:
                continue
            self._add_player_to_obs(cars, other, False)
        obs.extend(cars)
        obs.append(previous_action)
        return np.concatenate(obs)

    def _add_player_to_obs(self, obs: List, player: PlayerData, inverted: bool):
        if inverted:
            player_car = player.inverted_car_data
        else:
            player_car = player.car_data

        obs.extend([
            player_car.position * self.POS_COEF,
            player_car.forward(),
            player_car.up(),
            player_car.linear_velocity * self.LIN_VEL_COEF,
            player_car.angular_velocity * self.ANG_VEL_COEF,
            [player.boost_amount,
             int(player.on_ground),
             int(player.ball_touched),
             int(player.has_jump),
             int(player.has_flip),
             int(player.is_demoed)]])

        return player_car
