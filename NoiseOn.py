import numpy as np
import random
import cv2
from matplotlib import pyplot as plt


def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('C:\\Users\\heman\\Pictures\\IMG-3101.JPG',1) # Only for grayscale image
noise_img = sp_noise(image,0.05)
cv2.imwrite('sp_noise.jpg', noise_img)
plt.subplot(121),plt.imshow(image,cmap='gray')
plt.subplot(122),plt.imshow(noise_img,cmap='gray')
plt.show()


