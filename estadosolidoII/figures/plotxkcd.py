def cm2inch(value):
    return value/2.54

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

# import matplotlib as mpl
# colors = mpl.rcParams['axes.prop_cycle'].by_key()['color']
# primary = colors[0]
# secondary = colors[1]
# tertiary = colors[3]

# XKCD things
plt.xkcd()



fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# plt.xticks([])
# plt.yticks([])
# ax.set_ylim([-30, 10])

ωω=logspace(13,17,100)

me = 9.10938e-31
γ = 1.81e15
ω1 = 2.81e15
Ne_thing =  1.009e31

def Re(ω): return 1 + Ne_thing * (ω1**2-ω**2)/((ω1**2-ω**2)**2-(γ**2)*(ω**2))

ax.plot(ωω, [Re(ω) for ω in ωω])
ax.set_xscale('log')

# plt.annotate(
#     'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
#     xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))


ax.set_xlabel('Frequency')
ax.set_ylabel('The ε thing')

fig.savefig('xkcd12.pdf')
