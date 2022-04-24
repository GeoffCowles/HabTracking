

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

ncfile = '/home/lcabral4/WHOI/HAB4/HabTracking/float_output/box50.nc'


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
    if p == 0:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 1:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 2:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 3:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p ==4:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 5:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p ==  6:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 7:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 8:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 9:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 10:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 11:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 12:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 13:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 14:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 15:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 16:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 17:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 18:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 19:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 20:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 21:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 22:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 23:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 24:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 25:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 26:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 27:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 28:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 29:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 30:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 31:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 32:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 33:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 34:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 35:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 36:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 37:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 38:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 39:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 40:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 41:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 42:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 43:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 44:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 45:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 46:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 47:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 48:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 49:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 50:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if  p == 51:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 52:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 53:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 54:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 55:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 56:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 57:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 58:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 59:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 60:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 61:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 62:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 63:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 64:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 65:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 66:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 67:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 68:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 69:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 70:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 71:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 72:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 73:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 74:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 75:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 76:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 77:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 78:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 79:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 80:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 81:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 82:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 83:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 84:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 85:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 86:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 87:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 88:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 89:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 90:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 91:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 92:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 93:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 94:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 95:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 96:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 97:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 98:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 99:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 100:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 101:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 102:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 103:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 104:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 105:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 106:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 107:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 108:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 109:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 110:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 111:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 112:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 113:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 114:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 115:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 116:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 117:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 118:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 119:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 120:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 121:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 122:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 123:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 124:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 125:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 126:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 127:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 128:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 129:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 130:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 131:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 132:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 133:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 134:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 135:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 136:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 137:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 138:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 139:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 140:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 141:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 142:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 143:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 144:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 145:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 146:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 147:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 148:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 149:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 150:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 151:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 152:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 153:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 154:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 155:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 156:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 157:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 158:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 159:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 160:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 161:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 162:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 163:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 164:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 165:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 166:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 167:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 168:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 169:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 170:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 171:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 172:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 173:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 174:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 175:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 176:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 177:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 178:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 179:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 180:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 181:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 182:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 183:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 184:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 185:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 186:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 187:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 188:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 189:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 190:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 191:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 192:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 193:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 194:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 195:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 196:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 197:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 198:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 199:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 200:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 201:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 202:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 203:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 204:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 205:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 206:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 207:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 208:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 209:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 210:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 211:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 212:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 213:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 214:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 215:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 216:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 217:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 218:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 219:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 220:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 221:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 222:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 223:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 224:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 225:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 226:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 227:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 228:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 229:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 230:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 231:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 232:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 233:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 234:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 235:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 236:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 237:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 238:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 239:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 240:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 241:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 242:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 243:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 244:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 245:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 246:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 247:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 248:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 249:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 250:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 251:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 252:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 253:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 254:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 255:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 256:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 257:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 258:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 259:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 260:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 261:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 262:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 263:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 264:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 265:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 266:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 267:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 268:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 269:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 270:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 271:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 272:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 273:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 274:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 275:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 276:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 277:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 278:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 279:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 280:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 281:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 282:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 283:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 284:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 285:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 286:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 287:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p ==288:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 289:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 290:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 291:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 292:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 293:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 294:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 295:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 296:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 297:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 298:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 299:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 300:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 301:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 302:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 303:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 304:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 305:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 306:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 307:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 308:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 309:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 310:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 311:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 312:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 313:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 314:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 315:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 316:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 317:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 318:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 319:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 320:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 321:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 322:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 323:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 324:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 325:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 326:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 327:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 328:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 329:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 330:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 331:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 332:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 333:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 334:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 335:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 336:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 337:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 338:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 339:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 340:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 341:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 342:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 343:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 344:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 345:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 346:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 347:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 348:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 349:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 350:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 351:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 352:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 353:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 354:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 355:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 356:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 357:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 358:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 359:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 360:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 361:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 362:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 363:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 364:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 365:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 366:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 367:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 368:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 369:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 370:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 371:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 372:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 373:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 374:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 375:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 376:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 377:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 378:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 379:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 380:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 381:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 382:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 383:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 384:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 385:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 386:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 387:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 388:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 389:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 390:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 391:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 392:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 393:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 394:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 395:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 396:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 397:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 398:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 399:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 400:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 401:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 402:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 403:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 404:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 405:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 406:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 407:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 408:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 409:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 410:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 411:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 412:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 413:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 414:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 415:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 416:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 417:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 418:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 419:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 420:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 421:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 422:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 423:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 424:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 425:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 426:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 427:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 428:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 429:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 430:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 431:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 432:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 433:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 434:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 435:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 436:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 437:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 438:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 439:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 440:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 441:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 442:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 443:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 444:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 445:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 446:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 447:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 448:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 449:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 450:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 451:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 452:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 453:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 454:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 455:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 456:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 457:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 458:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 459:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 460:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 461:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 462:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 463:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 464:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 465:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 466:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 467:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 468:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 469:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 470:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 471:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 472:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 473:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 474:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 475:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 476:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 477:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 478:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 479:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 480:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 481:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 482:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 483:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 484:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 485:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 486:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 487:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 488:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 489:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 490:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 491:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 492:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 493:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 494:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 495:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 496:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 497:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 498:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 499:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 500:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 501:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 502:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 503:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 504:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 505:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 506:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 507:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 508:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 509:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 510:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 511:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 512:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 513:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 514:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 515:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 516:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 517:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 518:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 519:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 520:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 521:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 522:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 523:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 524:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 525:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 526:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 527:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 528:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 529:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 530:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 531:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 532:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 533:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 534:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 535:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 536:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 537:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 538:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 539:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 540:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 541:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 542:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 543:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 544:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 545:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 546:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 547:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 548:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 549:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)

    if p == 600:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 601:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 602:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 603:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 604:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 605:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 606:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 607:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 608:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 609:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 610:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 611:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 612:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 613:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 614:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 615:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 616:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 617:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 618:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 619:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 620:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 621:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 622:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 623:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 624:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 625:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 626:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 627:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 628:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 629:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 630:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 631:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 632:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 633:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 634:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 635:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 636:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 637:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 638:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 639:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 640:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 641:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 642:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 643:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 644:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 645:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 646:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 647:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 648:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 649:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 650:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 651:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 652:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 653:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 654:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 655:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 656:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 657:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 658:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 659:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 660:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 661:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 662:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 663:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 664:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 665:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 666:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 667:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 668:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 669:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 670:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 671:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 672:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 673:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 674:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 675:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 676:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 677:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 678:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 679:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 680:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 681:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 682:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 683:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 684:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 685:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 686:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 687:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 688:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 689:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 690:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if  p == 691:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 692:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 693:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 694:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 695:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 696:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 697:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 698:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 699:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 700:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 701:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 702:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 703:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 704:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 705:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 706:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 707:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 708:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 709:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 710:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 711:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 712:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 713:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 714:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 715:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 716:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 717:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 718:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 719:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 720:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 721:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 722:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 723:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 724:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 725:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 726:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 727:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 728:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 729:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 730:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 731:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 732:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 733:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 734:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 735:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 736:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 737:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 738:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 739:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 740:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 741:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 742:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 743:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 744:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 745:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 746:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 747:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 748:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 749:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 750:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 751:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 752:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 753:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 754:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 755:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 756:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 757:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 758:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 759:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 760:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 761:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 762:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 763:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 764:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 765:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 766:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 767:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 768:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 769:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 770:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 771:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 772:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 773:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 774:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 775:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 776:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 777:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 778:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 779:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 780:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 781:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 782:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 783:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 784:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 785:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 786:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 787:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 788:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 789:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 790:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 791:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 792:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 793:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 794:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 795:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 796:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 797:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)
    if p == 798:
        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1)
    if p == 799:
        plt.scatter(x[p,:], y[p,:], color = 'blue', s = 0.1)

#    else:
#        plt.scatter(x[p,:], y[p,:], color = 'red', s = 0.1, label=my_labels["x2"])
#        my_labels["x2"] = "_nolegend_"

        
    



coord1 = [[-65, 60], [-63, 65], [-50,55] ,[-55,50]]
coord1.append(coord1[0])
xs, ys = zip(*coord1) #create lists of x and y values 
plt.plot(xs,ys)

# plot

#print(particle_number)
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('6/10/15 800 Particle Release ')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("9Images_6_10_15_release_Point_In_Polygon.png")


