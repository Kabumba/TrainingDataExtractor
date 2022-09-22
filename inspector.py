import custom_carball

from createTrainingData import *
from interpolation_manager import *
import numpy as np


class Inspector:
    def __init__(self):
        self.baseDir = "C:/Users/Frederik/Masterarbeit/Data"
        self.replayDir = self.baseDir + "/Replays"
        self.dataDir = self.baseDir + "/ExtractedInputsToDo"
        self.jsonDir = self.baseDir + "/DecompiledReplays"
        self.testReplay = "test2.replay"

    def inspectData(self):
        gameData = loadSavedTrainingData(self.dataDir + "/" + self.testReplay + ".pbz2")
        print(f"This variable contains data for {len(gameData)} game frames in addition to controller input data")
        n = 0
        delta = 1
        time = 0
        for i in range(len(gameData)):
            oldtime = time
            time = gameData[i]["GameState"]["time"]
            deltatime = gameData[i]["GameState"]["deltatime"]
            remaining = gameData[i]["GameState"]["seconds_remaining"]
            diff = time - oldtime
            print(str(round(time * 100) / 100) + " \t" + str(round(diff / deltatime)))
        # print(gameData[n]["GameState"])
        # print(gameData[n + delta]["GameState"])
        # print(gameData[n]["PlayerData"][0])
        # print(gameData[n + delta]["PlayerData"][0])

    def analyzeJson(self, filename):
        with open(filename, encoding='utf-8', errors='ignore') as json_file:
            _json = json.load(json_file)
        game = Game()
        game.initialize(loaded_json=_json)

        analysis = AnalysisManager(game)
        analysis.create_analysis()
        return analysis

    def analyzeReplay(self, replayName):
        # analysis_manager = AnalysisManager()
        # analysis_manager = custom_carball.analyze_replay_file(replayName, analysis_per_goal=True)
        _json = custom_carball.decompile_replay(replayName)
        game = Game()
        game.initialize(loaded_json=_json)
        x = ControlsCreator()
        x.get_controls(game)

        analysis_manager = AnalysisManager(game)
        analysis_manager.create_data()
        # analysis_manager.data_frame.info(verbose=True)
        df = analysis_manager.data_frame
        last = 0
        scope = len(game.kickoff_frames)
        for i in range(scope):
            start = game.kickoff_frames[i]
            end = game.goals[i].frame_number
            length = end - start
            pause = start - last
            last = end
            dists = [np.sqrt(np.sum(
                np.power([df.loc[start - 3 + n, ("Teewurstprinz", "vel_x")],
                          df.loc[start - 3 + n, ("Teewurstprinz", "vel_y")]], 2)))
                for n in range(7)]
            print(dists)
            #print(df.loc[start - 2, ("Teewurstprinz", "pos_x")])
            #print(df.loc[start - 1, ("Teewurstprinz", "pos_x")])
            #print(df.loc[start - 0, ("Teewurstprinz", "pos_x")])
            #print(df.loc[start + 1, ("Teewurstprinz", "pos_x")])
            # print(df.loc[end, ("game","goal_number")])
            print("Kickoff-Pause: " + str(pause))
            print("Start: " + str(start) + " End: " + str(end) + " Length: " + str(length))

        '''
        n = 3
        print("kickoff")
        print(len(kickoff_frames))
        print(type(kickoff_frames))
        print(kickoff_frames)
        print(kickoff_frames[n])
        print("firsttouch")
        print(len(first_touch_frames))
        print(type(first_touch_frames))
        print(first_touch_frames)
        print(first_touch_frames[n])
        print(first_touch_frames - kickoff_frames)
        '''
        return analysis_manager

    def extract_inputs_per_goal(self, replay_path):
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

        #first included frame
        start_frames = [max(x-1, 0) for x in kickoff_frames]
        #last included frame
        end_frames = goal_frames
        if len(end_frames) < len(start_frames):
            end_frames.append(last_frame)
        assert (len(end_frames) == len(start_frames))

        #adjust for missing indices in df, that slices ignore
        goal_slices = [slice(start_frames[i]-i-1, end_frames[i]-i) for i in range(len(end_frames))]
        inputs_per_goal = []
        for goal in goal_slices:
            inputs_per_goal.append(self.extract_inputs_from_goal(game, df[goal]))
        return inputs_per_goal

    def extract_inputs_from_goal(self, game: Game, goal_data_frame):
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
        controls = ["throttle", "steer", "pitch", "yaw", "roll", "jump", "handbrake"]
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
                player_data["inputs"]["boost"] = row[player.name]["boost_active"]
                for c in controls:
                    temp = NaN_fixer(player.controls.loc[frame_index, c])
                    if temp == None:
                        temp = False
                    player_data["inputs"][c] = temp
                frame["players"].append(player_data)
            input_data["frames"].append(frame)
        return input_data


inspector = Inspector()
# inspector.inspectData()
# convert_replay_to_game_frames(inspector.replayDir + "/" + inspector.testReplay, inspector.baseDir + "/temp.json")
inspector.extract_inputs_per_goal(inspector.replayDir + "/" + inspector.testReplay)
# games = analysis.get_protobuf_data()
# print(type(games))
