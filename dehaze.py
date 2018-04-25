import cv2
import numpy as np
import get_dark_channel
import get_atmosphere
import matplotlib.pyplot as plt
import UnderwaterColorCorrection
import guidedfilter


def dehaze(im,omega,win_size):    
    m,n=im.shape[:2]
    
    img = im.copy()
    
    #img[:,:,2]=1-img[:,:,2]
    img=1-img
    
    trans = 1.06 - img 
    alpha = im.mean()/1.3
    trans = trans + alpha
    
    dark_channel = get_dark_channel.get_dark_channel(img,win_size)
    atmosphere , test = get_atmosphere.get_stmosphere(img,dark_channel)
    print (atmosphere)
    
    ab = (img - atmosphere) / trans + atmosphere
    ab[ab>1]=1
    ab[ab<0]=0
    result = (1-ab)*255
    return result
'''
im=cv2.imread('b.jpg')
im=np.float64(im)
im=im/255
omega, win_size = 10 ,15

result=dehaze(im,omega,win_size)

result = np.uint8(result)

#result = result * 255

#plt.imshow(result)
cv2.imwrite('rr.jpg',result)
########################
'''
