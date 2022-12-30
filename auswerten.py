import os
from IO_manager import Directories
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dirs = Directories()
exp_dir = "../Ergebnisse/"

'''
exps = ["16k 0.0001",
        "16k 0.0003",
        "16k 0.001",
        "16k 0.003",
        "16k 0.01"]

exps = ["16k 0.001",
        "2rep",
        "3rep"]
'''
exps = ["2k",
        "4k",
        "8k",
        "16k 0.001",
        "32k",
        "64k"]

data = []

for exp in exps:
    path = exp_dir + exp + "/TrainingLoss"
    files = os.listdir(path)
    losses = []
    for f in files:
        df = pd.read_csv(path + "/" + f)
        starttime = df["Wall time"][0]
        reftime = starttime + 7*60*60
        refstep = 1200000000
        for i in range(df.shape[0]):
            # if df["Wall time"][i]<reftime:
            if df["Step"][i] < refstep:
                continue
            else:
                #losses.append(df["Step"][i]/161959504.0)
                #losses.append(df["Value"][i]/(df["Step"][i]/161959504.0))
                losses.append(df["Value"][i])
                break
    data.append(losses)
fig = plt.figure(figsize=(10, 7))
# Creating plot
# = plt.boxplot(data)

# show plot
#fig.suptitle('Traingsloss nach 7 Stunden', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
ax.boxplot(data)

#plt.xticks([1, 2, 3, 4, 5], ['0.0001', '0.0003', '0.001', '0.003', '0.01'])
#plt.xticks([1, 2, 3], ['1', '2', '3'])
plt.xticks([1, 2, 3, 4, 5, 6], ['2048', '4096', '8192', '16384', '32768', '65536'])

#ax.set_title('Loss nach 7 Stunden Training, pro Batchverwendungsanzahl je 5 trainierte Modelle')
#ax.set_title('Loss nach 7 Stunden Training, pro Lernrate je 5 trainierte Modelle')
ax.set_title('Loss nach 7 Stunden Training, pro Batchgröße je 5 trainierte Modelle')

#ax.set_xlabel('Anzahl an Batchverwendungen')
#ax.set_xlabel('Lernrate')
ax.set_xlabel('Batchgröße')
ax.set_ylabel('Loss')
plt.show()
print("done")