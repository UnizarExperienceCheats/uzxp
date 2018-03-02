# Solution of problem 1.2

from sympy import *
init_printing()
a,x,ω,ω0,γ,e,E,m,t = symbols('a x ω ω_0 γ e E m t', real=True)

# Try a solution on the form ae^iωt

sol = a*exp(I*ω*t)

lhs = m*diff(sol,t,2) + m*γ*diff(sol,t,1) + m*ω0**2*sol

print(latex(lhs.factor()))

solution = (e*E/(lhs / (a*exp(I*ω*t)))).simplify()

# Get the polarizability
α = (e*solution/E).simplify()

print(latex(α))

# Get the ε from Clausius-Mossoti.

ε = symbols('ε', real=False)
N = symbols('N', real=True)
eq = (ε-1)/(ε+2) - 4*pi/3*N*α

ε_solution = solve(eq,ε)[0].simplify()

print(latex(ε_solution))

# Real and imaginary part.

realpart = re(ε_solution).simplify()
imagpart = im(ε_solution).simplify()

print(latex(realpart))
print(latex(imagpart))
