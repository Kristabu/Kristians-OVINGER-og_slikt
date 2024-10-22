import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 500)

#oppgave 3 X: [0, 3* np.pi / 2] -> R**2
#x_1 = np.cos(t)
#x_2 = np.sin(t)

#oppgave 4 X: [0, 2 * np.pi] -> R**2
#x_1 = 2 * np.cos(t)
#x_2 = np.sin(t)

#tangent av 4
#x_1_prikk = -2* np.sin(t)
#x_2_prikk = np.cos(t)

x_1 = t**3
x_2 = t**2

x_1_prikk = 3 * t**2
x_2_prikk = 2 * t

plt.plot(x_1, x_2, "r")
plt.plot(x_1_prikk, x_2_prikk, "g--")
plt.grid()
plt.show()