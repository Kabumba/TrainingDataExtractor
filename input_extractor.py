import custom_carball
from createTrainingData import *
from interpolation_manager import *
import numpy as np

def extract_inputs_per_goal(replay_path):
    '''
    :param replay_path: path to the .replay file to be examined
    :return: list of structured input data for each goal the replay consists of.
            See the documentation of extract_inputs_from_goal.
    '''
    _json = custom_carball.decompile_replay(replay_path)
    game = Game()
    game.initialize(loaded_json=_json)
    x = ControlsCreator()
    x.get_controls(game)
    analysis_manager = AnalysisManager(game)
    analysis_manager.create_data()
    df = analysis_manager.data_frame

    kickoff_frames = game.kickoff_frames
    goal_frames = [goal.frame_number for goal in game.goals]
    last_frame = df.last_valid_index()

    # first included frame
    start_frames = [max(x - 1, 0) for x in kickoff_frames]
    # last included frame
    end_frames = goal_frames
    if len(end_frames) < len(start_frames):
        end_frames.append(last_frame)
    assert (len(end_frames) == len(start_frames))

    # adjust for missing indices in df, that slices ignore
    goal_slices = [slice(start_frames[i] - i - 1, end_frames[i] - i) for i in range(len(end_frames))]
    inputs_per_goal = []
    for goal in goal_slices:
        inputs_per_goal.append(extract_inputs_from_goal(game, df[goal]))
    return inputs_per_goal


def extract_inputs_from_goal(game: Game, goal_data_frame):
    '''

    :param game: the game this goal is a part of
    :param goal_data_frame: should already be sliced to the respective part of the replay
    :return: structured input data for the duration of the game as defined by the timeframe in goal_data_frame
    input_data{}:
        player_info[for each player]:
            index
            team
            spawn_info{}:
                pos_x
                pos_y
                rot_y
        frames[for each frame]:
            time
            players[for each player]:
                index
                inputs{}:
                    throttle
                    steer
                    pitch
                    yaw
                    roll
                    jump
                    boost
                    handbrake
    '''
    controls = ["throttle", "steer", "pitch", "yaw", "roll", "jump", "boost", "handbrake"]
    input_data = {"player_info": [], "frames": []}
    start_index = goal_data_frame.first_valid_index()
    start_time = goal_data_frame.loc[start_index, ("game", "time")]
    for i in range(len(game.players)):
        player_info = {"index": i, "team": 0, "spawn_info": {}}
        player = game.players[i]
        if player.team.is_orange:
            player_info["team"] = 1
        player_info["spawn_info"]["pos_x"] = NaN_fixer(goal_data_frame.loc[start_index, (player.name, "pos_x")])
        player_info["spawn_info"]["pos_y"] = NaN_fixer(goal_data_frame.loc[start_index, (player.name, "pos_y")])
        player_info["spawn_info"]["rot_y"] = NaN_fixer(goal_data_frame.loc[start_index, (player.name, "rot_y")])
        input_data["player_info"].append(player_info)

    for frame_index, row in goal_data_frame.iterrows():
        frame = {"time": NaN_fixer(row["game"]["time"]) - start_time, "players": []}
        for i in range(len(game.players)):
            player_data = {"index": i, "inputs": {}}
            player = game.players[i]
            for c in controls:
                temp = NaN_fixer(player.controls.loc[frame_index, c])
                if temp == None:
                    temp = False
                player_data["inputs"][c] = temp
            frame["players"].append(player_data)
        input_data["frames"].append(frame)
    return input_data
