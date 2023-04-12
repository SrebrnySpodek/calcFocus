#!/usr/bin/env python3

"""
chcemy zrobic z tego package, z mozliwoscia wywolania cli

opcja1:
w wywolaniu chcemy *arg - jezeli jest tylko jeden arg to moze to byc sciezka do katalogu w ktorym sa fliki fits
i wtedy bierze je wszystkie w tym katalogu. Jezeli jest wiecej, to kazdy argument musi byc plikiem fits. 

opcja2: tylko jeden arg : sciezka do katalogu
jak chcemy podac liste likow fits, to podajemy jako kwarg lista_plikow

kwargs:
focus_keyword = "FOCUS"
focus_pos_list 
method = "rms"
crop = 10    (jako procent obrazka)

zwracenie bledow - katalog nie istnieje, pliki nie istnieja, nie da sie wczytac plikow fits, 
lista focus_pos innej dlugosci niz liczba plikow, nie ma methody 'method'

"""

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





