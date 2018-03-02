#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import seaborn as sns
import datetime as dt

plt.style.use('custom')
plt.rcParams['axes.facecolor'] = '#E5E5E5'
plt.rcParams['grid.color'] = 'white'

colors = mpl.rcParams['axes.prop_cycle'].by_key()['color']
primary = colors[0]
secondary = colors[1]

def cm2inch(value):
    return value/2.54

# Get data
df = pd.melt(pd.read_csv('statistics.csv'),
        id_vars=['Día','Asistentes'],
        value_name='Nota de la clase',
        var_name='Examinador'
)

df['Día'] = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in df['Día']]
df['Semana'] = [int(d.strftime('%W')) for d in df['Día']]
df['Semana'] -= min(df['Semana'])-1
df['Día de la semana'] = [d.strftime('%A') for d in df['Día']]

df = df.sort_values(by='Día de la semana')


# Plot

plt.figure()

s1 = plt.subplot(2, 2, 1)
ax = sns.swarmplot(x='Día de la semana',
                 y='Nota de la clase',
                 hue='Examinador',
                 data=df)
ax.legend_.remove()
ax.set_ylim([-3,10])
ax.set_xlabel('')
ax.axes.get_xaxis().set_ticklabels([])

s2 = plt.subplot(2, 2, 2)
ax = plt.gca()
for x, xdf in df.groupby('Examinador'):
    ax.scatter(xdf['Semana'], xdf['Nota de la clase'],
               label=x)
ax.legend(frameon=True)
ax.set_ylabel('')
ax.set_xlabel('')
ax.set_ylim([-3,10])
ax.axes.get_yaxis().set_ticklabels([])
ax.axes.get_xaxis().set_ticklabels([])

s3 = plt.subplot(2, 2, 3)
ax = sns.swarmplot(x='Día de la semana',
                 y='Asistentes',
                 color=primary,
                 data=df)
ax.set_ylim([15,30])
ax.set_ylabel('Asistentes')
ax.set_xlabel('Día de la semana')

s4 = plt.subplot(2, 2, 4)
ax = plt.gca()
ax.scatter(df['Semana'], df['Asistentes'])
ax.set_ylim([15,30])
ax.set_ylabel('')
ax.set_xlabel('Semana')
ax.axes.get_yaxis().set_ticklabels([])

plt.tight_layout()

plt.savefig('figures/metaplot.pdf', figsize=(cm2inch(10), cm2inch(8)))
