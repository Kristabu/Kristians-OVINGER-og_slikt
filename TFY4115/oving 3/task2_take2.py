import numpy as np
import matplotlib.pyplot as plt

m = 0.185 #g
g = 9.81 #m/s**2
S0 = m*g #startkraft
vinkel = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi, 7*np.pi/2, 4*np.pi]
Smax_G = [0.185, 0.240, 0.300, 0.440, 0.600, 0.800, 1.000, 1.100, 1.400]
Smax = np.array(Smax_G)*g
median_mu = 0
delta_mu = 0
mu = [0]

def my_f(theta):
    return np.log((Smax[theta]) / S0)/vinkel[i]

sum = 0
sum_d = 0
delta_mu = 0


for i in range(1, 9):
    #median
    my_t = my_f(i)
    mu.append(my_t*vinkel[i])
    sum += my_t

median_mu = sum/8

for i in range(1, 9):
    delta_mu_t = (my_f(i) - median_mu)**2
    sum_d = delta_mu_t

#standard avvik
delta_mu = 0.0132

#standard feil
delta_median_mu = delta_mu/np.sqrt(8)

#mu med middelverdi og usikkerhet
mu_p = median_mu + delta_mu
mu_n = median_mu - delta_mu


print("median: ", median_mu)
print("delta: ", delta_mu)
print("delta median: ", delta_median_mu)
print(mu_p)
print(mu_n)

plt.title("Plot av friksjon mot vinkel")
plt.xlabel("vinkel(rad)")
plt.plot(vinkel, np.array(vinkel)*median_mu, label="median")
plt.plot(vinkel, np.array(vinkel)*mu_p, "g", label="usikker +")
plt.plot(vinkel, np.array(vinkel)*mu_n, "r", label="usikker -")
plt.plot(vinkel, mu, "bp", label="målepunkt")
plt.legend()
plt.grid()
plt.savefig("TFY4115/oving 3/Plot_av_målepunt.png")
plt.show()
