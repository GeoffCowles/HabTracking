

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

ncfile = '/home/lcabral4/WHOI/HAB4/HabTracking/float_output/box1.nc'


data = Dataset(ncfile)

y = data.variables['lat'][:]

x = data.variables['lon'][:]
time = data.variables['time'][:]
temp = data.variables['temp'][:]

from shapely.geometry import LineString, MultiLineString
from shapely.geometry import Polygon, Point



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


my_labels = {"x1" : "Particle In Labrador Sea", "x2" : "Particle Not In Labrador Sea"}

polygon1 = Polygon([(-20.4, 63.2), (-20.4, 62.5), (-20.2, 62.5), (-20.2, 63.5)])
polygon2 = Polygon([(-65, 60), (-63, 65), (-50,55) ,(-55,50)])
for p in range(x.shape[0]):
    if p == 1:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1, label=my_labels["x1"])
        my_labels["x1"] = "_nolegend_"
    if p == 19:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 25:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 26:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 32:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 36:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 42:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 45:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 48:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 61:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 62:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 66:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 79:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 99:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 105:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 106:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 107:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 108:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 110:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 113:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 114:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 119:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 134:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 142:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 148:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 153:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 163:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 173:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 188:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 219:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 221:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 226:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 229:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 232:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 234:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 240:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 244:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 246:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 253:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 254:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 259:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 266:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 282:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 286:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 300:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 313:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 330:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 339:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 340:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 352:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 388:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 398:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 411:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 434:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 447:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 449:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 457:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 461:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 475:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 479:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 480:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 484:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 485:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 493:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 496:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 499:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 505:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 517:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 525:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 530:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 532:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 534:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 537:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 544:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 545:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 546:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 554:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 561:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 572:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 573:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 576:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 581:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 588:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 619:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 624:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 635:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 645:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 658:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 664:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 679:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 680:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 708:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 711:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 720:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 738:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 748:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 757:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 764:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 769:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 770:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 780:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 788:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 789:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    else:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1, label=my_labels["x2"])
        my_labels["x2"] = "_nolegend_"

        
    



coord1 = [[-65, 60], [-63, 65], [-50,55] ,[-55,50]]
coord1.append(coord1[0])
xs, ys = zip(*coord1) #create lists of x and y values 
plt.plot(xs,ys)

# plot

#print(particle_number)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('7/2/14 800 Particle Release Point Within Polygon ')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("7_2_14_release_Point_In_Polygon.png")


