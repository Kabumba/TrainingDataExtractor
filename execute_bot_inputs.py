import os
import random
from datetime import datetime

import numpy as np
import rlgym
import torch
from rlgym.utils.obs_builders import DefaultObs
from rlgym.utils.state_setters import DefaultState
from rlgym.utils.terminal_conditions import common_conditions

import IO_manager
from Nexto.agent import Agent as Nexto
from Nexto.nexto_obs import NextoObsBuilder
from Necto.agent import Agent as Necto
from Necto.necto_obs import NectoObsBuilder
from enhance_data import DataEnhancer
from observation_builder_1v1 import ObservationBuilder1v1


def generate_kickoffs(num_kickoffs: int):
    max_steps = 7200
    tick_skip = 1
    env = rlgym.make(tick_skip=1,
                     team_size=1,
                     game_speed=100,
                     terminal_conditions=[common_conditions.GoalScoredCondition(),
                                          common_conditions.TimeoutCondition(max_steps)],
                     state_setter=DefaultState(),
                     spawn_opponents=True,
                     obs_builder=DefaultObs(),
                     auto_minimize=False
                     )

    dirs = IO_manager.Directories()
    path = dirs.BASE_DIR + "/BotGenerated/"
    files = os.listdir(path)
    n = len(files)
    for i in range(num_kickoffs):
        bot1, agent1 = random_agent()
        bot2, agent2 = random_agent()
        beta1 = random_beta()
        beta2 = random_beta()
        game_states = generate_kickoff(env, agent1, agent2, beta1, beta2, max_steps, tick_skip)
        torch.save(game_states, path + f'[{bot1},{beta1} vs {bot2},{beta2}]_{n + i}.pt')
    env.close()


def random_agent():
    r = random.Random().uniform(0, 1) < 0.5
    if r:
        return "Nexto", Nexto()
    else:
        return "Necto", Necto()


def random_beta():
    r = random.Random().uniform(0, 1) < 0.5
    if r:
        return 1.0
    else:
        return 0.5


def generate_kickoff(env, agent1, agent2, beta1, beta2, max_steps, tick_skip):
    _, info = env.reset(return_info=True)
    state = info["state"]
    obs_builder = ObservationBuilder1v1()
    agent1_obs_builder = NectoObsBuilder(tick_skip=tick_skip)
    agent2_obs_builder = NextoObsBuilder(tick_skip=tick_skip)

    new_obs = obs_builder.build_obs(state.players[0], state)
    prev_obs = new_obs[:51]
    game_states = torch.zeros(max_steps, 101)
    action1 = np.zeros(8)
    action2 = np.zeros(8)
    de = DataEnhancer()
    steps = max_steps
    for i in range(max_steps):
        if i % tick_skip == 0:
            agent_obs = [agent1_obs_builder.build_obs(state.players[0], state, action1),
                         agent2_obs_builder.build_obs(state.players[1], state, action2)]
            action1, _ = agent1.act(agent_obs[0], beta1)
            action2, _ = agent2.act(agent_obs[1], beta2)
            actions = [action1, action2]
        _, _, done, info = env.step(actions)
        state = info["state"]
        new_obs = obs_builder.build_obs(state.players[0], state)
        prev_obs = np.concatenate([prev_obs, action1, action2])
        de.enhance_new_obs(game_states, i, prev_obs)
        prev_obs = new_obs[:51]
        if done:
            steps = i + 1
            break
    if steps != max_steps:
        new_game_states = torch.zeros(steps, 101)
        new_game_states[:steps] = game_states[:steps]
        return new_game_states
    return game_states


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def main():
    start_time = get_time()
    generate_kickoffs(5000)
    end_time = get_time()
    print("Started at " + start_time + " and ended at " + end_time)


if __name__ == '__main__':
    main()
