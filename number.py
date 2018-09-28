import os
fileDir = '/home/isio/data/COSI/why'
print len([name for name in os.listdir(fileDir) if os.path.isfile(os.path.join(fileDir, name))])