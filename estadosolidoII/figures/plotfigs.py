#!/usr/bin/env python3

# Imports
def cm2inch(value):
    return value/2.54

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
def coth(x): return (exp(2*x)+1)/(exp(2*x)-1)
from sys import stdin, argv
import pandas as pd

plt.style.use('custom')

import matplotlib as mpl
colors = mpl.rcParams['axes.prop_cycle'].by_key()['color']
primary = colors[0]
secondary = colors[1]
tertiary = colors[3]


# Langevin function
fig = plt.figure( figsize=(cm2inch(5), cm2inch(4)) )

plt.xticks([])
plt.yticks([])

xx1 = linspace(1e-5,5,100)
xx2 = linspace(1e-5,3,100)
langevin = coth(xx1) - 1/xx1
linear = 1/3*xx2

plt.xlabel('ζ')
plt.ylabel('L(ζ)')
plt.plot(xx1, langevin, color=primary)
plt.plot(xx2, linear, '--',linewidth=0.5, color=primary)
plt.text(1.6, 0.85, 'ζ/3', fontsize=10, rotation=45, color='gray')
plt.savefig('langevin.pdf')

# debye model vs langevin
plt.clf()
fig = plt.figure( figsize=(cm2inch(5), cm2inch(4)) )
plt.xticks([])
plt.yticks([])


xx = linspace(1e-5,5,100)
langevin = 15/(5*(xx+1))
debye = 1/(xx+1)
debye[:30] += 1.5
debye[30:70] += 1

plt.xlabel('T')
plt.ylabel('P')
plt.plot(xx, langevin, color=primary, label='Langevin')
plt.plot(xx, debye, color=secondary, label='Debye')
plt.legend(fontsize=7, frameon=False)
plt.savefig('jumps.pdf')

# Debye equations
plt.clf()
fig = plt.figure( figsize=(cm2inch(5), cm2inch(4)) )

ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
plt.xticks([])
plt.yticks([])

xx = linspace(1e-1,10,100)
real = 1+1/(1+xx*xx)
imag = xx/(1+xx*xx)

plt.xlabel('ω')
plt.ylabel('ε')
plt.plot(xx, real, color=primary)
plt.plot(xx, imag, color=secondary)
plt.text(0.1, 1.15, 'ℜ(ε)', fontsize=10, color='gray')
plt.text(0.1, 0.25, 'ℑ(ε)', fontsize=10, color='gray')
#plt.legend(fontsize=7, frameon=False)
plt.savefig('debyeeq.pdf')

# Soft phonons
plt.clf()
fig = plt.figure( figsize=(cm2inch(5), cm2inch(4)) )

ax = plt.gca()
plt.xticks([1],[r'$T_C$'])
plt.yticks([])


plt.xlim(0,3)

xx = linspace(1,3,1000)
ω = sqrt(xx-1)

#plt.xlabel('T')
plt.ylabel(r'$ω_T$')
plt.plot(xx, ω, color=primary)
#plt.legend(fontsize=7, frameon=False)
plt.savefig('softphonon.pdf')

# Landau phase transition
plt.clf()
fig = plt.figure( figsize=(cm2inch(5), cm2inch(4)) )

ax = plt.gca()
plt.xticks([1],[r'$T_C$'])
plt.yticks([])


plt.xlim(0,2)

xx = linspace(0,1,1000)
s_order = sqrt(1-xx)
f_order = +sqrt( 0.5  + 0.5*sqrt(1-4*(xx-1)))

#plt.xlabel('T')
plt.ylabel(r'$P_s$')
plt.plot(xx, s_order, color=primary, label = 'g₄>0')
plt.plot(xx, f_order, color=secondary, label = 'g₄<0')

plt.legend(fontsize=7, frameon=False)
plt.savefig('landau.pdf')

# Exercise 1.4 (like debye equations).
plt.clf()
fig = plt.figure( figsize=(cm2inch(15), cm2inch(8)) )

ax = plt.gca()
# ax.set_xscale('log')
# ax.set_yscale('log')
# plt.xticks([])
# plt.yticks([])

