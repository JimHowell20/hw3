__author__ = 'jimmy'

from skimage import img_as_ubyte
from skimage.morphology import closing
from skimage.morphology import opening
from skimage import data, io
from numpy.random import normal, uniform
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import disk

foregroundPixelValue = 0
backgroundPixelValue = 0

drawFaceImages = False

def HistogramSimilarity( list, averageList):
    distance = 0
    listIndex = 0

    for value in list:
        averageValue = averageList[listIndex]
        distance += (value-averageValue)**2
        listIndex +=1

    return (distance**0.5)


def ApplyThresholdToImage(image2):

    image = rgb2gray(image2)

    global foregroundPixelValue
    global backgroundPixelValue

    thresholdValue = 170

    NumberOfRows = image.shape[0]
    NumberOfColumns = image.shape[1]

    numberOfBlackPixels = 0
    numberOfWhitePixels = 0
    selem = disk(5)

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

    # assume foreground has more pixels in face region
    if (numberOfWhitePixels > numberOfBlackPixels):
        foregroundPixelValue = 1
        backgroundPixelValue = 0
        #print("foreground color is white")
    else:
        foregroundPixelValue = 0
        backgroundPixelValue = 1
        #print("foreground color is black")

    image = opening(image,selem)
    if (foregroundPixelValue == 0):
        image = opening(image,selem)
    else:
        image = closing(image,selem)


    if drawFaceImages:
        io.imshow(image)
        io.show()

    return image

def ApplyThresholdToImageRegion(image2, Tb, Bb, Lb, Rb,shouldThresholdImage):

    image = rgb2gray(image2)

    global foregroundPixelValue
    global backgroundPixelValue

    thresholdValue = threshold_otsu(image)

    NumberOfRows = image.shape[0]
    NumberOfColumns = image.shape[1]

    numberOfBlackPixels = 0
    numberOfWhitePixels = 0
    selem = disk(3)

    # simpe thresholding
    for y in range(NumberOfRows):
        for x in range(NumberOfColumns):

            isWithinBoundary = IsWithinBoundary(y,x,image2, Tb, Bb, Lb, Rb,shouldThresholdImage)

            if (isWithinBoundary):
                if image[y,x] > thresholdValue:
                    #black
                    image[y,x] = 0
                    numberOfBlackPixels += 1
                else:
                    #white
                    image[y,x] = 1
                    numberOfWhitePixels += 1

    # assume foreground has more pixels in face region
    if (numberOfWhitePixels > numberOfBlackPixels):
        foregroundPixelValue = 1
        backgroundPixelValue = 0
        #print("foreground color is white")
    else:
        foregroundPixelValue = 0
        backgroundPixelValue = 1
        #print("foreground color is black")

    image = opening(image,selem)
    if (foregroundPixelValue == 0):
        image = opening(image,selem)
    else:
        image = closing(image,selem)


    if drawFaceImages:
        io.imshow(image)
        io.show()

    return image

def UpdateDictKeyValue(dictionary,key,value):
    valueCheck = dictionary.get(key)

    if valueCheck == None:
        dictionary[key] = value
    else:
        dictionary[key] += value

def OpenImageFile(fileName):
    image = io.imread(fileName)
    image = img_as_ubyte(image)
    return image

def IsWithinBoundary(y,x,image,TopRegionBoundary,BottomRegionBoundary,LeftRegionBoundary,RightRegionBoundary,shouldThresholdImage):

    if (shouldThresholdImage):
        #Mark Boundary
        if (x == LeftRegionBoundary or x == RightRegionBoundary) and (y <= BottomRegionBoundary and y >= TopRegionBoundary):
            image[y,x] = [255,0,0]
        if (y == BottomRegionBoundary or y == TopRegionBoundary) and (x <= RightRegionBoundary and x >= LeftRegionBoundary):
            image[y,x] = [255,0,0]

    if (x < LeftRegionBoundary or x > RightRegionBoundary):
        return False
    elif (y > BottomRegionBoundary or y < TopRegionBoundary):
        return False
    else:
        return True

def ColorImageRegion(image, Tb, Bb, Lb, Rb, intensity):

    NumberOfRows = image.shape[0]
    NumberOfColumns = image.shape[1]

    if Tb < 0:
        Tb = 0
    if Bb > NumberOfRows:
        Bb = NumberOfRows
    if Lb < 0:
        Lb = 0
    if Rb > NumberOfColumns:
        Rb = NumberOfColumns

    for y in range(Tb,Bb):
        for x in range(Lb,Rb):
            image[y,x] = intensity

    return image


def CreateColorHistorGram(image, Tb, Bb, Lb, Rb, shouldThresholdImage):

    NumberOfRows = image.shape[0]
    NumberOfColumns = image.shape[1]

    if Tb < 0:
        Tb = 0
    if Bb > NumberOfRows:
        Bb = NumberOfRows
    if Lb < 0:
        Lb = 0
    if Rb > NumberOfColumns:
        Rb = NumberOfColumns

    binaryImage = image

    if shouldThresholdImage:
        binaryImage = ApplyThresholdToImageRegion(image, Tb, Bb, Lb, Rb,shouldThresholdImage)


    numberOfXbins = 64

    BinCountDictionary = {}
    BinCountList = [None]*numberOfXbins
    IndexList = [None]*numberOfXbins

    pixelCount = 0
    for y in range(Tb,Bb):
        for x in range(Lb,Rb):

            isWithinBoundary = IsWithinBoundary(y,x,image, Tb, Bb, Lb, Rb, shouldThresholdImage)

            if isWithinBoundary:

                if shouldThresholdImage:
                    isFacePixel = (binaryImage[y,x] == foregroundPixelValue)

                if not shouldThresholdImage or isFacePixel:
                    rgbValues = image[y,x]

                    R = rgbValues[0]
                    G = rgbValues[1]
                    B = rgbValues[2]

                    #image[y,x] = (0,255,0)

                    RBin = R//numberOfXbins
                    GBin = G//numberOfXbins
                    BBin = B//numberOfXbins

                    key = (RBin,GBin,BBin)

                    pixelCount += 1
                    UpdateDictKeyValue(BinCountDictionary,key,1)

    #Show Boundary of Region
    if drawFaceImages:
        io.imshow(image)
        io.show()

    binIndex = 0
    for x in range(4):
        for y in range(4):
            for z in range(4):
                key = (x,y,z)

                binCount = BinCountDictionary.get(key)

                if (binCount == None):
                        binCount = 0

                BinCountList[binIndex] = binCount/float(pixelCount)
                IndexList[binIndex] = binIndex

                ps = " Bin #: " + str(key) + " Count: " + str(binCount)
                #print(ps)

                binIndex += 1

    #Draw Histogram
    # fig = plt.figure()
    # ax = fig.add_subplot(1,1,1)
    #
    # xmajor_ticks = np.arange(0, numberOfXbins, 1)
    #
    # ax.set_xticks(xmajor_ticks)
    #
    # plt.bar(IndexList, BinCountList)
    # plt.show()

    return BinCountList