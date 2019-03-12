import plotly.plotly as py
import plotly.graph_objs as go
import h5py
import plotly
plotly.tools.set_credentials_file(username='mateus.normande', api_key='64glegfYYWD1va1j3Gu2')

filename = 'prec.nc'
f = h5py.File(filename, 'r')

print("Keys: %s" % f.keys())
fields = list(f.keys())
lat_key = list(fields)[0]
log_key = list(fields)[2]
count_key = list(fields)[2]

count = list(f[count_key])
lat = list(f[lat_key])
long = list(f[log_key])

grid = []
list_lat = []
list_long = []
for i in range(len(lat)):
    for j in range(len(long)):
        coord = lat[i],long[j]
        list_lat.append(lat[i])
        list_long.append(long[j])
        grid.append(coord)


mapbox_access_token = "pk.eyJ1IjoibWF0ZXVzLW5vcm1hbmRlIiwiYSI6ImNqczF6cG9oMzIwNnc0NHFyd2VqbGpheHUifQ.OZYbhTGC7-BXFMUhEQXRNg"
data = [
    go.Scattermapbox(
        lat= list_lat,
        lon = list_long,
        mode='markers',
        marker=dict(size=3)
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
py.iplot(fig, filename='Coordenadas')