kb = 8.617e-5 #ev/K
ω  = 2*pi*110e3 #Hz
θD = 153 # K
h  = 4.135e-15 # ev/s
ωD = 2*pi*kb*θD/h # Hz
A  = 5
B  = 15
ΔU = 0.4 #eV
def τ(T): return exp(ΔU / kb / T) / ωD

TT = linspace(200,400,1000)
real = [A+A/(1+(ω*τ(T))**2) for T in TT]
imag = [B*ω*τ(T)/(1+(ω*τ(T))**2) for T in TT]

plt.xlabel('T')
plt.ylabel('ε')
plt.plot(TT, real, color=primary)
plt.text(385, 9.3, 'ℜ(ε)', fontsize=10, color='gray')
plt.plot(TT, imag, color=secondary)
plt.text(385, 0.5, 'ℑ(ε)', fontsize=10, color='gray')
plt.savefig('debye_1_4.pdf')

# χ by material
fig = plt.figure( figsize=(cm2inch(5), cm2inch(4)) )
ax = plt.gca()

TC = 2
TN = 1

plt.xticks([TN,TC],[r'$T_N$', r'$T_C$'])
plt.yticks([])

xxall = linspace(1e-5,4,100)
xxrightTC = linspace(TC,4,100)
xxrightTN = linspace(TN,4,100)
xxleftTC = linspace(1e-5,TC,100)
xxleftTN = linspace(1e-5,TN,100)

ax.set_xlabel('T')
ax.set_ylabel('χ')
# Ferromagnetic
ax.plot(xxrightTC, 1.5+1/xxrightTC, color=secondary, label='Ferro')
ax.plot(xxleftTC, 0.5+1/TC + exp(2*(TC-xxleftTC)), color=secondary)

# Paramagnetic
ax.plot(xxall, 1+1/xxall, color=primary, label='Para')

# Antiferromagnetic
ax.plot(xxrightTN, 0.5+1/xxrightTN, color=tertiary, label='Anti')
ax.plot(xxleftTN, -0.5 +1/TN + exp(1*(xxleftTN-TN)), color=tertiary)
ax.set_ylim(0,5)
plt.legend(fontsize=7, frameon=False)
plt.savefig('chicomp.pdf')

# sol graph
fig = plt.figure( figsize=(cm2inch(10), cm2inch(5)) )
ax = plt.gca()

plt.xticks([])
plt.yticks([])

xx = linspace(1e-5,10,100)

approxbrillouin = coth(xx) - 1/xx
lessT = xx/8
theT = xx/3
moreT = xx

ax.set_xlabel(r'$ζ_0$')
ax.set_ylabel(r'$M_S$')

ax.plot(xx, approxbrillouin, color=primary)
ax.plot(xx, lessT, color=secondary)
ax.plot(xx, theT, color=secondary)
ax.plot(xx, moreT, color=secondary)
ax.scatter([6.82], [0.85], color='gray')


plt.text(0.3, 0.85, r'$T>T_C$', fontsize=10, rotation=80, color='gray')
plt.text(1.7, 0.85, r'$T=T_C$', fontsize=10, rotation=62, color='gray')
plt.text(3.6, 0.6, r'$T<T_C$', fontsize=10, rotation=35, color='gray')

ax.set_xlim(0,10)
ax.set_ylim(0,1)

ax.legend([r'$M_S = M_0 B_J(ζ_0)$',
           r'$M_S = \frac{J+1}{3JCλ} T ζ_0$'])

plt.savefig('solgraph.pdf')

# Arrott-Belov
fig = plt.figure( figsize=(cm2inch(5), cm2inch(5)) )
ax = plt.gca()

plt.xticks([])
plt.yticks([])

xx = linspace(0,1,100)

above = 0.2+xx**(1/3)
just = xx
below = xx**(2) - 0.2

ax.set_xlabel('H/M')
ax.set_ylabel('M²')

ax.plot(xx, above, color=primary)
ax.plot(xx, just, color=primary)
ax.plot(xx, below, color=primary)


plt.text(0.5, 0.55, r'$T=T_C$', fontsize=10, rotation=45, color='gray')
plt.text(0.25, 0.85, r'$T<T_C$', fontsize=10, rotation=45, color='gray')
plt.text(0.75, 0.4, r'$T>T_C$', fontsize=10, rotation=60, color='gray')

