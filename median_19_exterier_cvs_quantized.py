#!/usr/bin/env python3

import pandas
from datetime import datetime

df = pandas.read_csv('median_19_exterier_cvs.csv', sep=";", decimal=",", usecols=['day', 'hour', 'b'])

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

print(list(df.columns))
print(df.columns)
print(df.index)
print(df.head())
print(df.size)

import matplotlib.pyplot as plt

df2 = df.reset_index().pivot(columns='day',index='hour',values='b')

print(df2)

fig, ax = plt.subplots()

from matplotlib import colors
cmap = colors.ListedColormap(['dimgray', 'darkgrey', 'lightgray', 'lightsteelblue', 'dodgerblue', 'deepskyblue', 'aliceblue', 'yellow', 'gold', 'orange'])
bounds=[0, 2000, 5000, 10000, 20000, 40000, 60000, 80000, 100000, 120000, 150000]
norm = colors.BoundaryNorm(bounds, cmap.N)
im = ax.pcolor(df2, cmap=cmap, norm=norm)


import locale
locale.setlocale(locale.LC_TIME, "cs_CZ.utf8")

#import matplotlib.dates as mdates
#
#months = mdates.MonthLocator()  # every month
#days = mdates.DayLocator()
#months_fmt = mdates.DateFormatter('%b')
#
#ax.xaxis.set_major_locator(months)
#ax.xaxis.set_major_formatter(months_fmt)
#ax.xaxis.set_minor_locator(days)

def dateToStr(d):
  if d.day == 1:
    return d.strftime('%b')
  else:
    return ""

ticklabelsx = [dateToStr(item) for item in df2.columns]

ax.set_xticks(range(len(ticklabelsx)))
ax.set_xticklabels(ticklabelsx, rotation = 90, fontsize=20)


#hours = mdates.HourLocator()   # every year
#hours_fmt = mdates.DateFormatter('%H')
#
#ax.yaxis.set_major_locator(hours)
#ax.yaxis.set_major_formatter(hours_fmt)

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

