
# Define the new Kernel that mimics RW
def VerticalMovement(particle, fieldset, time):
    
    # set particle salinity at new depth for output
    particle.salt =  fieldset.salt[time, particle.depth, particle.lat, particle.lon]

    # can code vertical diffusivity here with random walk
    # ocean parcels has some random walk functions as well
    # have particle.dt for time step, particle.depth for depth
    
    # for now, lock to depth (surface)
    particle.depth = 0

from parcels import FieldSet, ParticleSet, JITParticle, AdvectionRK4, ErrorCode, Variable
from datetime import timedelta, datetime
import numpy as np
import os


# Load the HYCOM Analysis data in the Gulf of Maine
# The paths/datafiles should be read in from a control file
filenames = {'U': "./hycom_data/*.nc",
             'V': "./hycom_data/*.nc",
             'salt': "./hycom_data/*.nc",
             'temp': "./hycom_data/*.nc"}
variables = {'U': 'water_u',
             'V': 'water_v',
             'salt': 'salinity',
             'temp': 'water_temp'}
dimensions = {'lat': 'lat', 'lon': 'lon', 'depth' : 'depth' , 'time': 'time'}
fieldset = FieldSet.from_netcdf(filenames, variables, dimensions)#,allow_time_extrapolation = True)
fieldset.mindepth = fieldset.U.depth[0]  # uppermost layer in the hydrodynamic data

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
pset = ParticleSet.from_list(fieldset=fieldset,
                            pclass=HabParticle,
                            lon=[-70,-70],
                            lat=[43.,43.],
                            depth=[0,0],
                            time=[datetime(2016, 1, 1),
                            datetime(2016,1,2,0,0,0)])


# combine Argo vertical movement kernel with built-in Advection kernel
kernels = VerticalMovement + pset.Kernel(AdvectionRK4)
#kernels = IsoPycnalVerticalMovement + pset.Kernel(AdvectionRK4)

# Create a ParticleFile object to store the output
# outputdt might be read in from a control file
output_file = pset.ParticleFile(name="float_output/isopycnal_float", outputdt=timedelta(minutes=30))

# Now execute the kernels for 30 days, saving data every 30 minutes
# dt and runtime might be read in from a control file
pset.execute(kernels, runtime=timedelta(days=2), dt=timedelta(minutes=1), output_file=output_file)


#uncomment below for interactive plots (need ipympl)
####%matplotlib widget
import netCDF4
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# using matplotlib basemap toolkit can add coastlines 
# install is picky about python version

output_file.export()  # export the trajectory data to a netcdf file

nc = netCDF4.Dataset("float_output/isopycnal_float.nc")

x = nc.variables["lon"][:].squeeze()
time = nc.variables["time"][:].squeeze()
y = nc.variables["lat"][:].squeeze()
z = nc.variables["z"][:].squeeze()
salt = nc.variables["salt"][:].squeeze()
temp = nc.variables["temp"][:].squeeze()
nc.close()


# plot
fig = plt.figure(figsize=(13,10))
ax = plt.axes()
for p in range(x.shape[0]):
    cb = ax.scatter(x[p,:], y[p,:], c=salt[p,:], s=20, marker="o")

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.title('With temperature')
plt.show()
