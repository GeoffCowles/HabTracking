#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:49:49 2022

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


from netCDF4 import Dataset
ncfile = '/home/lcabral4/WHOI/HabTracking/float_output/Gulf_Of_St_Lawrence/Gulf_Of_St_Lawrence_1_1_2015.nc'
data = Dataset(ncfile)
y = data.variables['lat'][:]
x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]

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


particle = []
t = []
initial_lon = []
initial_lat = []
final_lon = []
final_lat = []
#time = []
for p in range(x.shape[0]):
    if np.any(x[p,:] >=-70) and np.any(x[p,:] <=-65) and np.any(y[p,:] <=45) and np.any(y[p,:] >=40) and np.any(time[p,0] < 5184000.0):
        
        plt.scatter(x[p,:], y[p,:], c=temp[p,:], s=0.0001, marker = "o")
        plt.scatter(x[:,0], y[:,0]) 
        particle.append(p)
        t.append(np.mean(temp[p,:]))
        #initial_lon.append(x[0])
        initial_lon.append(x[p,0])
        initial_lat.append(y[p,0])
        final_lon.append(x[p, -1])
        final_lat.append(y[p,-1])
print(np.size(time[p,:]))
print(np.size(x[p,:]))
print(time[p,0])
print(x.shape)
print(time.shape, 'time')
print(time[0,0], time[0, -1])
print(time[-1, 0], time[-1, -1])
#print(time[0, -1],'last' )
print(time[-1, 0])
print(time[-1, -1], 'last particle')

print('particle number ------------------------------')
print(particle)
print('temperature ----------------------------------')
print(t)
print('initial lon ----------------------------------')
print(initial_lon)
print('initial lat ----------------------------------')
print(initial_lat)
print('final lon ------------------------------------')
print(final_lon)
print('final lat ------------------------------------')
print(final_lat)




c = plt.colorbar(shrink = .7855)
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



plt.title('Greenland')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("box.png")    

for p in range(x.shape[0]):
    if np.any(x[p,:] >=-70) and np.any(x[p,:] <=-65) and np.any(y[p,:] <=45) and np.any(y[p,:] >=40) and np.any(time[p,0] > 5184000.0):
        
        plt.scatter(x[p,:], y[p,:], c=temp[p,:], s=0.0001, marker = "o")
        plt.scatter(x[:,0], y[:,0]) 

c = plt.colorbar(shrink = .7855)
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



plt.title('Greenland')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("box1.png")    

