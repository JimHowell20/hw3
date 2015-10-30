__author__ = 'jimmy'

from functions import *
from skimage import img_as_ubyte
import random

#START of PROGRAM

fileName1 = 'tiger.jpg'

image = io.imread(fileName1)
image = img_as_ubyte(image)

datatype = image.dtype

CreateColorHistorGram(image)
