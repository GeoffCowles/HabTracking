#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:17:39 2022

@author: lcabral4
"""
# Define the new Kernel that mimics RW
def VerticalMovement(particle, fieldset, time):

    # set particle salinity at new depth for output
    particle.salt =  fieldset.salt[time, particle.depth, particle.lat, particle.lon]
    particle.temp = fieldset.temp[time, particle.depth, particle.lat, particle.lon]


    # can code vertical diffusivity here with random walk
    # ocean parcels has some random walk functions as well
    # have particle.dt for time step, particle.depth for depth

    # for now, lock to depth (surface)
#    particle.depth = 0

def OutOfBounds ( particle , fieldset , time ):

    particle.delete ()

from parcels import FieldSet, ParticleSet, JITParticle, AdvectionRK4, ErrorCode, Variable
from datetime import timedelta, datetime
import numpy as np
import random
import netCDF4
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
from England import *


# Load the HYCOM Analysis data in the Gulf of Maine
# The paths/datafiles should be read in from a control file
filenames = {'U': "./hycom_data/HAB4*",
             'V': "./hycom_data/HAB4*",
             'salt': "./hycom_data/HAB4*",
             'temp': "./hycom_data/HAB4*"}
variables = {'U': 'water_u',
             'V': 'water_v',
             'salt': 'salinity',
             'temp': 'water_temp'}
dimensions = {'lat': 'lat', 'lon': 'lon', 'time': 'time'}
fieldset = FieldSet.from_netcdf(filenames, variables, dimensions,allow_time_extrapolation = False)
fieldset.mindepth = fieldset.U.depth[0]  # uppermost layer in the hydrodynamic data



#npart=2
# print the domain boundaries to the screen
print("domain boundaries")
print(fieldset.U.lon[0],fieldset.U.lon[-1],fieldset.U.lat[0],fieldset.U.lat[-1])


# Define a new Particle type including extra Variables
#class ArgoParticle(JITParticle):
#    # Phase of cycle: init_descend=0, drift=1, profile_descend=2, profile_ascend=3, transmit=4
#    cycle_phase = Variable('cycle_phase', dtype=np.int32, initial=0.)
#    cycle_age = Variable('cycle_age', dtype=np.float32, initial=0.)
#    drift_age = Variable('drift_age', dtype=np.float32, initial=0.)
#    S = Variable('S', dtype=np.float32, initial=np.nan)  # store salinity

# Define a new Particle type including extra Variables
class HabParticle(JITParticle):
    # Phase of cycle: init_descend=0, drift=1, profile_descend=2, profile_ascend=3, transmit=4
    salt = Variable('salt', dtype=np.float32, initial=np.nan)  # store salinity
    temp = Variable('temp', dtype=np.float32, initial=np.nan)  # store water temperature

# Initiate two Isopycnal Floats with staggered starts and different programmed drift densities initiated from 
# different depths and horizontal locations.  These variables here (lon, lat, time, float_density) should
# be read in from a control file.


x = []
y = []

lonmin
lonmax
latmin
latmax
n
days
year
month
day
outputminutes
dtminutes
npart = n  # number of particles to be released
for i in range(n):
    lon = lonmin + random.uniform(0, 1)*(lonmax-lonmin)
    x.append(lon)
    lat = latmin + random.uniform(0, 1)*(latmax-latmin)
    y.append(lat)
time = datetime(year,month,day)

pset = ParticleSet(fieldset=fieldset, pclass=HabParticle, lon=x, lat=y, time=time)


fig = plt.figure(figsize=(13,10))
kernels = VerticalMovement + pset.Kernel(AdvectionRK4)
output_file = pset.ParticleFile(name="float_output/box1", outputdt=timedelta(minutes=outputminutes))
pset.execute(kernels, runtime=timedelta(days=days), dt=timedelta(minutes=dtminutes), output_file=output_file, recovery={ErrorCode.ErrorOutOfBounds: OutOfBounds})

#pset.execute(kernels, runtime=timedelta(days=600.), dt=timedelta(minutes=-30), output_file=output_file, recovery={ErrorCode.ErrorOutOfBounds: OutOfBounds})

output_file.export()  # export the trajectory data to a netcdf file

nc = netCDF4.Dataset("float_output/box1.nc")

x = nc.variables["lon"][:].squeeze()
time = nc.variables["time"][:].squeeze()

y = nc.variables["lat"][:].squeeze()
z = nc.variables["z"][:].squeeze()
salt = nc.variables["salt"][:].squeeze()
temp = nc.variables["temp"][:].squeeze()
nc.close()
