__author__ = 'jimmy'

from functions import *

#START of PROGRAM

# Tb, Bb, Lb, Rb

# Dude
fileName = '302001.jpg'

image = OpenImageFile(fileName)

list1 = CreateColorHistorGram(image,16,62,12,56)

ApplyThresholdToImage(image)

# Girl
fileName = '388070.jpg'

image = OpenImageFile(fileName)

list2 = CreateColorHistorGram(image,36,63,55,70)

ApplyThresholdToImage(image)


fileName = 'ross022500197.jpg'

image = OpenImageFile(fileName)
ApplyThresholdToImage(image)

fileName = 'south-park03.jpg'

image = OpenImageFile(fileName)
ApplyThresholdToImage(image)