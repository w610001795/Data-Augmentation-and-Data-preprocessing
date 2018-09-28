# -*- coding: utf-8 -*-
#把带七的注销掉就是原来的啦！
import os
import random
import shutil

fileDir = '/home/isio/data/COSI/1/'
#fileDir7 = '/home/isio/data/COSI/BSQH/00000_17/'
#fileDir17 = '/home/isio/data/COSI/BSQH/00000_27/'
#fileDir27 = '/home/isio/data/COSI/BSQH/00000_37/'
#fileDir37 = '/home/isio/data/COSI/BSQH/00001_37/'
tarDir = '/home/isio/data/COSI/new_train/00001/'

pathDir = os.listdir(fileDir)
sample = random.sample(pathDir, 2048)
print(sample)

for name in sample:
	shutil.move(fileDir+name, tarDir+name)
	#shutil.move(fileDir7+'17_'+name, tarDir+'17_'+name)
	#shutil.move(fileDir17+'27_'+name, tarDir+'27_'+name)
	#shutil.move(fileDir27+'37_'+name, tarDir+'37_'+name)
	#shutil.move(fileDir37+'37_'+name, tarDir+'37_'+name)

print("END")
