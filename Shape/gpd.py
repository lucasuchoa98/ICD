import geopandas as gpd
import h5py
#import pandas as pd
#from shapely.geometry import Point

filename = 'prec.nc'
f = h5py.File(filename, 'r')
df = pd.DataFrame()
df['coordinates'] = list(zip(br_lat,br_long))
df['coordinates'] = df['coordinates'].apply(Point)
gdf = gpd.GeoDataFrame(df, geometry='coordinates')

ax = rio.plot(figsize=(10, 10), alpha=1, edgecolor='k')
