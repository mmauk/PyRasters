import numpy as np
import matplotlib.pyplot as plt
import os
from sys import platform

def determineCellType(File):
    cellType = (File[len(File)-3:len(File)])
    numNeurons = 0
    if (cellType =="grr"):      # Sets numNeurons according to neuron type  
        numNeurons = 2 ** 20
        numNeurons = 4000       # Have to look at fewer granule cells because run out of memory if too many
    elif (cellType =="mfr"):
        numNeurons = 4096
    elif (cellType =="gor"):
        numNeurons = 4096
    elif (cellType =="ncr"):
        numNeurons = 8
    elif (cellType =="pcr"):
        numNeurons = 32
    elif (cellType =="bcr"):
        numNeurons = 128
    elif (cellType =="scr"):
        numNeurons = 512
    elif (cellType =="ior"):
        numNeurons = 4
    print(cellType,numNeurons)
    return cellType, numNeurons

def makeFiles(filename): ## need to check os type and do different slashes for linux and mac
    currentPath = os.getcwd()
    OStype = 0
    if platform[0:3]=="win":
        OStype = 1
    fileType = filename[len(filename)-3:]
    fileRoot = filename[0:len(filename)-4]
    if OStype ==1:                          # this hasn't yet been tested in mac or linux
        rasterSave = currentPath + "\\" + fileRoot + "_" + fileType + ".npy"
        activitySave = currentPath + "\\" + fileRoot + "_" + fileType + ".act"
    else:
        rasterSave = currentPath + "/" + fileRoot + "_" + fileType + ".npy"
        activitySave = currentPath + "/" + fileRoot + "_" + fileType + ".act"
    print(currentPath,fileType,fileRoot,rasterSave,activitySave)
    return rasterSave, activitySave