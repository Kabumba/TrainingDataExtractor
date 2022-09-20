import custom_carball

from createTrainingData import *
from custom_carball.extras.per_goal_analysis import PerGoalAnalysis
from interpolation_manager import *


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
            print(str(round(time*100)/100) + " \t" + str(round(diff/deltatime)))
        #print(gameData[n]["GameState"])
        #print(gameData[n + delta]["GameState"])
        #print(gameData[n]["PlayerData"][0])
        #print(gameData[n + delta]["PlayerData"][0])

    def analyzeJson(self, filename):
        with open(filename, encoding='utf-8', errors='ignore') as json_file:
            _json = json.load(json_file)
        game = Game()
        game.initialize(loaded_json=_json)

        analysis = AnalysisManager(game)
        analysis.create_analysis()
        return analysis

    def analyzeReplay(self, replayName):
        #analysis_manager = AnalysisManager()
        #analysis_manager = custom_carball.analyze_replay_file(replayName, analysis_per_goal=True)
        _json = custom_carball.decompile_replay(replayName)
        game = Game()
        game.initialize(loaded_json=_json)

        analysis_manager = PerGoalAnalysis(game)
        analysis_manager.create_analysis()
        analysis_manager.data_frame.info(verbose=True)
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



inspector = Inspector()
#inspector.inspectData()
#convert_replay_to_game_frames(inspector.replayDir + "/" + inspector.testReplay, inspector.baseDir + "/temp.json")
analysis = inspector.analyzeReplay(inspector.replayDir + "/" + inspector.testReplay)
#games = analysis.get_protobuf_data()
#print(type(games))

