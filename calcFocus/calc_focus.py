#!/usr/bin/env python3

"""
chcemy zrobic z tego package, z mozliwoscia wywolania cli

opcja1:
w wywolaniu chcemy *arg - jezeli jest tylko jeden arg to moze to byc sciezka do katalogu w ktorym sa fliki fits
i wtedy bierze je wszystkie w tym katalogu. Jezeli jest wiecej, to kazdy argument musi byc plikiem fits. 

opcja2: tylko jeden arg : sciezka do katalogu
jak chcemy podac liste likow fits, to podajemy jako kwarg lista_plikow

kwargs:

zwracenie bledow - katalog nie istnieje, pliki nie istnieja, nie da sie wczytac plikow fits, 
lista focus_pos innej dlugosci niz liczba plikow, nie ma methody 'method'

"""

from astropy.io import fits
import os
import numpy

METHODS = ["rms", ]


def calculate(path, focus_keyword="FOCUS", focus_list=None, crop=10, method="rms"):
    """
    Function to find optimal focus value

    :param path:
    :param focus_keyword:
    :param focus_list:
    :param crop:
    :param method:
    :return:
    """

    if method not in METHODS:
        raise ValueError(f"Invalid method {method}")
    if isinstance(path, list):
        if not all(os.path.isfile(file) for file in path):
            raise ValueError(f"Invalid list with fits {path}")
        lista = path
    else:
        if os.path.isdir(path):
            lista = [os.path.join(path, f) for f in os.listdir(path) if ".fits" in f]
        else:
            raise ValueError(f"{path} is not valid dir")

    if method == "rms":

        focus_list_ret = []
        for my_iter, f_file in enumerate(lista):
          hdu = fits.open(f_file)
          hdr = hdu[0].header
          if focus_list is None:
            focus = hdr[focus_keyword]
          else:
            focus = focus_list[my_iter]
          data = hdu[0].data

          edge_rows = int(data.shape[0] * crop/100.)
          edge_cols = int(data.shape[1] * crop/100.)

          data = data[edge_rows:-edge_rows, edge_cols:-edge_cols]

          mean = numpy.mean(data)
          rms = numpy.std(data)
          focus_list_ret.append(focus)
          hdu.close()
    return focus_list_ret
    #print(f_file, focus , rms)





