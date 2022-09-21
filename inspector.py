import custom_carball

from createTrainingData import *
from custom_carball.extras.per_goal_analysis import PerGoalAnalysis
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

    def extract_inputs_per_goal(self, replayName):
        _json = custom_carball.decompile_replay(replayName)
        game = Game()
        game.initialize(loaded_json=_json)
        x = ControlsCreator()
        x.get_controls(game)
        analysis_manager = AnalysisManager(game)
        analysis_manager.create_data()

        kickoff_frames = game.kickoff_frames
        goal_frames = [goal.frame_number for goal in game.goals]
        last_frame = len(analysis_manager.data_frame)-1

        #first included frame
        start_frames = [max(x-1, 0) for x in kickoff_frames]
        #last included frame
        end_frames = goal_frames
        if len(end_frames) < len(start_frames):
            end_frames.append(last_frame)
        assert (len(end_frames) == len(start_frames))
        goal_slices = [slice(start_frames[i],end_frames[i]+1) for i in range(len(end_frames))]

        inputs_per_goal = []
        for goal in goal_slices:
            inputs_per_goal.append(self.extract_inputs_from_slice(game, analysis_manager.data_frame, goal))
        return inputs_per_goal

    def extract_inputs_from_slice(self, game: Game, game_data_frame, goal_slice: slice):
        spawn_info = {}
        frames = []
        goal_data_frame = game_data_frame[goal_slice]
        print()
        for col, row in goal_data_frame.iterrows():
            pass
        return spawn_info, frames


inspector = Inspector()
# inspector.inspectData()
# convert_replay_to_game_frames(inspector.replayDir + "/" + inspector.testReplay, inspector.baseDir + "/temp.json")
inspector.extract_inputs_per_goal(inspector.replayDir + "/" + inspector.testReplay)
# games = analysis.get_protobuf_data()
# print(type(games))
