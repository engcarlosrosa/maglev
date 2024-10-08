# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:40:57 2015

@author: pccb
"""

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace 
from numpy import linalg 
from numpy import multiply 

Bq = 1.67 * 10**5 #campo magnético e carga elétrica do trem

def forca_magnetica(P1,m1,P2):
    R_x = P2[0]-P1[0]
    #R_y = P2[1]-P1[1]
    R = [R_x] #vetor resultante

    r = linalg.norm(R) 
    r_versor = R/r

    F = multiply(Bq * m1  , r_versor)
    return F
    
def func(A,t):
    dxdt = A[0]
    Pt = [A[0],A[1]]
    F12 = forca_magnetica(Pt, m1)
    dVxdt = F12[0] / m1
    return [dxdt, dVxdt]
    

m1 = 5 * 10**4 #kg massa de Jupiter

#Condicões inicias
x0 = 0
Vx0 = 1.5 * 10

A0 = [x0,Vx0]

T = linspace(0,10**9,500)
M = odeint(func,A0,T)
print(M)
F = [0] * 500
plt.figure(figsize=(7,7))
plt.plot(M[:,0], M[:,1],'g')
plt.plot(T, F,'k')
plt.plot(-T, F,'k')
plt.plot(F, T,'k')
plt.plot(F, -T,'k')
plt.axis([min(M[:,0])-0.1, max(M[:,0])+0.1, min(M[:,1])-0.1, max(M[:,1])+0.1])
plt.xlabel('x')
plt.ylabel('y')
plt.show() 
#print(max(M[:,0]))
#print(max(M[:,1]))
plt.plot(T,M[:,0])
plt.show()

X_max = max(M[:,0])
print(X_max)
