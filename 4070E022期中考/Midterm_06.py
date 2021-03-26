 # -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from pylab import *
from PCV.tools import imtools

im = array(Image.open('../data/empire.jpg').convert('L'))

#print (int(im.min()), int(im.max()))

im2 = 255.0 * (im/255.0)**2  # squared
#print (int(im2.min()), int(im2.max()))

im3 = 255 - im  # invert image
#print (int(im3.min()), int(im3.max()))

figure()
gray()
subplot(2, 2, 1)
imshow(im2)
axis('off')
title(r'$f(x)=255(\frac{x}{255})^2$')
#hist(im.flatten(), 128)

subplot(2, 2, 2)
imshow(im3)
axis('off')
title(r'$f(x)=255-x$')
#hist(im.flatten(), 128)

subplot(2, 2, 3)
axis('off')
#hist(im.flatten(), 128, cumulative=True, normed=True)
hist(im.flatten(), 128)

subplot(2, 2, 4)
axis('off')
#hist(im2.flatten(), 128, cumulative=True, normed=True)
hist(im2.flatten(), 128)

show()