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
'''
#gráfico 1 --- Fmg=397638.285 --- m=32000
T = linspace(0,54.5,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=302918.2849
m=32000
A=9
o=1.2922
Cd=2
def func (L,T):
    x = L[1]
    dxdt = (Fmg)/m
    return[x, dxdt]
    
W = odeint(func, L0, T)
plt.plot( T,W[:,1], "red", label = '0°')
plt.title('Velocidade em função do tempo')
plt.ylabel('Velocidade [ m / s ]')
plt.xlabel('Tempo [ s ]')
plt.legend(loc='upper left')
plt.show()
'''
'''
#gráfico 2 --- Fmg=397638.285 --- m=32000
T = linspace(0,54.5,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=302918.2849
m=32000
A=9
o=1.2922
Cd=2

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

#gráfico 3 --- Fmg=397638.285 --- m=32000
T = linspace(0,54.5,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=302918.2849
m=32000
A=9
o=1.2922
Cd=2
g=10
def func0 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(0)))/m
    return[x, dxdt]

def func3 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(1)))/m
    return[x, dxdt]

def func6 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(2)))/m
    return[x, dxdt]
    
def func9 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(3)))/m
    return[x, dxdt]

def func50 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(4)))/m
    return[x, dxdt]

def func15 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(5)))/m
    return[x, dxdt]



W0 = odeint(func0, L0, T)
W3 = odeint(func3, L0, T)
W6 = odeint(func6, L0, T)
W9 = odeint(func9, L0, T)
W50 = odeint(func50, L0, T)
W15 = odeint(func15, L0, T)
plt.plot( T,W0[:,1],'red', label = '0°')
plt.plot( T,W3[:,1],'green', label = '1°')
plt.plot( T,W6[:,1],'blue', label = '2°')
#plt.plot( T,W9[:,1],'yellow', label = '3°')
#plt.plot( T,W50[:,1],'gray', label = '4°')
#plt.plot( T,W15[:,1],'black', label = '5°')
plt.title('Velocidade do Maglev em diferentes inclinações')
plt.legend(loc='down right')
plt.ylabel('Velocidade [ m / s ]')
plt.xlabel('Tempo [ s ]')
plt.axis([0,60,0,170])
plt.show()
'''
'''
#gráfico 4 --- Fmg=397638.285 --- m=32000
T = linspace(0,54.5,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=302918.2849
m=32000
A=9
o=1.2922
Cd=2
def func (L,T):
    x = L[1]
    dxdt = (Fmg)/m
    return[x, dxdt]
    
W = odeint(func, L0, T)
plt.plot( T,W[:,1], "red", label = '0°')
plt.title('Velocidade em função do tempo')
plt.ylabel('Velocidade [ m / s ]')
plt.xlabel('Tempo [ s ]')
plt.legend(loc='upper left')
plt.show()
'''
#gráfico 5 --- Fmg=397638.285 --- m=32000
T = linspace(0,54.5,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=302918.2849
m=32000
A=9
o=1.2922
Cd=2

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

#gráfico 6 --- Fmg=397638.285 --- m=32000
T = linspace(0,180,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=302918.2849
m=96000
A=9
o=1.2922
Cd=2
g=10
def func0 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(0)))/m
    return[x, dxdt]

def func3 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(math.pi/36)))/m
    return[x, dxdt]

def func6 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(math.pi/18)))/m
    return[x, dxdt]
    
def func9 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(math.pi/10)))/m
    return[x, dxdt]

def func50 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin((math.pi*19)/180)))/m
    return[x, dxdt]

def func15 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m*math.sin(0)))/m
    return[x, dxdt]



W0 = odeint(func0, L0, T)
W3 = odeint(func3, L0, T)
W6 = odeint(func6, L0, T)
W9 = odeint(func9, L0, T)
W50 = odeint(func50, L0, T)
W15 = odeint(func15, L0, T)
plt.plot( T,W0[:,1],'red', label = '0°')
plt.plot( T,W3[:,1],'green', label = '5°')
plt.plot( T,W6[:,1],'blue', label = '10°')
plt.plot( T,W9[:,1],'yellow', label = '18°')
plt.plot( T,W50[:,1],'gray', label = '19°')
#plt.plot( T,W15[:,1],'black', label = '90°')
plt.title('Velocidade do Maglev em diferentes inclinações')
plt.legend(loc='down right')
plt.ylabel('Velocidade [ m / s ]')
plt.xlabel('Tempo [ s ]')
plt.axis([0,180,-40,163])
plt.show()

#gráfico 7 --- Fmg=397638.285 --- m=32000
T = linspace(0,300,201)
# L = [x, vx]
x0 = 0
v0 = 0
L0 = [x0, v0]
 
Fmg=302918.2849
m1=32000        #1vagão
m2=64000        #2vagões
m3=96000        #3vagões
m4=128000       #4vagões
m5=320000       #10vagões
m6=480000       #15vagões
m7=640000       #20vagões
m8=960000       #30vagões
m9=1600000      #50vagões
m10=32000*30    #1000vagões
A=9
o=1.2922
Cd=2
g=10
def funcm1 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m1*math.sin(0)))/m1
    return[x, dxdt]

def funcm2 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m2*math.sin(0)))/m2
    return[x, dxdt]

def funcm3 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m3*math.sin(0)))/m3
    return[x, dxdt]
    
def funcm4 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m4*math.sin(0)))/m4
    return[x, dxdt]

def funcm5 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m5*math.sin(0)))/m5
    return[x, dxdt]

def funcm6 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m6*math.sin(0)))/m6
    return[x, dxdt]

def funcm7 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m7*math.sin(0)))/m7
    return[x, dxdt]

def funcm8 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m8*math.sin(0)))/m8
    return[x, dxdt]
    
def funcm9 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m9*math.sin(0)))/m9
    return[x, dxdt]

def funcm10 (L,T):
    x = L[1]
    dxdt = ((Fmg)-((0.5*o*A*Cd)*x**2)-(g*m10*math.sin(0)))/m10
    return[x, dxdt]


Wm1 = odeint(funcm1, L0, T)
Wm2 = odeint(funcm2, L0, T)
Wm3 = odeint(funcm3, L0, T)
Wm4 = odeint(funcm4, L0, T)
Wm5 = odeint(funcm5, L0, T)
Wm6 = odeint(funcm6, L0, T)
Wm7 = odeint(funcm7, L0, T)
Wm8 = odeint(funcm8, L0, T)
Wm9 = odeint(funcm9, L0, T)
Wm10 = odeint(funcm10, L0, T)
plt.plot( T,Wm1[:,1],'red', label = '1 Vagão')
plt.plot( T,Wm2[:,1],'green', label = '2 Vagões')
plt.plot( T,Wm3[:,1],'blue', label = '3 Vagões')
plt.plot( T,Wm4[:,1],'yellow', label = '4 Vagões')
plt.plot( T,Wm5[:,1],'gray', label = '10 Vagões')
#plt.plot( T,Wm6[:,1],'black', label = '15 Vagões')
#plt.plot( T,Wm7[:,1],'blue', label = '20 Vagões')
#plt.plot( T,Wm8[:,1],'yellow', label = '30 Vagões')
#plt.plot( T,Wm9[:,1],'gray', label = '50 Vagões')
plt.plot( T,Wm10[:,1],'black', label = '40 Vagões')
plt.title('Velocidade do Maglev em numero de vagões')
plt.legend(loc='lower left')
plt.ylabel('Velocidade [ m / s ]')
plt.xlabel('Tempo [ s ]')
plt.axis([0,300,-10,170])
plt.show()

print(math.sin(math.pi/2))