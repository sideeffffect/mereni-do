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

def quantize(n):
  if n > 100000:
    return 100000
  elif n > 80000:
    return 80000
  elif n > 60000:
    return 60000
  elif n > 40000:
    return 40000
  elif n > 20000:
    return 20000
  elif n > 10000:
    return 10000
  elif n > 5000:
    return 5000
  elif n > 2500:
    return 2500
  elif n > 1000:
    return 1000
  elif n > 0:
    return 100
  else:
    return n

df['b'] = df['b'].apply(quantize)

import numpy
df['b'] = numpy.log10(df['b'])

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

im = ax.imshow(df2, aspect='auto', origin='lower', cmap=plt.get_cmap("twilight_shifted"))


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
cbar.ax.set_ylabel("log_10 lx", rotation=90, fontsize=20)

plt.show()

