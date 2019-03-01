# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:14:49 2019

@author: Lucas
"""
import geopandas as gpd
import h5py
import pandas as pd
from shapely.geometry import Point

filename = 'prec.nc'
f = h5py.File(filename, 'r')

# List all groups
for i in f.keys():
    print(i)

data1 = list(f.keys())[0]
data2 = list(f.keys())[2]
data3 = list(f.keys())[4]
data4 = list(f.keys())[3]


# Get the data
lat = list(f[data2])
long = list(f[data3])
count = list(f[data1])
dia = pd.DataFrame(count[4])

grid = []
list_lat = []
list_long = []
for i in range(len(lat)):
    for j in range(len(long)):
        coord = lat[i],long[j],dia[j][i]
        list_lat.append(lat[i])
        list_long.append(long[j])
        grid.append(coord)
 
br_lat = []
br_long = []      
for k in range(len(grid)):
    if grid[k][2] != 127:
        br_lat.append(grid[k][0])
        br_long.append(grid[k][1])

shape = gpd.read_file("regioes_hidrograficas.shp")
rio = shape[shape.index==1]

df = pd.DataFrame()
df['coordinates'] = list(zip(br_lat,br_long))
df['coordinates'] = df['coordinates'].apply(Point)
gdf = gpd.GeoDataFrame(df, geometry='coordinates')

rio.within()


#for i in shape:
 #   print(i)

#url = 'http://dados.al.gov.br/dataset/104be3f2-e942-43ea-bdde-afb660a32a6f/resource/650dddab-74af-454b-bb34-495c66798dd7/download/regioeshidrograficas.geojson'
#df = geopandas.read_file(url)

ax = rio.plot(figsize=(10, 10), alpha=1, edgecolor='k')
