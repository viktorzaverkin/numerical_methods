#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:41:56 2020

@author: April Cooper 
"""
#parameters following D. Foss Smith, Jr. and John Overend,
#Spectrochim. Acta 28A 471 (1972)

from math import atan
def pot_water(dist1,dist2,angle):
    k11=4.2294
    k12=-0.0948
    k13=0.3752
    k33=0.3589
    k111=-10.1664
    k112=-0.4044
    k113=-0.3809
    k123=-0.5491
    k133=-0.4481
    k333=-0.2039
    k1111=18.3497
    k1112= 1.1283
    k1113=-3.6896
    k1122= 1.2990
    k1123=-4.1278
    k1133=-0.0163
    k1233=-0.0072
    k1333= 0.0546
    k3333= 0.0482
    
    r1=dist1-0.9572
    r2=dist2-0.9572
    r3=(angle-104.52)/180.0*4.0*atan(1.0) # r3=angle in radians
        
    energy=(k11*(r1**2+r2**2) + k12*r1*r2 + k13*(r1*r3+r2*r3) + k33*r3**2 + 
      k111*(r1**3+r2**3) + k112*(r1**2*r2+r1*r2**2) + 
      k113*(r1**2+r2**2)*r3 + k123*r1*r2*r3 + k133*(r1+r2)*r3**2 + 
      k333*r3**3 + k1111*(r1**4+r2**4) + k1112*r1*r2*(r1**2+r2**2) + 
      k1113*r3*(r1**3+r2**3) + k1122*r1**2*r2**2 + 
      k1123*(r1**2*r2+r1*r2**2)*r3 + k1133*(r1**2+r2**2)*r3**2 + 
      k1233*r1*r2*r3**2 + k1333*(r1+r2)*r3**3 + k3333*r3**4)
    energy=energy*602.0 # convert Joule to kJ/mol
    
    return energy




