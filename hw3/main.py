__author__ = 'jimmy'

from functions import *
from skimage import img_as_ubyte
import random

#START of PROGRAM

fileName1 = '388070.jpg'

image = io.imread(fileName1)
image = img_as_ubyte(image)

datatype = image.dtype

# TopRegionBoundary = 32
# BottomRegionBoundary = 65
#
# LeftRegionBoundary = 52
# RightRegionBoundary = 74
CreateColorHistorGram(image,32,65,52,74)
