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

# Person # 4
fileName = '80-of-people-arent-using-linkedin-the-way-theyre-supposed-to.jpg'

list4 = CreateColorHistorGram(fileName,17,299,145,360)
listOfHistograms.append(list4)

# Person # 5
fileName = '1319023.jpg'

list5 = CreateColorHistorGram(fileName,25,560,70,408)
listOfHistograms.append(list5)


# Person # 6
fileName = '3442168664_d1f4b7cc67.jpg'

list6 = CreateColorHistorGram(fileName,10,285,75,292)
listOfHistograms.append(list6)


# Person # 7
fileName = 'breaking_bad_people2.jpg'

list7 = CreateColorHistorGram(fileName,95,306,275,400)
listOfHistograms.append(list7)

# Person # 8
fileName = 'mountfordpompeii2_2521445b.jpg'

list8 = CreateColorHistorGram(fileName,110,285,137,275)
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


