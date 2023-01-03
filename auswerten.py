import os
from IO_manager import Directories
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dirs = Directories()
exp_dir = "../Ergebnisse/"

exps = [["2k",
         "4k",
         "8k",
         "16k 0.001",
         "32k",
         "64k"],
        ["16k 0.001",
         "2rep",
         "3rep"],
        ["16k 0.0001",
         "16k 0.0003",
         "16k 0.001",
         "16k 0.003",
         "16k 0.01"]
        ]

data = [[], [], []]
for j in range(len(exps)):
    for exp in exps[j]:
        path = exp_dir + exp + "/TrainingLoss"
        files = os.listdir(path)
        losses = []
        for f in files:
            df = pd.read_csv(path + "/" + f)
            starttime = df["Wall time"][0]
            reftime = starttime + 7 * 60 * 60
            refstep = 1200000000
            for i in range(df.shape[0]):
                # if df["Wall time"][i]<reftime:
                if df["Step"][i] < refstep:
                    continue
                else:
                    # losses.append(df["Step"][i]/161959504.0)
                    # losses.append(df["Value"][i]/(df["Step"][i]/161959504.0))
                    losses.append(df["Value"][i])
                    break
        data[j].append(losses)
fig = plt.figure(figsize=(10, 7))
fig.set_size_inches(6.40, 2.4 * 2)
# Creating plot
# = plt.boxplot(data)

# show plot
# fig.suptitle('Traingsloss nach 7 Stunden', fontsize=14, fontweight='bold')

plotnumber = 2

ax = fig.add_subplot(111)
ax.boxplot(data[plotnumber])
axes = [['2048', '4096', '8192', '16384', '32768', '65536'],
        ['1', '2', '3'],
        ['0.0001', '0.0003', '0.001', '0.003', '0.01']]
plt.xticks(range(1, len(axes[plotnumber])+1), axes[plotnumber])

titles = ["Loss nach 7 Stunden Training je Batchgröße",
          'Loss nach 7 Stunden Training je Batchverwendungsanzahl',
          'Loss nach 7 Stunden Training je Lernrate']

# ax.set_title('Loss nach 7 Stunden Training, pro Batchverwendungsanzahl je 5 trainierte Modelle')
# ax.set_title('Loss nach 7 Stunden Training, pro Lernrate je 5 trainierte Modelle')
ax.set_title(titles[plotnumber])

xlabels = ['Batchgröße',
           'Anzahl an Batchverwendungen',
           'Lernrate']

ax.set_xlabel(xlabels[plotnumber])
ax.set_ylabel('Loss')
plt.show()


'''figure, axis = plt.subplots(1, 3)
figure.set_size_inches(6.40, 2.4 * 1)
axis[0].boxplot(data[0])
axis[0].xticks([1, 2, 3, 4, 5, 6], ['2048', '4096', '8192', '16384', '32768', '65536'])
axis[0].set_title("Batchgröße")
axis[1].boxplot(data[1])
axis[1].set_title("Batchverwendungen")
axis[2].boxplot(data[2])
axis[2].set_title("Lernrate")
# Combine all the operations and display
figure.tight_layout()
plt.show()'''
fig.savefig(f"../Bilder/boxplot{plotnumber}.svg")
print("done")
