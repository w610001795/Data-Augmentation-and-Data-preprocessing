# -*- coding: utf-8 -*-

import os
import sys
import shutil

addressPNG = '/home/isio/data/COSI/BSQH/00001_quan_7-37/'
targetDir = '/home/isio/data/COSI/BSQH/00001_7/'
i = 0

def getFileList(path):
    filenames_set = set()
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            filenames_set.add(dirpath  + '/'+ file)
    return filenames_set


def copyPNG(subStr, filenames_set, i):
    for fileNAME in filenames_set:
        dir, strfile = os.path.split(fileNAME)
        if strfile.find(subStr)>=0:
			oldname = fileNAME
			#i2 = str(i)
			#i3 = i2.zfill(6)
			newname = targetDir+ strfile
			shutil.move(oldname, newname)
			#i+=1
			print('copy over')

if __name__ == '__main__':
#    if not os.path.exists(targetDir):
#        os.makedirs(targetDir)
    filenames_set = getFileList(addressPNG)
    while 1:
        str2 = raw_input()
        copyPNG(str2, filenames_set, i)
