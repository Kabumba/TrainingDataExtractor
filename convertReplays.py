import multiprocessing

from createTrainingData import *
import os
from datetime import datetime
from multiprocessing import Pool

def getTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
def convertAllReplays():
    baseDir = "C:/Users/Frederik/Masterarbeit/Data"
    replayDir = baseDir + "/Replays"
    replays = os.listdir(replayDir)
    n_processors = multiprocessing.cpu_count()
    print("Converting " + str(len(replays)) + " Replays")
    try:
        pool = Pool(n_processors)
        pool.map(convertSingleReplay, replays)
    finally:
        pool.close()
        pool.join()
    print("========= Done converting! =========")

def convertSingleReplay(replay_name):
    baseDir = "C:/Users/Frederik/Masterarbeit/Data"
    replayDir = baseDir + "/Replays"
    dataDir = baseDir + "/ExtractedInputsToDo"
    if replay_name + ".pbz2" not in os.listdir(dataDir):
        try:
            print("[" + getTime() + "] Converting next Replay")
            _path = "{}/{}".format(replayDir, replay_name)
            output = dataDir + "/" + replay_name + ".pbz2"
            createDataFromReplay(_path, output, baseDir + "/temp"+replay_name+".json", save_json=False)
        except Exception as e:
            print("===== FAILURE ======")
            print(e, "\n" + _path)
            print("====================")
    else:
        print("Skipped Replay, already exists")




"how decompile a .replay file into .json format, save it locally(optional) returns extracted game frames data and controls"
# extractedGameStatesAndControls = createTrainingData.convert_replay_to_game_frames("../Data/test2.replay","../Data/testExtract2.json",save_json = True)


"how to extract game frames adSavdata and controls from a previously decompiled .json file"
# x = convert_json_to_game_frames("PreviouslyUnpackedJson.json")


"how to load the data from a previously saved .pbz2 file"
# gameData = createTrainingData.loadTrainingData("exampleSavedTrainingData.pbz2")


def main():
    convertAllReplays()


if __name__ == '__main__':
    main()
