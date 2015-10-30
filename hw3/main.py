__author__ = 'jimmy'

from functions import *

#START of PROGRAM

# Tb, Bb, Lb, Rb

# Dude
fileName = '302001.jpg'

image = OpenImageFile(fileName)

list1 = CreateColorHistorGram(image,16,62,12,56)

# Girl
fileName = '388070.jpg'

image = OpenImageFile(fileName)

list2 = CreateColorHistorGram(image,36,63,55,70)
