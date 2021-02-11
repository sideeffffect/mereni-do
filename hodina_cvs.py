#!/usr/bin/env python3

import pandas

df = pandas.read_csv('hodina_cvs.csv', sep=";", index_col=['day1', 'hour'], parse_dates=['day1', 'hour'], dayfirst=True, decimal=",", usecols=['day1', 'hour', 'horizon'])

print(list(df.columns))
print(df.columns)
print(df.index)
print(df.head())
print(df.size)

import matplotlib.pyplot as plt

df2 = df.reset_index().pivot(columns='day1',index='hour',values='horizon')

print(df2)

im = plt.imshow(df2, aspect='auto', origin='lower')

ax = plt.gca()

def datetimeToStr(d):
  if d.day == 1:
    return d.strftime('%b')
  else:
    return ""

import locale
locale.setlocale(locale.LC_TIME, "cs_CZ.utf8")

ticklabelsx = [datetimeToStr(item) for item in df2.columns]

ax.set_xticks(range(len(ticklabelsx)))
ax.set_xticklabels(ticklabelsx, rotation = 90, fontsize=20)

ticklabelsy = [item.strftime('%H:xx') for item in df2.index]

ax.set_yticks(range(len(ticklabelsy)))
ax.set_yticklabels(ticklabelsy, fontsize=20)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.tick_params(labelsize=20)
cbar.ax.set_ylabel("lx", rotation=90, fontsize=20)

plt.show()

