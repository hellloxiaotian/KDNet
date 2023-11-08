import os
import random

import shutil
from shutil import copy2
trainfiles = os.listdir(" ")
num_train = len(trainfiles)
index_list = list(range(num_train))
random.shuffle(index_list)
num = 0
trainDir = " "
validDir = " "
for i in index_list:
    fileName = os.path.join(" ", trainfiles[i])
    if num < num_train*0.6:  # 6:4
        print(str(fileName))
        copy2(fileName, trainDir)
    else:
        print(str(fileName))
        copy2(fileName, validDir)
    num += 1
