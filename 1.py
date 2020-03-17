# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:55:28 2020

@author: Mahdi
"""

import matplotlib.pyplot as plt
import cv2     # for capturing videos
import os
import numpy as np

os.chdir("C:\\Users\\Mahdi\\Desktop")

#image = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
image = cv2.imread('1.jpg')

b,g,r = cv2.split(image)        #Splits the BGR channels in blue,green,red vectors.
picture = cv2.merge([r,g,b])    #Merges in RGB format

# plt.subplot(121)
# plt.imshow(image)
# plt.subplot(122)
# plt.imshow(picture)
# plt.show()


# cv2.imshow("my image",picture)
# cv2.waitKey()
# cv2.destroyAllWindows()

main_image_vertically = np.concatenate((image,picture),axis = 0)
main_image_horizontally = np.concatenate((image,picture),axis = 1)

plt.subplot(121)
plt.imshow(main_image_vertically)
plt.subplot(122)
plt.imshow(main_image_horizontally)
plt.show()
