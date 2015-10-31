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


fileName = 'day28apr2009.jpg'

image = OpenImageFile(fileName)
similarityImage = rgb2gray(image)

NumberOfRows = image.shape[0]
NumberOfColumns = image.shape[1]

HSW = 32
interval = 32
RW = interval/2

for y in range(0,NumberOfRows,interval):
    print(str(y))
    for x in range(0,NumberOfColumns,interval):

        list8 = CreateColorHistorGram(image,y-HSW,y+HSW,x-HSW,x+HSW, False)

        similarityValue = 1 - HistogramSimilarity(list8,averageHistogram)

        intensity = int(255*similarityValue)

        if (intensity > 255):
            print("WARNING " + str(intensity))

        similarityImage = ColorImageRegion(similarityImage,y-RW,y+RW,x-RW,x+RW, intensity)


io.imshow(image)
io.show()
io.imshow(similarityImage)
io.show()
similarityImage = ApplyThresholdToImage(similarityImage)
io.imshow(similarityImage)
io.show()
