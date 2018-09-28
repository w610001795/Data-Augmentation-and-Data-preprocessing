# -*- coding: utf-8 -*-

import os
import random
import shutil
from rotate import rotation
import time
import progressbar

N = 1000   #edit
num = 4    #edit

bar = progressbar.ProgressBar(widgets=[
    'Being in progerss:' ,
    progressbar.Percentage(),
    ' (', progressbar.SimpleProgress(), ') ',
    ' (', progressbar.ETA(), ') ',
    '(',progressbar.Bar(), ') ',])
#fileDir = '/home/isio/data/COSI/0/' #edit
#tarDir = '/home/isio/data/COSI/new_train/00000/'  #edit

fileDir = '/home/isio/data/COSI/why_num/00001/' #edit
tarDir = '/home/isio/data/COSI/why3/'  #edit

pathDir = os.listdir(fileDir)
sample = random.sample(pathDir, N)
print(sample)

for i in bar(range(N)):
    name = sample[i]
    rotation(fileDir+name, tarDir, num, name)
    shutil.move(fileDir+name, tarDir+name)

print("END")