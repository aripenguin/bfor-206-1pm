#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:28:44 2019

@author: root
"""

import numpy as np
import pandas as pd
from matplotlib.pyplot import hist

matrix = np.random.randint(0,100,size=(100, 4))
#print(matrix)
print(matrix[90:100,0])

random_df = pd.DataFrame(matrix, columns=list('ABCD'))
random_df['A']
random_df['A'].plot.hist()

new_col = np.random.normal(loc=5, scale=2, size=100)
# add it as a new column to our dataframe
random_df['E'] = new_col
random_df['E'].plot.hist()

labels = np.random.choice(['A_1', 'A_2', 'B_1', 'B_2'], size=100)
random_df['labels'] = labels
list(random_df)

#"What is up BFOR 206?".splint(" ")

label_group = random_df['labels'].str.split('_')
print(label_group)
random_df['group'] = label_group.str[0]
#random_df.head()
random_df.tail(10)

random_df.describe(include='all')
random_df.groupby('group')['A', 'E'].mean()
df_summary = random_df.groupby('group').mean()

