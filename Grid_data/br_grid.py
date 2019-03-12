import pandas as pd
import h5py
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='mateus.normande', api_key='64glegfYYWD1va1j3Gu2')

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
lat = list(f[data1])
long = list(f[data2])
count = list(f[data3])
dist_n = list(f[data4])
dia = pd.DataFrame(count[0])

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

mapbox_access_token = "pk.eyJ1IjoibWF0ZXVzLW5vcm1hbmRlIiwiYSI6ImNqc2tjOHZ1cTE0d3UzeW56aWZ6eG9yMXQifQ.7AYFzmLq_ycuWnF2bGhO_Q"
data = [
    go.Scattermapbox(
        lat= br_lat,
        lon = br_long,
        mode='markers',
        marker=dict(size=5)
        )]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=-9.551585,
            lon=-35.775490,
        ),
        pitch=0,
        zoom=10
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='Coordenadas_BR')
