#!/usr/bin/env python3

import pandas

df = pandas.read_csv('zapocitana_hodina_tm_cvs.csv', sep=";", index_col=['day1', 'hour'], parse_dates=['day1', 'hour'], dayfirst=True, decimal=",", usecols=['day1', 'hour', 'horizon'])

print(list(df.columns))
print(df.columns)
print(df.index)
print(df.head())
print(df.size)

import matplotlib.pyplot as plt

df2 = df.reset_index().pivot(columns='day1',index='hour',values='horizon')

print(df2)

fig, ax = plt.subplots()

from matplotlib import colors
cmap = colors.ListedColormap(['black', 'dimgray', 'darkgrey', 'gainsboro', 'lightsteelblue', 'powderblue', 'dodgerblue', 'royalblue', 'deepskyblue', 'cyan', 'yellow', 'orange', 'firebrick'])
bounds=[0, 1000, 2000, 5000, 10000, 20000, 40000, 50000, 60000, 70000, 80000, 100000, 120000, 150000]
norm = colors.BoundaryNorm(bounds, cmap.N)
im = ax.pcolor(df2, cmap=cmap, norm=norm)


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

ticklabelsy = [item.strftime('%H:00') for item in df2.index]

ax.set_yticks(range(len(ticklabelsy)))
ax.set_yticklabels(ticklabelsy, fontsize=20)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.tick_params(labelsize=20)
cbar.ax.set_ylabel("lx", rotation=90, fontsize=20)

plt.show()

