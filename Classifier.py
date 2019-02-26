# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:06:26 2019

@author: Dipanshu
"""

#import library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#import data set
dataset=pd.read_csv('dataset.csv')
x=dataset.iloc[:,[1,2,3,5,10,11,12,13,14,15,16,17,18,19]]
y=dataset.iloc[:,20].values

x=pd.x.drop()


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder( )
x[:,2]=labelencoder_x.fit_transform(x[:,2])
ohe=OneHotEncoder(categorical_features=[0])
x=ohe.fit_transform(x).toarray()