#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:05:51 2020

@author: April Cooper
"""
from PES_water import pot_water
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

def plot_PES():
    #Computing the PES for a grid of points (distance,angle)
    distances = np.arange(0.7,1.55,0.05)
    angles = np.arange(90,185,5)

    pes=np.zeros((len(distances),len(angles))) # 17x19 Matrix

    for dist in range(len(distances)):
        for ang in range(len(angles)):
            pes[dist,ang]=pot_water(distances[dist],distances[dist],angles[ang])

    #Plotting the results
    angles, distances = np.meshgrid(angles, distances)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Bond distance ($\AA$)')
    ax.set_ylabel('Bond angle ($^\circ$)')
    ax.set_zlabel('Potential energy (kJ/mol)')

    ax.plot_surface(distances, angles, pes, cmap="viridis",
                      lw=0.5, rstride=1, cstride=1, alpha=0.75)

    ax.contour(distances, angles, pes, 100, lw=3, cmap="viridis",
                     linestyles="solid", offset=-800)
    ax.contour(distances, angles, pes, 100, lw=3, colors="k", linestyless="solid")

    plt.show()
    #plt.savefig('pes_water_plt.pdf')
    
    