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

dir = "../Data/Test"
files = os.listdir(dir)
ball_touch_end = 0
for f in files:
    tensor = torch.load(os.path.join(dir, f))
    n = tensor.shape[0]-1
    if tensor[n][26] == 1:
        ball_touch_end +=1
    if tensor[n][64] == 1:
        ball_touch_end +=1
print(f"ball touch last frame: {ball_touch_end}")
print("done")
