import math
import os
import sys

from IO_manager import Directories
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dirs = Directories()
exp_dir = "../Ergebnisse/Baseline/"

train_data = {}
test_data = {}
steps = []
train_step_data = {}
test_step_data = {}
exps = os.listdir(exp_dir)
exps.sort()
test_path = exp_dir + exps[0] + "/Testdaten"
test_file = os.listdir(test_path)[0]
test_df = pd.read_csv(test_path + "/" + test_file)
steps_df = test_df["Step"]
for i in range(steps_df.shape[0] - 1):
    steps.append(steps_df[i])

for exp in exps:
    train_path = exp_dir + exp + "/Trainingsdaten"
    test_path = exp_dir + exp + "/Testdaten"
    train_files = os.listdir(train_path)
    for f in train_files:
        if f.startswith("run"):
            f_cut = f[29:]
            if f_cut[1] == "-":
                f_cut = "0" + f_cut
            os.rename(os.path.join(train_path, f), os.path.join(train_path, f_cut))
    train_files = os.listdir(train_path)
    train_files.sort()
    test_file = os.listdir(test_path)[0]
    test_df = pd.read_csv(test_path + "/" + test_file)
    current_step = 1000000000
    train_values = []
    test_values = []
    train_steps = []
    test_steps = []
    angle = False
    if exps[10] == exp or exps[11] == exp:
        angle = True
    for i in range(test_df.shape[0]):
        value = test_df["Value"][i]
        if angle:
            value = np.degrees(np.arccos(value))
        test_values.append(value)
        test_steps.append(test_df["Step"][i])
    train_step_size = 1000000000
    value_sum = 0
    skipped_steps = 0
    for f in train_files:
        df = pd.read_csv(train_path + "/" + f)
        for i in range(df.shape[0]):
            value = df["Value"][i]
            if angle:
                value = np.degrees(np.arccos(value))
            value_sum += value
            skipped_steps += 1
            if df["Step"][i] < current_step:
                continue
            else:
                train_values.append(value_sum / skipped_steps)
                train_steps.append(df["Step"][i])
                current_step += train_step_size
                value_sum = 0
                skipped_steps = 0

    train_data[exp] = np.array(train_values)
    test_data[exp] = np.array(test_values)
    train_step_data[exp] = np.array(train_steps)
    test_step_data[exp] = np.array(test_steps)

columns = 2
rows = 3
os = [[1, 7, 3, 13, 5, 15], [10, 11], [18, 20, 22, 24], [25, 0]]
rc = [[3, 2], [1, 2], [2, 2], [1, 2]]
plotnumber = 2
figure, axis = plt.subplots(rc[plotnumber][0], rc[plotnumber][1])
figure.set_size_inches(6.40, 2.4 * rc[plotnumber][0])

for i in range(rc[plotnumber][0] * rc[plotnumber][1]):
    exp = exps[os[plotnumber][i]]
    plot = None
    if rc[plotnumber][0] == 1:
        plot = axis[i]
    else:
        plot = axis[math.floor(i / rc[plotnumber][1]), i % rc[plotnumber][1]]
    plot.plot(test_step_data[exp], test_data[exp], label="Test")
    plot.plot(train_step_data[exp], train_data[exp], label="Training")
    title = exp[3:]
    plot.set_title(title)
    plot.legend()
'''
figure, axis = plt.subplots(1, 2)
for i in range(2):
    exp = exps[os[plotnumber][i]]
    axis[i].plot(test_step_data[exp], test_data[exp], label="Test")
    axis[i].plot(train_step_data[exp], train_data[exp], label="Training")
    title = exp[3:]
    axis[i].set_title(title)
    axis[i].legend()
'''
# Combine all the operations and display
figure.tight_layout()
plt.show()
figure.savefig(f"../Bilder/timeplot{str(plotnumber)}.svg")
print("done")
