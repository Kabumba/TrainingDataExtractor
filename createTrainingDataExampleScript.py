from createTrainingData import *
import os
from datetime import datetime

def getTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
def convertAllReplays():
    replays = os.listdir(replayDir)
    replayData = os.listdir(dataDir)
    n_replays = len(replays)
    print("Converting " + str(n_replays) + " Replays")
    for i in range(len(replays)):
        if replays[i]+".pbz2" not in replayData:
            try:
                print("[" + getTime() +"] Converting ["+str(i)+"/"+str(n_replays)+"]")
                _path = "{}/{}".format(replayDir, replays[i])
                output = dataDir+"/"+replays[i]+".pbz2"
                createDataFromReplay(_path, output, baseDir+"/temp.json", save_json=True)
            except Exception as e:
                print("===== FAILURE ======")
                print(e, "\n" + _path)
                print("====================")
        else:
            print("Skipped Replay " + str(i) + ", already exists")
    print("========= Done converting! =========")



baseDir = "C:/Users/Frederik/Masterarbeit/Data"
replayDir = baseDir + "/Replays"
dataDir = baseDir + "/TrainingData"

"how decompile a .replay file into .json format, save it locally(optional) returns extracted game frames data and controls"
# extractedGameStatesAndControls = createTrainingData.convert_replay_to_game_frames("../Data/test2.replay","../Data/testExtract2.json",save_json = True)


"how to extract game frames adSavdata and controls from a previously decompiled .json file"
# x = convert_json_to_game_frames("PreviouslyUnpackedJson.json")


"how to load the data from a previously saved .pbz2 file"
# gameData = createTrainingData.loedTrainingData("exampleSavedTrainingData.pbz2")


"uncomment below code and replace dummy arg with the path to a valid previously saved training data file. Run to see frame data format"
gameData = loadSavedTrainingData(dataDir + "/" + os.listdir(dataDir)[0])
print(f"This variable contains data for {len(gameData)} game frames in addition to controller input data")
n = 500
delta = 2
print(gameData[n]["GameState"])
print(gameData[n+delta]["GameState"])
print(gameData[n]["PlayerData"][0])
print(gameData[n+delta]["PlayerData"][0])

convertAllReplays()

