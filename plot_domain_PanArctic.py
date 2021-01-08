from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset

from rpn.rpn import RPN
from rpn.domains.rotated_lat_lon import RotatedLatLon
from rpn import level_kinds

'''
Reads a Netcdf file and plot the domain over the globe
'''

#r = RPN('/glacier/caioruman/Data/Geophys/PanArctic0.5/pan_artic_me_0.5')
#r = RPN('/home/cruman/scratch/CanArc_004deg_1500x900.fst')
#nc = Dataset('PanCanadian.nc')
r = RPN('pan_artic_me_0.5')
#var = "MSKC"

me = r.variables['ME'][0,0]
#lon = nc.variables['lon'][:]
#lat = nc.variables['lat'][:]

lon_r, lat_r = r.get_longitudes_and_latitudes_for_the_last_read_rec()

#m = Basemap(resolution='l',projection='ortho',lon_0=-90,lat_0=70)
m = Basemap(resolution='l',projection='ortho',lon_0=-110,lat_0=80)
#m = Basemap(resolution='l', projection='', 

fig1 = plt.figure(figsize=(7, 11), frameon=False, dpi=200)
ax = fig1.add_axes([0.1,0.1,0.8,0.8])

#print(lon[:,0].shape)
#print(lat[0,:].shape)
#print(lon.shape)
#print(lat.shape)
#newlon = np.where(lon <= 180, lon, lon - 360)

# big domain
# Plotting the inner lines every 5 points
for i in range(0, lat_r[0,:].shape[0],5):
    x, y = m(lon_r[:,i], lat_r[:,i])
    m.plot(x, y, color='red', linewidth=0.5)

for i in range(0, lon_r[:,0].shape[0],5):
    x, y = m(lon_r[i,:], lat_r[i,:])
    m.plot(x, y, color='red', linewidth=0.5)

# small domain
#for i in range(0,lat[0,:].shape[0],25):
#    x, y = m(lon[:,i], lat[:,i])
#    m.plot(x, y, color='red', linewidth=0.25)

#for i in range(0,lon[:,0].shape[0],25):
#    x, y = m(lon[i,:], lat[i,:])
#    m.plot(x, y, color='red', linewidth=0.25)

ii = [0,-1]

# Plotting the border of the domain in thicker lines
for i in ii:
        
#     x,y = m(lon[:,i],lat[:,i])
#     m.plot(x,y,color='red')

#     x,y = m(lon[i,:],lat[i,:])
#     m.plot(x,y,color='red')

    x,y = m(lon_r[:,i], lat_r[:,i])
    m.plot(x,y,color='red')

    x,y = m(lon_r[i,:], lat_r[i,:])
    m.plot(x,y,color='red')

#    x,y = m(lon_b[i,:],lat_b[i,:])
#    m.plot(x,y,color='red')

#    x,y = m(lon_b[:,i],lat_b[:,i])
#    m.plot(x,y,color='red')

# Blending domain
#bb = 40
#ii = [bb,-bb]

#for i in ii:

#   x,y = m(lon[bb:-bb,i],lat[bb:-bb,i])
#   m.plot(x,y,color='red')

#   x,y = m(lon[i,bb:-bb],lat[i,bb:-bb])
#   m.plot(x,y,color='red')

#   x,y = m(lon_b[i,bb:-bb],lat_b[i,bb:-bb])
#   m.plot(x,y,color='red')
           
#   x,y = m(lon_b[bb:-bb,i],lat_b[bb:-bb,i])
#   m.plot(x,y,color='red')


        #r.close()

#m.readshapefile('shapefile/lpr_000b16a_e', 'lpr_000b16a_e')
#m.drawcoastlines(linewidth=0.25)
#m.drawmapboundary(fill_color='#999999')
        #m.drawcountries(linewidth=0.5)
        #m.drawstates(linewidth=0.5)
        #m.drawlsmask()
m.shadedrelief()
#m.fillcontinents(color='#E8112D', lake_color='#76a6cc')
#m.fillcontinents(color='#666666', lake_color='#999999')

        #plt.title('Figure 3: Grid telescoping into Nunavut\nfor convection permitting simulations', y=-0.12, fontsize=40)
plt.savefig('domain_center_grid.png', pad_inches=0.0, bbox_inches='tight', transparent=True)
