import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd


npzfile = np.load('prec_raw.npz')
#estou enfrentando problemas com memória na proxima linha
var = npzfile['var']
latlon = npzfile['latlon']
days = npzfile['days']


#modo não muito eficiente de se tratar dados de dias
df_var = pd.DataFrame(var).T
#outro jeito de ter a serie de dias do df_days, achei melhor pois tem mais conteudo desse formato na web
nday = pd.date_range('1/1/1980',periods=13149,freq='D')
df_latlon = pd.DataFrame(latlon)
df_days = pd.DataFrame(days)



data = [go.Scatter(x=nday, y=df_var[0])]

py.iplot(data, filename = 'Ruberto_var')
