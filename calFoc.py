#!/usr/bin/env python3

"""A script to calculate the focus position of maximum sharpness for a given FITS files.  

Usage:
    calFocus.py <fits_path> [options]

Arguments:
    <fits_path>      Required. The path to the FITS files directory or a list with FITS files.

Options:
    focus_keyword=<keyword>  FIST file header keyword to retrive focus encoder position. Default: "FOCUS".
    focus_list=<values>      A list of focus values to use for the calculation. If None, the focus values will be extracted from the FITS header. Defaults to None.
    crop=<pixels>            The amount of pixels to crop from the edges of each image. Defaults to 10.
    method=<method>          The method to use for calculating sharpness. Can be "rms", "rms_quad". Defaults to "rms_quad".

Returns: focus encoder value for maximum sharpness
"""  

import os
import sys

import numpy
import matplotlib.pyplot as plt

from calcFocus import calc_focus as cf

def main():
    kwargs = {}
    args = []
    for arg in sys.argv[1:]:
        if '=' in arg:
            key, value = arg.split('=', 1)
            kwargs[key] = value
        else:
            args.append(arg)   
    
    max_sharpness_focus, calc_metadata = cf.calculate(*args,**kwargs)
    #print(help(cf.calculate))

    coef = calc_metadata["poly_coef"]
    focus_list_ret = calc_metadata["focus_values"] 
    sharpness_list_ret = calc_metadata["sharpness_values"]

    txt=f"{max_sharpness_focus}"
    print(txt)


if __name__ == "__main__":
    main()

