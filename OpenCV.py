import cv2

#Now we have to read the image,by pasting the directory of the image
#0 means Grayscale

img=cv2.imread('C:\\Users\\heman\\Pictures\\download.JPG', 0)
#Now read the image
cv2.imshow('Demo image', img)

#Now assign a variable to waitkey,in this case we use key ESC which is 27
#0 means it waits for infinite seconds  for the key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()