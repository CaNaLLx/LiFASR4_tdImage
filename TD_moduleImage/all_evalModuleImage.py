#!/usr/bin/python3
import os
import glob

def listarchives():
    l = []
    files = glob.glob("*.*")
    for f in files:
        if f.find(".tar.gz") != -1 or f.find(".tgz") != -1 or f.find(".tar") != -1 or f.find(".zip") != -1:
            l.append(f)
    return l

os.system('clear')
archives = listarchives()
print("Execution du script pour "+str(len(archives))+" archives.\n")
for a in archives:
    os.system("python3 evalModuleImage.py "+a)
