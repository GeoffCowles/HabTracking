#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:36:10 2022

@author: lcabral4
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:58:02 2022

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
import geopandas as gpd

shapely.speedups.enable()
ncfile = '/home/lcabral4/WHOI/WHOI/float_output/Scotia.nc'

data = Dataset(ncfile)

y = data.variables['lat'][:]
x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]
polygon1 = Polygon([(-55, 45), (-55, 40), (-50, 40), (-50, 45)])
particle = []
longitude = []
latitude = []
times = []
for p in range(x.shape[0]):
    for i, j, t in zip(x[p,:], y[p,:], time[p,:]):

        if (Point(i,j).within(polygon1)) == True:
            particle.append(p)
            times.append(t*1.15741e-5)
            

#            particle.append(p)
#            longitude.append(i)
#            latitude.append(y)
#            times.append(t)
#            print(p,t*1.15741e-5)
#            dat = np.array([p, t])

#            dat = dat.T
#            np.savetxt('England_test.txt', dat ,header = 'particle number               times',delimiter = ',')

            break

print(particle, times)

#for n, l, m, k in zip(particle, longitude, latitude, times):
#    y,u,i,p = np.meshgrid(n,l,m,k)
#    print(y,u,i,p)
dat = np.array([particle, times])
#print(particle,times)
dat = dat.T

np.savetxt('particle_time.txt', dat ,header = 'particle number               times')#,delimiter = ',')
            
            #m.append(t)
#            l, m = np.meshgrid(p,t).reshape(-1, 2)
#            print(l,m)
#np.savetxt('England_test.txt','a', dat ,header = 'particle number               times',delimiter = ',')