ax.set_xlim(0,1)
ax.set_ylim(0,1)

plt.savefig('abplot.pdf')


# Magnon disp
fig = plt.figure( figsize=(cm2inch(5), cm2inch(5)) )
ax = plt.gca()

plt.xticks([3.141592],['π/a'])
plt.yticks([])

xx = linspace(0,3.141592,100)
yy = 1-cos(xx)
xx2 = linspace(0,3.141592/2,100)
yy2 = xx2**2 / 2

ax.set_xlabel('k')
ax.set_ylabel('ℏω/4SJ')

ax.plot(xx, yy, color=primary)
ax.plot(xx2, yy2, '--', lw=1,color=primary)

ax.set_xlim(0,3.141592)
ax.set_ylim(0,2.2)

plt.savefig('magnon.pdf')


# RKKY
fig = plt.figure( figsize=(cm2inch(5), cm2inch(5)) )
ax = plt.gca()

plt.xticks([])
plt.yticks([])

xx = linspace(0.0001,20,100)
yy = [(sin(x) - x*cos(x))/x**4 for x in xx]

ax.set_xlabel('ζ')
ax.set_ylabel('F(ζ)')

ax.plot(xx, yy, color=primary)

ax.set_ylim(-0.008, 0.01)

plt.savefig('RKKY.pdf')


# χ by material, with formulae.

TC = 2
TN = 1

xxall = linspace(1e-5,4,100)
xxrightTC = linspace(TC,4,100)
xxrightTN = linspace(TN,4,100)
xxleftTC = linspace(1e-5,TC,100)
xxleftTN = linspace(1e-5,TN,100)

fig = plt.figure( figsize=(cm2inch(11), cm2inch(5)) )
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)


# plt.xticks([TN,TC],[r'$T_N$', r'$T_C$'])
# plt.yticks([])


# Paramagnetic
ax1.plot(xxall, 1+1/xxall, color=primary)
ax1.set_title('Paramagnetismo')
ax1.text(1.75,3.0,r'$χ=\frac{C}{T}$',backgroundcolor='w')
ax1.text(1.75,2.3,'Ley de Curie', backgroundcolor='w')

ax1.set_ylabel('χ')

ax1.set_yticks([])
ax1.set_xticks([])
ax1.set_xlim(0,4)

# Ferromagnetic
ax2.plot(xxrightTC, 1+1/(xxrightTC-TC), color=primary)
ax2.set_title('Ferromagnetismo')
ax2.text(0.50,2.2,r'$χ=\frac{C}{T-T_C}$')
ax2.text(0.50,1.5,'Ley de Curie-Weiss')

#ax2.set_ylabel('χ')

ax2.set_yticks([])
ax2.set_xlabel('T')
ax2.set_xlim(0,4)
ax2.set_xticks([TC])
ax2.set_xticklabels(['$T_C$'])


# Antiferromagnetic
ax3.plot(xxrightTN, 1+1/xxrightTN, color=primary)
ax3.plot(xxleftTN, 1+1/xxleftTN, '--', lw=1, color=primary)
ax3.plot(xxleftTN, 0.5+ -0.5 +1/TN + exp(1*(xxleftTN-TN)), color=primary)

ax3.set_title('Antiferromagnetismo')
ax3.text(1.5,3.7,r'$χ=\frac{C}{T+θ}$')

ax3.set_yticks([])
ax3.set_xticks([0,0.5,TN])
ax3.set_xticklabels(['θ', '0', '$T_N$'])



ax1.set_ylim(1,5)
ax2.set_ylim(1,5)
ax3.set_ylim(1,5)


plt.savefig('susccompare.pdf')


# myass
fig = plt.figure( figsize=(cm2inch(5), cm2inch(5)) )
ax = plt.gca()

ax.set_xticks([1,-1])
ax.set_xticklabels(['V₀','-V₀'])
ax.set_yticks([])

xx = linspace(-2,2,100)
yy = [x-x/abs(x) if abs(x)>1 else 0  for x in xx]

ax.set_xlabel('V')
ax.set_ylabel('I')

ax.plot(xx, yy, color=primary)

plt.savefig('ohmnicmyass.pdf')


