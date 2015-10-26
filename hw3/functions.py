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

def CreateColorHistorGram(image):

    NumberOfRows = image.shape[0]
    NumberOfColumns = image.shape[1]

    numberOfXbins = 64

    HValues = {}
    HValueList = [None]*numberOfXbins
    IndexList = [None]*numberOfXbins

    # simpe thresholding
    for y in range(NumberOfRows):
        for x in range(NumberOfColumns):

            rgbValues = image[y,x]

            R = rgbValues[0]
            G = rgbValues[1]
            B = rgbValues[2]

            RBin = R//numberOfXbins
            GBin = G//numberOfXbins
            BBin = B//numberOfXbins

            key = (RBin,GBin,BBin)

            UpdateDictKeyValue(HValues,key,1)

            # redValueList.append(R)
            # greenValueList.append(G)
            # blueValueList.append(B)


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

                ps = " Bin #: " + str(index) + " Count: " + str(dictValue)
                print(ps)

                index += 1

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    # major ticks every 20, minor ticks every 5
    xmajor_ticks = np.arange(0, 63, 1)

    ax.set_xticks(xmajor_ticks)

    # plt.hist(HValueList, bins=4, color='blue')
    # plt.show()

    plt.bar(IndexList, HValueList)
    plt.show()