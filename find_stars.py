#!/usr/bin/env python3

from astropy.io import fits
from astropy.convolution import Gaussian2DKernel
from astropy.convolution import convolve
import os
import numpy

from scipy.signal import convolve2d
from scipy.signal import find_peaks
from scipy.ndimage.filters import maximum_filter

path="../focus2/"
lista=[f for f in os.listdir(path) if ".fits" in f]

lista=lista[5:6]

for f_file in lista:
  hdu=fits.open(path+f_file)
  hdr = data = hdu[0].header 
  data = hdu[0].data

  mean = numpy.median(data)
  #rms = numpy.std(data)
  rms=numpy.quantile(data, 0.68)-numpy.quantile(data, 0.32)
  rms=rms/2.
  print(rms)

  maska1=data>(mean+5*rms)
  maska2=data<30000

  #kernel = [[1,2,1],[2,4,2],[1,2,1]]
  #data2 = convolve2d(data, kernel, mode='same')

  kernel = Gaussian2DKernel(5, 5,x_size=41,y_size=41)
  data2 = convolve(data, kernel)



  maska0 = (data2 == maximum_filter(data2, 10))
  maska3=numpy.logical_and(maska1, maska2)  
  maska=numpy.logical_and(maska0, maska3) 

  max_coo = numpy.argwhere(maska)

txt="\n \n"
for coo in max_coo:
  txt = txt + "1 "+str(coo[1])+" "+str(coo[0])+"\n"


with open("result.coo", mode='w') as plik: plik.write(txt)


hdu2 = fits.PrimaryHDU(data)
hdu2.header = hdr
hdu2.writeto('result.fits',overwrite=True)




# Convolve the image with the kernel
#convolved_image = convolve(image, kernel)




