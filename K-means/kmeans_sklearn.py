#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 00:01:47 2020

@author: jaekyumkim
"""


#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#import the dataset
df = pd.read_csv('wine.data')
df.head(10)

x = df.iloc[:, [0,1,2,3,4]].values

kmeans5 = KMeans(n_clusters=3)
y_kmeans5 = kmeans5.fit_predict(x)
print(y_kmeans5)

print(kmeans5.cluster_centers_)