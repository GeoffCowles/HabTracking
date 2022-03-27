#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:55:10 2022

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

ncfile = '/home/lcabral4/WHOI/HAB3/HabTracking/float_output/England1.nc'

data = Dataset(ncfile)

y = data.variables['lat'][:]
x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]


particle_start_time = []
for p in range(x.shape[0]):
    particle_start_time.append(time[p,0])
    
dat = np.array([particle_start_time])

dat = dat.T

np.savetxt('particle_time.txt', dat ,header = 'particle number',delimiter = ',')