import matplotlib.pyplot as plt
import numpy as np

#gitter
x = np.arange(-20, 20, 1)
y = np.arange(-20, 20, 1) 
X, Y = np.meshgrid(x, y)

#vektorfelt x'(t) = Ax     plot 5     plot 4  plot 3   plot 2     plot 1
u = Y                    #  -X + -Y |   Y   |  -X    |   X -2*Y | 2*X + Y 
v = -X + 2*X             #   X - Y  |   -X  |  -Y    | -2*X + Y | X + 2*Y

#noe muffins med plotsa^

fig, ax = plt.subplots(figsize =(10, 10))
ax.quiver(X, Y, u, v, scale=500)

#optional
#ax.xaxis.set_ticks([])
#ax.yaxis.set_ticks([])
#ax.axis([-5, 5, -5, 5])
#ax.set_aspect('equal')

#plot and save
plt.plot(x,y)
plt.savefig("Matematikk3/Faseportretter/faseplott_6")