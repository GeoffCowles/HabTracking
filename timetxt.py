

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

ncfile = '/home/lcabral4/WHOI/HAB3/HabTracking/float_output/Final.nc'



data = Dataset(ncfile)

y = data.variables['lat'][:]

x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]

from shapely.geometry import LineString, MultiLineString
from shapely.geometry import Polygon, Point

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import shapely.speedups

shapely.speedups.enable()

polygon1 = Polygon([(-65, 60), (-63, 65), (-50,55) ,(-55,50)])
particle = []
longitude = []
latitude = []
times = []
for p in range(x.shape[0]):
    for i, j, t in zip(x[p,:], y[p,:], time[p,:]):
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import shapely.speedups

shapely.speedups.enable()

polygon1 = Polygon([(-65, 60), (-63, 65), (-50,55) ,(-55,50)])
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

np.savetxt('particle_time_7_2_2014.txt', dat ,header = 'particle number               times')#,delimiter = ',')
        if (Point(i,j).within(polygon1)) == True and time[p,0] == 4.32*10**4:
            particle.append(p)
            times.append(t*1.15741e-5)



            break
dat = np.array([particle, times])
#print(particle,times)
dat = dat.T

np.savetxt('particle_time_7_2_2014.txt', dat ,header = 'particle number               times')#,delimiter = ',')