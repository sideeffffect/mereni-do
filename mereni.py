#!/usr/bin/env python3
import pandas
#import dateparser

print("hello")

#def parse(x):
#  dateparser.parse(x, date_formats=['%d.%M.%Y'])

df = pandas.read_csv('median_19_exterier_cvs.csv', sep=";", index_col=['day', 'hour'], parse_dates=['day', 'hour'], dayfirst=True, decimal=",", usecols=['day', 'hour', 'b'])
print(list(df.columns))
print(df.columns)
print(df.index)
print(df.head())
print(df.size)

import matplotlib.pyplot as plt
#import numpy as np

#a = np.random.random((16, 16))
#plt.imshow(a, cmap='hot', interpolation='nearest')
#plt.show()

#plt.imshow(df, cmap ="RdYlBu")

#plt.imshow(df)

#plt.pcolor(df)

#plt.show()

import seaborn as sns

df2 = df.reset_index().pivot(columns='day',index='hour',values='b')

plt.imshow(df2, aspect='auto')
plt.show()

#sns.heatmap(df)

