__author__ = 'jimmy'

from skimage import data, io
from numpy.random import normal, uniform
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt


def ApplyThresholdToImage(image):

    thresholdValue = threshold_otsu(image)

    NumberOfRows = image.shape[0]
    NumberOfColumns = image.shape[1]

    numberOfBlackPixels = 0
    numberOfWhitePixels = 0

    # simpe thresholding
    for y in range(NumberOfRows):
        for x in range(NumberOfColumns):
            if image[y,x] > thresholdValue:
                #black
                image[y,x] = 0
                numberOfBlackPixels += 1
            else:
                #white
                image[y,x] = 1
                numberOfWhitePixels += 1

def UpdateDictKeyValue(dictionary,key,value):
    valueCheck = dictionary.get(key)

    if valueCheck == None:
        dictionary[key] = value
    else:
        dictionary[key] += value

def IsWithinBoundary(y,x):
    LeftRegionBoundary = 10
    RightRegionBoundary = 300
    BottomRegionBoundary = 200
    TopRegionBoundary = 100

    if (x < LeftRegionBoundary or x > RightRegionBoundary):
        return False
    elif (y > BottomRegionBoundary or y < TopRegionBoundary):
        return False
    else:
        return True

def CreateColorHistorGram(image):

    NumberOfRows = image.shape[0]
    NumberOfColumns = image.shape[1]

    numberOfXbins = 64

    HValues = {}
    HValueList = [None]*numberOfXbins
    IndexList = [None]*numberOfXbins


    for y in range(NumberOfRows):
        for x in range(NumberOfColumns):

            rgbValues = image[y,x]

            isWithinBoundary = IsWithinBoundary(y,x)

            if isWithinBoundary:
                image[y,x] = [255,0,0]

            R = rgbValues[0]
            G = rgbValues[1]
            B = rgbValues[2]

            RBin = R//numberOfXbins
            GBin = G//numberOfXbins
            BBin = B//numberOfXbins

            key = (RBin,GBin,BBin)

            UpdateDictKeyValue(HValues,key,1)

    io.imshow(image)
    io.show()

    index = 0
    for x in range(4):
        for y in range(4):
            for z in range(4):
                key = (x,y,z)

                dictValue = HValues.get(key)

                if (dictValue == None):
                        dictValue = 0

                HValueList[index] = dictValue
                IndexList[index] = index

                ps = " Bin #: " + str(key) + " Count: " + str(dictValue)
                print(ps)

                index += 1

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    xmajor_ticks = np.arange(0, numberOfXbins, 1)

    ax.set_xticks(xmajor_ticks)

    plt.bar(IndexList, HValueList)
    plt.show()