import sympy as sy
from sympy.abc import *
print(sy.laplace_transform(sy.cos(2*t),t,s))
print(sy.inverse_laplace_transform(1/s,s,t))