# Im(ε) = Q/2
fig = plt.figure( figsize=(cm2inch(5), cm2inch(5)) )
ax = plt.gca()

ax.set_xticks([1])
ax.set_xticklabels(['1/τ'])
ax.set_yticks([])

ax.set_xlim(0,5)
ax.set_ylim(0,1)

xx = linspace(1e-5,5,100)
Q = [x**2/(1+x**2) for x in xx]
I = [x/(1+x**2) for x in xx]

ax.set_xlabel('ω')
ax.set_ylabel('')
ax.plot(xx, Q, label='$Q$')
ax.plot(xx, I, label=r'$\Im(ε)$')
ax.legend(fontsize=7, frameon=False)
fig.savefig('sopainful.pdf')


# Sineplot
fig = plt.figure( figsize=(cm2inch(5), cm2inch(4)) )

plt.xticks([0,3.141592*2], ['0', '2π'])
plt.yticks([])

xx = linspace(0,3.141592*2,100)
yy = sin(xx)**2 * cos(xx)

plt.xlabel('θ')
plt.ylabel(r'$H_x$')
plt.plot(xx, yy, color=primary)
plt.savefig('sineplot.pdf')

# diffract
fig = plt.figure( figsize=(cm2inch(15), cm2inch(7)) )
ax2 = fig.add_subplot(2,1,1)
ax = fig.add_subplot(2,1,2)

up = pd.read_csv('data_up.csv')
down = pd.read_csv('data_down.csv')

ax.plot(down['x'], down['y'])
ax2.plot(up['x'], up['y'])

ax.set_xlim(0,25)
ax2.set_xlim(0,25)

λ = 1.06 # Å
a = 4.43 # Å
def idx2angle(i,j,k,λ,a): return sqrt(i**2+j**2+k**2)*λ/(2*a)

# down
ax.set_ylabel('T=273K')
ax.set_yticks([])

idxsdown = [(1,1,1),(2,0,0),(3,1,1)]
ax.set_xticks([idx2angle(*ζ,λ,a)*360/2/pi for ζ in idxsdown])
ax.set_xticklabels(["(%d,%d,%d)" % (ζ[0],ζ[1],ζ[2]) for ζ in idxsdown])

# Up
ax2.set_ylabel('T=80K')
ax2.set_yticks([])
idxsup = [(1,1,1),(3,3,1),(5,1,1)]
ax2.set_xticks([idx2angle(*ζ,λ,2*a)*360/2/pi for ζ in idxsup])
ax2.set_xticklabels(["(%d,%d,%d)" % (ζ[0],ζ[1],ζ[2]) for ζ in idxsup])

plt.savefig('difract.pdf')

















# XKCD things
plt.xkcd()



fig = plt.figure(figsize=(cm2inch(15), cm2inch(8)) )
ax = fig.add_subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# plt.yticks([])
# ax.set_ylim([-30, 10])

ωω=logspace(13,17,100)

# In units of 1e15 s⁻¹
γ = 1.81e15
ω1 = 2.81e15
Ne_thing =  1.009e31

def Re(ω): return 1 + Ne_thing * (ω1**2-ω**2)/((ω1**2-ω**2)**2+(γ**2)*(ω**2))
def Im(ω): return -Ne_thing *(γ*ω)/((ω1**2-ω**2)**2+(γ**2)*(ω**2))

ax.plot(ωω, [Re(ω) for ω in ωω], color='#6E7B91', label='Real part')
ax.plot(ωω, [Im(ω) for ω in ωω], color='#99A8C8', label='Imaginary part')
ax.set_xscale('log')
ax.set_xticks([])

plt.annotate(
    'CLOSE TO 2.25 AT LOW FREQUENCY',
    xy=(3e13, 2.25), arrowprops=dict(arrowstyle='->'), xytext=(1e14, 3))

plt.annotate(
    'MAXIMUM AROUND THE PETAHERTZ',
    xy=(3e15, -2), arrowprops=dict(arrowstyle='->'), xytext=(1e14, 1))


ax.set_xlabel('LOG FREQUENCY')
ax.set_ylabel("THE 'EPSILON' THING")
ax.set_ylim(-3,3)
ax.legend()

fig.savefig('xkcd12.pdf')
