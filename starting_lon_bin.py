#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:36:28 2022

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

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import shapely.speedups
#import geopandas as gpd

shapely.speedups.enable()
#ncfile = '/home/lcabral4/WHOI/WHOI/float_output/Scotia.nc'
ncfile = '/home/lcabral4/WHOI/HAB3/HabTracking/float_output/box1.nc'
#ncfile = '/home/lcabral4/WHOI/WHOI/float_output/Scotia.nc'
data = Dataset(ncfile)

y = data.variables['lat'][:]
x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]
#polygon1 = Polygon([(-55, 45), (-55, 40), (-50, 40), (-50, 45)])
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



#            particle.append(p)
#            longitude.append(i)
#            latitude.append(y)
#            times.append(t)
#            print(p,t*1.15741e-5)
#            dat = np.array([p, t])

#            dat = dat.T
#            np.savetxt('England_test.txt', dat ,header = 'particle number               times',delimiter = ',')

            break

print(particle, longitude)
#for n, l, m, k in zip(particle, longitude, latitude, times):
#    y,u,i,p = np.meshgrid(n,l,m,k)
#    print(y,u,i,p)
dat = np.array([particle, longitude])
#print(particle,times)
dat = dat.T

np.savetxt('particle_lon.txt', dat ,header = 'particle number               starting lon                  ')#,delimiter = ',')
dat = np.array([particle1, all_lon])
dat = dat.T
np.savetxt('all_lon.txt', dat, header = 'starting lon')
            #m.append(t)
#            l, m = np.meshgrid(p,t).reshape(-1, 2)
#            print(l,m)
#np.savetxt('England_test.txt','a', dat ,header = 'particle number               times',delimiter = ',')
data = np.loadtxt('particle_lon.txt')
data1 = np.loadtxt('all_lon.txt')

#print(type(data[0,:]))
print(data[:,0])
print(data1[:,1])
#plt.figure()

plt.figure(1)
CO = len(data1[:,1])
bins = int(np.sqrt(CO))
#plt.yscale('log', nonpositive='clip')
y = data[:,1]
print(len(y))
x = data[:,0]
#print(x)
#print(y)
#print(bins)
#print("Time std is", np.std(y))
plt.title('Starting Longitude That Enters Polygon')
plt.ylabel('Number of Particles',fontsize=16)
plt.xlabel('Longitude',fontsize=16)
plt.hist(y, bins=bins)
plt.savefig('starting_lon.png')