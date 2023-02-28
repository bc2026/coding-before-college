import cv2 as cv
import sys


imgFileName = "img.jpg"
img = cv.imread(cv.samples.findFile(imgFileName))

if img is None:
    sys.exit("Could not read the image or the file", imgFileName,)


cv.imshow("Diplay window", img)
k = cv.waitKey(0)


if k == ord("s"):
    cv.imwrite(imgFileName, img)

