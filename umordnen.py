import os
import random
import shutil

from IO_manager import Directories

dirs = Directories()
gs = os.listdir(dirs.BASE_DIR + "/GameStates")
for f in gs:
    if random.Random().uniform(0.0, 1.0) < 0.2:
        shutil.copy(dirs.BASE_DIR + "/GameStates/" + f, dirs.BASE_DIR + "/Test/" + f)
    else:
        shutil.copy(dirs.BASE_DIR + "/GameStates/" + f, dirs.BASE_DIR + "/Train/" + f)
