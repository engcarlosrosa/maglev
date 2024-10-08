# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:16:49 2015

@author: pccb
"""

__author__ = 'Carlos'
 
from scipy.integrate import odeint
from numpy import linspace
import matplotlib.pyplot as plt
import math 

T = linspace(0,54.5,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=397638.285
m=50000
A=9
o=1.2922
Cd=2.5
def func (L,T):
    x = L[1]
    dxdt = (Fmg-((0.5*o*A*Cd)*x**2))/m
    return[x, dxdt]
    
W = odeint(func, L0, T)
plt.plot( T,W[:,1], "red", label = '0°')
plt.title('Velocidade em função do tempo')
plt.ylabel('Velocidade [ m / s ]')
plt.xlabel('Tempo [ s ]')
plt.legend(loc='upper left')
plt.show()
