#!/usr/bin/env python3

import pandas
from datetime import datetime

df = pandas.read_csv('exterier_en_30_cvs.csv', sep=";", decimal=",", usecols=['day', 'hour', 'b'])

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

im = ax.imshow(df2, aspect='auto', origin='lower')


import locale
locale.setlocale(locale.LC_TIME, "cs_CZ.utf8")

def dateToStr(d):
  if d.day == 1:
    return d.strftime('%b')
  else:
    return ""

ticklabelsx = [dateToStr(item) for item in df2.columns]

ax.set_xticks(range(len(ticklabelsx)))
ax.set_xticklabels(ticklabelsx, rotation = 90)


def timeToStr(d):
  if d.minute == 0 and d.second == 15:
    return d.strftime('%H:00')
  else:
    return ""

ticklabelsy = [timeToStr(item) for item in df2.index]

ax.set_yticks(range(len(ticklabelsy)))
ax.set_yticklabels(ticklabelsy)

plt.colorbar(im)

plt.show()
