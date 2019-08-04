#Image Cropping import cv2
from PIL import Image

#Now read the image
img= Image.open('C:\\Users\\heman\\Pictures\\download.JPG')

area = (77,102,149,147)
newimg=img.crop(area)
newimg.show()




