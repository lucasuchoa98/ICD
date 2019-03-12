# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:20:53 2019

@author: Lucas
"""
import h5py
from xarray import Dataset

#Ponto de estudo: (-35.875;-9.375), (99;153)

filename = 'Rs_ctrl_s1.nc'
f = h5py.File(filename, 'r')

for i in f.keys():
    print(i)

data_ct = list(f.keys())[0]
data_dn = list(f.keys())[1]
data_lt = list(f.keys())[2]
data_ln = list(f.keys())[3]
data_tm = list(f.keys())[4]

lat = list(f[data_lt])
long = list(f[data_ln])
count = list(f[data_ct])
dist_n = list(f[data_dn])
time = list(f[data_tm])

