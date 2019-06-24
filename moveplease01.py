#!/usr/bin/python3

import os
import shutil

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'mani_storage/')

xname= input("what is the new name for kerrigan.obj?")

shutil.move('mani_storage/kerrigan.obj', 'mani_storage/' + xname)
