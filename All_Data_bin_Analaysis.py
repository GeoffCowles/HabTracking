
#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:02:56 2022

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

ncfile = '/home/lcabral4/WHOI/HAB3/HabTracking/float_output/box4.nc'


data = Dataset(ncfile)

y = data.variables['lat'][:]

x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]

from shapely.geometry import LineString, MultiLineString
from shapely.geometry import Polygon, Point

'''d_analysis.py'''
'''

fig = plt.figure(figsize=(13,10))

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-74,-1, 70, 20], ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)

lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.set_xticks([-75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10,-5, 0, 5, 10, 15, 20, 25], crs=ccrs.PlateCarree())
ax.set_yticks([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85], crs=ccrs.PlateCarree())


lat_formatter = cticker.LatitudeFormatter()


starting_longitude = []
ending_longitude = []
starting_time = []
ending_time = []
starting_lat = []
ending_lat = []
particle_number = []

for p in range(x.shape[0]):
#    if np.any(x[p,:] >=-20.4) and np.any(x[p,:] <=-20.2) and np.any(y[p,:] <=63.26) and np.any(y[p,:] >=62.5):


    plt.scatter(x[p,:], y[p,:], c=temp[p,:], s=0.1, marker = "o")
    plt.scatter(x[:,0], y[:,0])
c = plt.colorbar(shrink = .7855)
plt.clim(-2.5, 27.5)


plt.title('Release of 800 particles on 4/27/2015')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("All_4_27_2015.png")


#iceland_box.py


fig = plt.figure(figsize=(13,10))

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-74,-1, 70, 20], ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)

lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.set_xticks([-75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10,-5, 0, 5, 10, 15, 20, 25], crs=ccrs.PlateCarree())
ax.set_yticks([30, 35, 40, 45, 50, 55, 60, 65, 70, 75,80], crs=ccrs.PlateCarree())

lat_formatter = cticker.LatitudeFormatter()

current_directory = os.getcwd()

starting_longitude = []
ending_longitude = []
starting_time = []
ending_time = []
starting_lat = []
ending_lat = []
particle_number = []
seconds = []
polygon1 = Polygon([(-20.4, 63.2), (-20.4, 62.5), (-20.2, 62.5), (-20.2, 63.5)])
polygon2 = Polygon([(-64.6775, 60.576667), (-61.697222, 61.264444), (-51.024222,52.248889) ,(-54.5425,51.243056)])
for p in range(x.shape[0]):
#    seconds.append(time[p,:])
    for i, j in zip(x[p,:], y[p,:]):
        if Point(i,j).within(polygon2):
            plt.scatter(x[p,:], y[p,:],c = temp[p,:], s =0.1, marker = "o")
            #seconds.append(time[p,:])
            plt.scatter(x[p,0],y[p,0])

plt.colorbar(shrink = .7855)
plt.clim(-2.5, 27.5)


coord1 = [[-64.6775, 60.576667], [-61.697222, 61.264444], [-51.024222,52.248889] ,[-54.5425,51.243056]]
coord1.append(coord1[0])
xs, ys = zip(*coord1) #create lists of x and y values 
plt.plot(xs,ys)

# plot

#print(particle_number)

plt.title('4/27/15 800 Particle Release Point Within Polygon ')
plt.xlabel("Longitude")
plt.ylabel("Lattitude")
plt.savefig("4_27_15_release_Point_In_Polygon.png")

#particle_time.py

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import shapely.speedups

shapely.speedups.enable()

polygon1 = Polygon([(-64.6775, 60.576667), (-61.697222, 61.264444), (-51.024222,52.248889) ,(-54.5425,51.243056)])

particle = []
longitude = []
latitude = []
times = []
for p in range(x.shape[0]):
    for i, j, t in zip(x[p,:], y[p,:], time[p,:]):

        if (Point(i,j).within(polygon1)) == True:
            particle.append(p)
            times.append(t*1.15741e-5)



            break
dat = np.array([particle, times])
#print(particle,times)
dat = dat.T

np.savetxt('particle_time_4_27_2015.txt', dat ,header = 'particle number               times')#,delimiter = ',')
'''

#bin.py


data = np.loadtxt('particle_time_4_27_2015.txt')

#print(type(data[0,:]))

#plt.figure()
fig = plt.figure(figsize=(13,10))
CO = len(data[:,1])
bins = int(np.sqrt(CO))
#plt.yscale('log', nonpositive='clip')
y = data[:,1]
print(len(y))
x = data[:,0]
print(x)
print(y)
#print(bins)
#print("Time std is", np.std(y))
plt.title('Time Particle Reaches Polygon 4/27/2015 Release')
plt.ylabel('Number of Particles',fontsize=16)
plt.xlabel('Time (Days)',fontsize=16)
plt.hist(y, bins=bins)
plt.savefig('bin_4_27_2015.png')

'''lon_bin_.py'''


import shapely.speedups
#import geopandas as gpd

shapely.speedups.enable()

polygon1 = Polygon([(-64.6775, 60.576667), (-61.697222, 61.264444), (-51.024222,52.248889) ,(-54.5425,51.243056)])

particle = []
particle1 = []
longitude = []
latitude = []
all_lon = []
times = []
for p in range(x.shape[0]):
    all_lon.append(x[p,0])
    particle1.append(p)
    for i, j, t in zip(x[p,:], y[p,:], time[p,:]):

        if (Point(i,j).within(polygon1)) == True:
            particle.append(p)
#            times.append(t*1.15741e-5)
            longitude.append(x[p,0])
            break

#print(particle, longitude)
#for n, l, m, k in zip(particle, longitude, latitude, times):
#    y,u,i,p = np.meshgrid(n,l,m,k)
#    print(y,u,i,p)
dat = np.array([particle, longitude])
#print(particle,times)
dat = dat.T

np.savetxt('particle_lon_4_27_2015.txt', dat ,header = 'particle number               starting lon                  ')#,delimiter = ',')
dat = np.array([particle1, all_lon])
dat = dat.T
np.savetxt('all_lon_4_27_2015.txt', dat, header = 'starting lon')
            #m.append(t)
#            l, m = np.meshgrid(p,t).reshape(-1, 2)
#            print(l,m)
#np.savetxt('England_test.txt','a', dat ,header = 'particle number               times',delimiter = ',')
data = np.loadtxt('particle_lon_4_27_2015.txt')
data1 = np.loadtxt('all_lon_4_27_2015.txt')

#print(type(data[0,:]))
#print(data[:,0])
#print(data1[:,1])
#plt.figure()

fig = plt.figure(figsize=(13,10))
CO = len(data1[:,1])
bins = int(np.sqrt(CO))
#plt.yscale('log', nonpositive='clip')
y = data[:,1]
#print(len(y))
x = data[:,0]
plt.title('Starting Longitude 4/27/2015 Release For Successful polygon Entrance')
plt.ylabel('Number of Particles',fontsize=16)
plt.xlabel('Longitude',fontsize=16)
plt.hist(y, bins=bins)
plt.savefig('starting_lon_4_27_2015.png')


