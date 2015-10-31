__author__ = 'jimmy'

from functions import *

#START of PROGRAM

# Tb, Bb, Lb, Rb

numberOfXbins = 64
listOfHistograms = []
averageHistogram = [0]*numberOfXbins
IndexList = [0]*numberOfXbins

# Dude
fileName = '302001.jpg'

image = OpenImageFile(fileName)
list1 = CreateColorHistorGram(image,16,62,12,56, True)
listOfHistograms.append(list1)

# Girl
fileName = '388070.jpg'

image = OpenImageFile(fileName)
list2 = CreateColorHistorGram(image,36,63,55,70, True)
listOfHistograms.append(list2)

# Ross
fileName = 'ross022500197.jpg'

image = OpenImageFile(fileName)
list3 = CreateColorHistorGram(image,80,192,80,175, True)
listOfHistograms.append(list3)

# Person # 4
fileName = '80-of-people-arent-using-linkedin-the-way-theyre-supposed-to.jpg'

image = OpenImageFile(fileName)
list4 = CreateColorHistorGram(image,17,299,145,360, True)
listOfHistograms.append(list4)

# Person # 5
fileName = '1319023.jpg'

image = OpenImageFile(fileName)
list5 = CreateColorHistorGram(image,25,560,70,408, True)
listOfHistograms.append(list5)


# Person # 6
fileName = '3442168664_d1f4b7cc67.jpg'

image = OpenImageFile(fileName)
list6 = CreateColorHistorGram(image,10,285,75,292, True)
listOfHistograms.append(list6)


# Person # 7
fileName = 'breaking_bad_people2.jpg'

image = OpenImageFile(fileName)
list7 = CreateColorHistorGram(image,95,306,275,400, True)
listOfHistograms.append(list7)

# Person # 8
fileName = 'mountfordpompeii2_2521445b.jpg'

image = OpenImageFile(fileName)
list8 = CreateColorHistorGram(image,110,285,137,275, True)
listOfHistograms.append(list8)



for list in listOfHistograms:
    listIndex = 0
    for value in list:
        averageHistogram[listIndex] += value
        listIndex += 1

listIndex = 0
for value in averageHistogram:
    total = averageHistogram[listIndex]
    numberOfLists = len(listOfHistograms)
    averageHistogram[listIndex] = total / float(numberOfLists)

    IndexList[listIndex] = listIndex
    listIndex += 1


#Draw Histogram
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

xmajor_ticks = np.arange(0, numberOfXbins, 1)

ax.set_xticks(xmajor_ticks)

plt.bar(IndexList, averageHistogram)
plt.show()


print("finished running")


fileName = 'hw3test1.jpg'

image = OpenImageFile(fileName)
similarityImage = rgb2gray(image)

NumberOfRows = image.shape[0]
NumberOfColumns = image.shape[1]

HSW = 8
interval = 4
RW = interval/2

for y in range(interval,NumberOfRows,interval):
    percentComplete =int((y/float(NumberOfRows))*100)
    print(str(percentComplete)+ " % ")
    for x in range(interval,NumberOfColumns,interval):

        list8 = CreateColorHistorGram(image,y-HSW,y+HSW,x-HSW,x+HSW, False)

        similarityValue = 1 - HistogramSimilarity(list8,averageHistogram)

        intensity = int(255*similarityValue)

        if (intensity > 255):
            print("WARNING " + str(intensity))

        similarityImage = ColorImageRegion(similarityImage,y-RW,y+RW,x-RW,x+RW, intensity)

io.imshow(similarityImage)
io.show()
binarySimilarityImage = ApplyThresholdToImage(similarityImage.copy())
io.imshow(similarityImage)
io.show()


# label image regions
NumberOfRows = image.shape[0]
NumberOfColumns = image.shape[1]

label_image = label(binarySimilarityImage)

for region in regionprops(label_image):

    # draw rectangle around segmented coins
    minr, minc, maxr, maxc = region.bbox

    Tb = minr
    Bb = maxr

    Lb = minc
    Rb = maxc

    if Tb < 0:
        Tb = 0
    if Bb > NumberOfRows:
        Bb = NumberOfRows
    if Lb < 0:
        Lb = 0
    if Rb > NumberOfColumns:
        Rb = NumberOfColumns

    numberOfXbins = 64

    for y in range(Tb,Bb):
        for x in range(Lb,Rb):

            midY = (Tb+Bb)/2.0
            midX = (Lb+Rb)/2.0
            blobIntensity = similarityImage[midY,midX]

            difference = blobIntensity - 170

            print(difference)

            color = (255,0,0)
            if difference > 0 and difference < 5:
                color = (255,0,0)
            if difference > 5 and difference < 30:
                color = (0,255,0)
            if difference > 30:
                color = (0,0,255)

            isWithinBoundary = drawBoundaryWithColor(y,x,image, Tb, Bb-1, Lb, Rb-1, color)

io.imshow(image)
io.show()