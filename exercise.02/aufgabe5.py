#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Aufgabe 5

import numpy as np
import skimage.io
import matplotlib.pyplot as plt
import math

np.random.seed(1)

img= plt.imread('mandrill.png')


# In[3]:



def gaussian_noise(img, std):
    
    noise = np.random.normal(img, std)
    img_noise = img+noise
    
    return np.clip(img_noise,0,1)


def salt_pepper_noise(img,probs):
    
    img_copy = img.copy()
    row, col = img_copy.shape
    
    
    num_pixsp= math.floor(probs * 0.5* row*col)
    
    #salt noise
    #indices for white-pixel
    coord_salt_x = np.random.randint(0, img.shape[0],num_pixsp)
    coord_salt_y = np.random.randint(0, img.shape[1],num_pixsp)
    
    for i in range(coord_salt_x.size):
        img_copy[coord_salt_x[i],coord_salt_y[i]]=1
        
    #pepper noise   
    #indices for black-pixel
    coord_pepper_x = np.random.randint(0, img.shape[0]-1,num_pixsp)
    coord_pepper_y = np.random.randint(0, img.shape[1]-1,num_pixsp)
    
    for i in range(coord_pepper_x.size):
        img_copy[coord_pepper_x[i],coord_pepper_y[i]]=0
        
    
    return img_copy
    


# In[4]:



std = np.std(img)

gaussian_img= gaussian_noise(img,std)

gaussian_img*=255
gaussian_img=gaussian_img.astype(np.uint8)
plt.imsave('gaussian_img.png',gaussian_img)

  
salt_pepper_img = salt_pepper_noise(img,0.004)

salt_pepper_img*=255
salt_pepper_img=salt_pepper_img.astype(np.uint8)
plt.imsave('salt_pepper_img.png',salt_pepper_img)


fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img)

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(gaussian_img)

ax3=fig.add_subplot(2,2,3)
ax3.imshow(gaussian_img)

