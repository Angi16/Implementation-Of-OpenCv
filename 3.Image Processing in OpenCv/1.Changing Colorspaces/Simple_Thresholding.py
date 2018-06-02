#OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function.

#Different types are:

	#cv2.THRESH_BINARY
	#cv2.THRESH_BINARY_INV
	#cv2.THRESH_TRUNC
	#cv2.THRESH_TOZERO
	#cv2.THRESH_TOZERO_INV

	
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/OpenCv Image - processing/Lighthouse.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
	
plt.show()