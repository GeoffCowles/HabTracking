#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 23:20:04 2022

@author: lcabral4
"""

from parcels import FieldSet, ParticleSet, JITParticle, AdvectionRK4, ErrorCode, Variable
from datetime import timedelta, datetime
import numpy as np
import random
import netCDF4
import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import cartopy.crs as ccrs 
#from mpl_toolkits.basemap import Basemap
from cartopy import config
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker 
from parcels import plotting
import matplotlib.pylab as pl
import cartopy.feature as cfeature
#from x import *
from matplotlib.colors import ListedColormap
#from Southern_Greenland import *

from mpl_toolkits.axes_grid1 import make_axes_locatable
import os

from netCDF4 import Dataset

ncfile = '/home/lcabral4/WHOI/WHOI/float_output/Scotia.nc'

data = Dataset(ncfile)

y = data.variables['lat'][:]
x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]

starting_longitude = []
ending_longitude = []
starting_time = []
ending_time = []
starting_lat = []
ending_lat = []
particle_number = []


#print(longitude)
#print(starting_time)

fig = plt.figure(figsize=(13,10))

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-74,-1, 70, 20], ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)

lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.set_xticks([-75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10,-5, 0], crs=ccrs.PlateCarree())
ax.set_yticks([30, 35, 40, 45, 50, 55, 60, 65, 70, 75], crs=ccrs.PlateCarree())

lat_formatter = cticker.LatitudeFormatter()

current_directory = os.getcwd()


for p in range(x.shape[0]):
    if np.any(time[p,0] == 0):

        
        plt.scatter(x[p,:], y[p,:], c=temp[p,:], s=0.0001, marker = "o")
        plt.scatter(x[:,0], y[:,0]) 
plt.colorbar(shrink = .7855)
plt.clim(-2.5, 27.5) 

#print(temp, 'temp')
coord = [[-70,40], [-70,45],[-65,45], [-65,40]]
#poly = Polygon(((-70, 40), (-70, 45), (-65, 45), (-65, 40)))
#print(poly)
#poly = MultiPoint(coords).convex_hull
coord.append(coord[0])
xs, ys = zip(*coord) #create lists of x and y values 
plt.plot(xs,ys) 


# plot

print(particle_number)

plt.title('Greenland')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("canada_box.png")  