#!/usr/bin/env python3

import pandas

df = pandas.read_csv('zapocitane_hodnoty.csv', sep=";", index_col=['day1', 'hour'], parse_dates=['day1', 'hour'], dayfirst=True, decimal=",", usecols=['day1', 'hour', 'horizon'])

print(list(df.columns))
print(df.columns)
print(df.index)
print(df.head())
print(df.size)

import matplotlib.pyplot as plt

df2 = df.reset_index().pivot(columns='day1',index='hour',values='horizon')

print(df2)

plt.imshow(df2, aspect='auto', origin='lower')

ax = plt.gca()

ticklabelsx = ['']*len(df2.columns)
ticklabelsx[::30] = [item.strftime('%b %d') for item in df2.columns[::30]]

ax.set_xticks(range(len(ticklabelsx)))
ax.set_xticklabels(ticklabelsx)

ax.set_xticks(range(len(ticklabelsx)))
ax.set_xticklabels(ticklabelsx)

ax.set_yticks(range(len(df2.index)))
ax.set_yticklabels(df2.index)

plt.show()

