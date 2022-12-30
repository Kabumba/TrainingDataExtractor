import os
import shutil

import torch

from IO_manager import Directories

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

def remove_suffix(string, suffix):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string

cp_dir = "../Experimente/BaselineTest/Checkpoints"
files = os.listdir(cp_dir)
cphs = []
dirs = []
for f in files:
    if f.endswith(".cph"):
        cphs.append(f)
    else:
        dirs.append(f)
print(cphs)
cp_indices = []
for f in cphs:
    cp = remove_prefix(f, "cph_")
    cp = remove_suffix(cp, ".cph")
    cp_indices.append(int(cp))
cp_indices.sort()
print(dirs)
for dir in dirs:
    path = cp_dir + "/" + dir
    cps = os.listdir(path)
    for f in cps:
        a = remove_suffix(f, ".cp")
        remove = True
        for i in cp_indices:
            if a.endswith(str(i)):
                remove = False
        if remove:
            os.remove(path + "/" + f)
print("done")
