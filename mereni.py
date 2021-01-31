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


print(df2)

#fig = plt.figure(figsize=(20, 100))
#ax1 = fig.add_subplot(131)
#ax1.set_title("A")
#ax1.tick_params(axis='both', direction='out')
#ax1.set_xticks(range(len(df2.columns)))
#ax1.set_xticklabels(df2.columns)
#ax1.set_yticks(range(len(df2.index)))
#ax1.set_yticklabels(df2.index)
#im1 = ax1.imshow(df2, aspect='auto', origin='lower')

plt.imshow(df2, aspect='auto', origin='lower')

ax = plt.gca()

#import matplotlib.dates as mdates
#locator = mdates.AutoDateLocator()
#formatter = mdates.ConciseDateFormatter(locator)
#ax.xaxis.set_major_locator(locator)
#ax.xaxis.set_major_formatter(formatter)

#import matplotlib.ticker as ticker
ticklabels = ['']*len(df2.columns)
ticklabels[::30] = [item.strftime('%b %d') for item in df2.columns[::30]]
#ax.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))

ax.set_xticks(range(len(ticklabels)))
ax.set_xticklabels(ticklabels)


#ax.set_xticks(range(len(df2.columns)))
#ax.set_xticklabels(df2.columns, rotation = 90)

#ax.tick_params(axis='y', labelrotation = 45)
#ax.locator_params(nbins=10, axis='x')
#plt.xticks(range(len(df2.columns)), df2.columns, rotation = 90)
#plt.yticks(range(len(y)), y)
#plt.gcf().autofmt_xdate()
plt.show()


#plt.contour(df2, 2)
#plt.show()

#sns.heatmap(df)

