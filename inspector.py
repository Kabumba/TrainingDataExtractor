from createTrainingData import *
from interpolationManager import *


class Inspector:
    def __init__(self):
        self.baseDir = "C:/Users/Frederik/Masterarbeit/Data"
        self.replayDir = self.baseDir + "/Replays"
        self.dataDir = self.baseDir + "/ExtractedInputsToDo"
        self.testReplay = "test.replay"

    def inspectData(self):
        gameData = loadSavedTrainingData(self.dataDir + "/" + os.listdir(self.dataDir)[0])
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


inspector = Inspector()
inspector.inspectData()
