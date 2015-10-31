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

list1 = CreateColorHistorGram(fileName,16,62,12,56)
listOfHistograms.append(list1)

# Girl
fileName = '388070.jpg'

list2 = CreateColorHistorGram(fileName,36,63,55,70)
listOfHistograms.append(list2)

# Ross
fileName = 'ross022500197.jpg'

list3 = CreateColorHistorGram(fileName,80,192,80,175)
listOfHistograms.append(list3)


fileName = '80-of-people-arent-using-linkedin-the-way-theyre-supposed-to.jpg'

list4 = CreateColorHistorGram(fileName,17,299,145,360)
listOfHistograms.append(list4)


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


