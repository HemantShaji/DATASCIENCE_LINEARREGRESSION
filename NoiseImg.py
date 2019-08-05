import cv2
import matplotlib.pyplot as plt
import numpy as np


#Create a fn Main

def main():

 img=cv2.imread('C:\\Users\\heman\\Pictures\\IMG-2994.JPG',1)
 output = img
 #show the output of the image using matplotlib
 plt.imshow(output)
 #Introduce the title of the image
 plt.title('Orginal image')
 #Show the image
 plt.show()



if __name__== "__main__":
    main()
