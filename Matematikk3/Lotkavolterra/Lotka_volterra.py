import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


plt.style.use('_mpl-gallery')

#gitter
x = np.arange(0.1, 4, 0.1)
y = np.arange(0.1, 4, 0.1) 
X, Y = np.meshgrid(x, y)

#lotkavolterrafunksjonen
Z = X + Y - np.log(X)-np.log(Y)

#vektorfeltet
u = X*(1-Y)
v = Y*(X-1)


#numerisk lÃ¸sning
T=20
N=2000
h=T/N

t=np.linspace(0,T,N+1)
x=np.zeros(N+1)
y=np.zeros(N+1)
f=np.zeros(N+1)

#bestander
x[0]=2
y[0]=2
#lotkavolterrafunksjones verdi pÃ¥ trajektorie
f[0]=x[0]+y[0]-np.log(x[0])-np.log(y[0])

for n in range(N):
    x[n+1]=x[n]+h*x[n]*(1-y[n])
    y[n+1]=y[n]+h*y[n]*(x[n+1]-1)
    f[n+1]=x[n]+y[n]-np.log(x[n])-np.log(y[n])

#plotte lotkavolterrafunksjonen
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
plt.savefig("lotkavolterra-1")

#plotte nivÃ¥kurver til lotkavolterrafunksjon
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
plt.savefig("lotkavolterra-2")


#plotte vektorfeltet
fig, ax = plt.subplots(figsize =(14, 8))
ax.quiver(X, Y, u, v, scale=100)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.axis([0, 3, 0, 3])
ax.set_aspect('equal')
plt.plot(x,y)
plt.savefig("lotkavolterra-3")

#bestander mot tid
plt.figure()
plt.plot(t,x)    
plt.plot(t,y)
plt.savefig('lotkavolterra-tid.png')

#fÃ¸rsteintegral mot tid
plt.figure()
plt.plot(t,f)    
plt.savefig('lotkavolterra-integral.png')

#bestander mot hverandre
plt.figure()
plt.plot(x,y)
plt.savefig('lotkavolterra-fase.png')