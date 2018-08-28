import cv2
import matplotlib.pyplot as plt 

def fixColorSpace(im):
    nDims = len(im.shape)
    if nDims == 3:
        imOut = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    elif nDims == 2: 
        imOut = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
    
    return imOut

def imshow3(im1, im2, im3, scale = 1):
    plt.figure(figsize=(15 * scale, 15 *scale)); 
    
    plt.subplot(131); 
    plt.imshow(fixColorSpace(im1)); 
    plt.axis('off'); 
    
    plt.subplot(132); 
    plt.imshow(fixColorSpace(im2)); 
    plt.axis('off'); 
    
    plt.subplot(133); 
    plt.imshow(fixColorSpace(im3))
    plt.axis('off');

    plt.show()

def imshow2(im1, im2, scale = 1):
    
    imOut1 = fixColorSpace(im1)
    imOut2 = fixColorSpace(im2)

    plt.figure(figsize=(15 * scale, 15 * scale))
    
    plt.subplot(121)
    plt.imshow(imOut1)
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(imOut2)
    plt.axis('off')

    plt.show()

def imshow(im, scale = 1):
    imOut = fixColorSpace(im) 
    plt.figure(figsize=(15 * scale, 15 * scale))
    plt.imshow(imOut)
    plt.axis('off')
    plt.show()
