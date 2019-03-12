import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd

npzfile = np.load('prec_raw.npz')
latlon = npzfile['latlon']
df_latlon = pd.DataFrame(latlon)

mapbox_access_token = 'pk.eyJ1IjoibHVjYXN1Y2hvYSIsImEiOiJjanFxdjVjNjMwZjcwM3htdm9pbzViOW4wIn0.E8WOGX1mAGUjr0O4fbcXVA'

data = [
    go.Scattermapbox(
        lat=df_latlon[0].tolist(),
        lon=df_latlon[1].tolist(),
        mode='markers',
        marker=dict(size=9),
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=-10.116700,
            lon=-36.650002
        ),
        pitch=0,
        zoom=10
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='1212 Multiple Mapbox')
