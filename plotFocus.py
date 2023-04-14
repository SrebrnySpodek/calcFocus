#!/usr/bin/env python3

"""A script to calculate the focus position of maximum sharpness for a given FITS files, and plot the result.  

Usage:
    plotFocus.py <fits_path> [options]

Arguments:
    <fits_path>      Required. The path to the FITS files directory or a list with FITS files.

Options:
    focus_keyword=<keyword>  FIST file header keyword to retrive focus encoder position. Default: "FOCUS".
    focus_list=<values>      A list of focus values to use for the calculation. If None, the focus values will be extracted from the FITS header. Defaults to None.
    crop=<pixels>            The amount of pixels to crop from the edges of each image. Defaults to 10.
    method=<method>          The method to use for calculating sharpness. Can be "rms", "rms_quad". Defaults to "rms_quad".

Returns:
    FOCUS: focus encoder value for maximum sharpness
    POLY COEFF: coefficients for the polynomial fit used to calculate sharpness.
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

    txt=f"FOCUS: {max_sharpness_focus}\nPOLY COEFF: {coef}"
    print(txt)

    x = numpy.linspace(min(focus_list_ret), max(focus_list_ret), 100)
    if len(coef)>3:
        y = coef[0]* x**4 + coef[1]* x**3 + coef[2]*x**2 +  coef[3]*x + coef[4]
    elif len(coef)>1:
        y = coef[0]* x**2 + coef[1]*x + coef[2]

    plt.plot(x,y)
    plt.plot(focus_list_ret,sharpness_list_ret,"ro")
    plt.axvline(x=max_sharpness_focus,color="red",alpha=1)
    plt.gca().invert_yaxis()
    plt.xlabel("focus encoder position")
    plt.ylabel("sharpness")    
    plt.show()   


if __name__ == "__main__":
    main()

