#!/usr/bin/env python3

from astropy.io import fits
import os
import numpy

path="../focus1/"
lista=[f for f in os.listdir(path) if ".fits" in f]

for f_file in lista:
  hdu=fits.open(path+f_file)
  hdr = data = hdu[0].header 
  focus = hdr["FOCUS"]
  data = hdu[0].data
  
  edge_rows = int(data.shape[0] * 0.1)
  edge_cols = int(data.shape[1] * 0.1)

  data = data[edge_rows:-edge_rows, edge_cols:-edge_cols]

  mean = numpy.mean(data)
  rms = numpy.std(data)

  print(f_file, focus , rms)





