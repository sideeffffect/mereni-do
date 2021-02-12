#!/usr/bin/env python3

import pandas
from datetime import datetime

df = pandas.read_csv('median_19_interier_cvs.csv', sep=";", decimal=",", usecols=['day', 'hour', 'c'])

print(list(df.columns))
print(df.columns)
print(df.index)
print(df.head())
print(df.size)


df['day'] = pandas.to_datetime(df['day'], format='%Y-%b-%d')

def normalizeYear(d):
  if d.year == 2020:
    return d.replace(year=2019)
  else:
    return d

df['day'] = df['day'].apply(normalizeYear)

df['hour'] = pandas.to_datetime(df['hour'], format='%H:%M:%S')

df['c'] = df['c'].apply(lambda x: x * 1.6)

print(list(df.columns))
print(df.columns)
print(df.index)
print(df.head())
print(df.size)

import matplotlib.pyplot as plt

df2 = df.reset_index().pivot(columns='day',index='hour',values='c')

print(df2)

fig, ax = plt.subplots()

from matplotlib import colors
cmap = colors.ListedColormap(['black', 'dimgray', 'darkgrey', 'gainsboro', 'lightsteelblue', 'powderblue', 'dodgerblue', 'royalblue', 'deepskyblue', 'cyan', 'yellow', 'orange', 'firebrick'])
bounds=[0, 100, 200, 500, 1000, 2000, 4000, 5000, 6000, 7000, 8000, 10000, 12000, 15000]
norm = colors.BoundaryNorm(bounds, cmap.N)
im = ax.pcolor(df2, cmap=cmap, norm=norm)


import locale
locale.setlocale(locale.LC_TIME, "cs_CZ.utf8")

def dateToStr(d):
  if d.day == 1:
    return d.strftime('%b')
  else:
    return ""

ticklabelsx = [dateToStr(item) for item in df2.columns]

ax.set_xticks(range(len(ticklabelsx)))
ax.set_xticklabels(ticklabelsx, rotation = 90, fontsize=20)


def timeToStr(d):
  if d.minute == 0 and d.second == 15:
    return d.strftime('%H:00')
  else:
    return ""

ticklabelsy = [timeToStr(item) for item in df2.index]

ax.set_yticks(range(len(ticklabelsy)))
ax.set_yticklabels(ticklabelsy, fontsize=20)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.tick_params(labelsize=20)
cbar.ax.set_ylabel("lx", rotation=90, fontsize=20)

plt.show()

