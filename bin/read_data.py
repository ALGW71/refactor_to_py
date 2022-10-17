import os
import sys
import csv

dir = os.getcwd()

PATH = dir + "/../input"

dirlist = []


for root, dirs, files in os.walk(PATH, topdown=False):
   for name in files:
     dirlist.append(os.path.join(root, name))

print(dirlist[0])
