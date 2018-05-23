# -*- coding: utf-8 -*-
"""
Created on Wed May 23 09:56:25 2018

@author: 705family
"""

import os
os.chdir("C:/Users/705family/Desktop/decisiontree")
import tree

data,y = tree.createDataSet()
myTree = tree.createTree(data,y)


# In[] test Part 2
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
data = pd.read_excel('西瓜数据集.xlsx')
data = data.iloc[:,1:-1]

clf = LabelEncoder()
label=[[] for i in range(np.size(data,1))]
for i in range(np.size(data,1)):
    data.iloc[:,i] = clf.fit_transform(data.iloc[:,i])
    label[i][:]=list(clf.classes_)
y = data.iloc[:,-1]
data = np.array(data)
data = data.tolist()
y = np.array(y)
y= y.tolist()
    
myTree = tree.createTree(data,y)
