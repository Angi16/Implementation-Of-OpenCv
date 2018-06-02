#Adding Text to Images:

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Anjali',(10,250), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)