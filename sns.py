import numpy as np
import cv2

img=cv2.imread('C:\\Users\\heman\\Pictures\\download.JPG',1)
px= img[100,100]
#Now print the BGR values
print(px)

blue= img[:,:,0]
print(blue)
img.show()



