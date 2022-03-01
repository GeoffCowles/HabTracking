#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:01:12 2022

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
from Greenland_1_1_2015 import *


# Load the HYCOM Analysis data in the Gulf of Maine
# The paths/datafiles should be read in from a control file
filenames = {'U': "./hycom_data/HAB2*",
             'V': "./hycom_data/HAB2*",
             'salt': "./hycom_data/HAB2*",
             'temp': "./hycom_data/HAB2*"}
variables = {'U': 'water_u',
             'V': 'water_v',
             'salt': 'salinity',
             'temp': 'water_temp'}
dimensions = {'lat': 'lat', 'lon': 'lon', 'time': 'time'}
fieldset = FieldSet.from_netcdf(filenames, variables, dimensions,allow_time_extrapolation = True)
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

#%matplotlib inline

#lon = -70.20
#lat = 42.95
#depth = 0.

# pset = ParticleSet.from_list(fieldset=fieldset,
#                             pclass=HabParticle,
#                             lon=[-70.20,-70.18],
#                             lat=[42.85,43.0],
#                             depth=[0.,0.],
#                             time=[datetime(2015, 1, 1),
#                             datetime(2015,1,1)])

#baffin
line_start 
line_end 

#cross-gom
line_start 
line_end
Np 

days
year
month
pset = ParticleSet.from_line(fieldset=fieldset,
                            pclass=HabParticle,
                            start=line_start,
                            finish=line_end,
                            size=Np,
                            time=[datetime(year, month, day)],
                            repeatdt=5184000)
                            

x = []
y = []
m = []

#lonmin 
#lonmax 
#latmin 
#latmax 
#n
days
year
month
day
outputminutes
dtminutes

kernels = VerticalMovement + pset.Kernel(AdvectionRK4) 
output_file = pset.ParticleFile(name="float_output/Line_Greenland/1_1_2015_Line_Greenland", outputdt=timedelta(minutes=outputminutes))

# combine Argo vertical movement kernel with built-in Advection kernel
#kernels = VerticalMovement + pset.Kernel(AdvectionRK4)

# Create a ParticleFile object to store the output
# outputdt might be read in from a control file
#output_file = pset.ParticleFile(name="case3", outputdt=timedelta(minutes=240))

# dt and runtime might be read in from a control file
pset.execute(kernels, runtime=timedelta(days=days), dt=timedelta(minutes=dtminutes), 
           output_file=output_file, recovery={ErrorCode.ErrorOutOfBounds: OutOfBounds})
pset.show(field=fieldset.U)
output_file.export()

#pset.execute(kernels, runtime=timedelta(days=days), dt=timedelta(minutes=dtminutes), output_file=output_file, recovery={ErrorCode.ErrorOutOfBounds: OutOfBounds})
    
#pset.execute(kernels, runtime=timedelta(days=600.), dt=timedelta(minutes=-30), output_file=output_file, recovery={ErrorCode.ErrorOutOfBounds: OutOfBounds})

#output_file.export()  # export the trajectory data to a netcdf file

nc = netCDF4.Dataset("float_output/Line_Greenland/1_1_2015_Line_Greenland.nc")

x = nc.variables["lon"][:].squeeze()
time = nc.variables["time"][:].squeeze()
y = nc.variables["lat"][:].squeeze()
z = nc.variables["z"][:].squeeze()
salt = nc.variables["salt"][:].squeeze()
temp = nc.variables["temp"][:].squeeze()
nc.close()
fig = plt.figure(figsize=(13,10))
for p in range(x.shape[0]):
    cb = plt.scatter(x[p,:], y[p,:], c=temp[p,:], s=0.01, marker = "o")
    plt.scatter(x[:,0], y[:,0], s= 20, marker = 's') 
plt.title('Greenland Temperature')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("Greenland_1_1_2015.png")
    
plt.show()


fig = plt.figure(figsize=(13,10))
#    for p in range(x.shape[0]):
#        cb = plt.scatter(x[p], y[p], c=temp[p], s=20, marker = "o")
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-74,-1, 70, 20], ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
#x = np.linspace(-65, -75)
#y = np.linspace(35, 45)
#plt.title('Temperature Variable')
#ax.set_xlabel("Longitude")
#ax.set_ylabel("Latitude")
#ax.set_xticks(np.arange(-80,-65,100), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.set_xticks([-75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25, -20, -15, -10,-5, 0], crs=ccrs.PlateCarree())
ax.set_yticks([30, 35, 40, 45, 50, 55, 60, 65, 70, 75], crs=ccrs.PlateCarree())
#ax.set_yticks(np.arange(40,50,20), crs=ccrs.PlateCarree())
lat_formatter = cticker.LatitudeFormatter()
#ax.yaxis.set_major_formatter(lat_formatter) 
#lon, lat = np.meshgrid(x, y)
for p in range(x.shape[0]):
    cb = plt.scatter(x[p,:], y[p,:], c=temp[p,:], s=0.0001, marker = "o")
    plt.scatter(x[:,0], y[:,0]) 
print(temp, 'temp')



# plot




plt.title('Greenland')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("Greenland_1_1_2015_temp.png")    
plt.show()
