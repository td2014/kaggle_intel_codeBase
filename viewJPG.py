# Simple code to read in some training data and
# view images in sequence.
#
# Anthony L. Daniell
# April 12, 2017
#
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

#
# open a camera directory and load files (sorted by alpha).
#

mypath='/Users/anthonydaniell/Desktop/FilesToSync/Research/Kaggle/IntelCervix/train/Type_2'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
###print onlyfiles
#
# Load and display images
#
i=0
skip=1
for inFile in onlyfiles:
    if i % skip == 0:
        fullFile = mypath + '/' + inFile
        print ('inFile = ', inFile)
        print ('fullFile = ', fullFile)
        try:
           img = cv2.imread(fullFile,1)
           img_out = cv2.resize(img, (256,256))
           cv2.imshow('bgr image',img_out)
           cv2.waitKey(0)
           cv2.destroyAllWindows()
        except:
           pass
    i+=1
#
# End of script
#
