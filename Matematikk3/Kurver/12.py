import numpy as np
import matplotlib.pyplot as plt

n = 100
t = np.linspace(-1, 1, n)

x_1 = t**3
x_2 = t**2

dx_1 = 3*t**2
dx_2 = 2*t

plt.title("Plott av kurven")
plt.plot(x_1, x_2, label = "x(t)")
plt.ylabel("x_2")
plt.xlabel("x_1")
plt.legend()
plt.grid()
plt.savefig("Matematikk3\Kurver\opg12_plott.png")
plt.show()
