# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:10:51 2020

@author: marco
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, pi, cos, imag, real, sqrt





#### Diskrete Fouriertransformation 

def DF(X):
    N = len(X)
    x = [2*pi*l/N for l in range(N)]
    fourier = []
    for k in range(N):
        coef = []
        for l in range(N):
            coef.append(X[l]*complex(cos(k*x[l]),-sin(k*x[l])))
        a = 1/N*sum(coef)
        fourier.append(a)
    return fourier
        

