import xarray as xr
import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='mateus.normande', api_key='64glegfYYWD1va1j3Gu2')

#la = 98 (-9.625), lo = 153 (-35.875)
file_name = "ETo_daily_UT_Brazil_v2_20000101_20061231.nc"
xrdataset = xr.open_dataset(file_name)

ETo = xrdataset["ETo"]
time = xrdataset["time"]
longitude = xrdataset["longitude"]
latitude = xrdataset["latitude"]

list_ETo = []
for p in ETo.values:
    list_ETo.append(p)    

list_datetime = []
for datetime in time.values:
    list_datetime.append(datetime)

list_ETo_98_153 = []
for m in list_ETo:
    list_ETo_98_153.append(m[98][153])

df = pd.DataFrame(list_ETo_98_153, index = list_datetime)

data = [go.Scatter(x=df.index, y=df.values)]
py.iplot(data, filename = 'time-series-ETo')