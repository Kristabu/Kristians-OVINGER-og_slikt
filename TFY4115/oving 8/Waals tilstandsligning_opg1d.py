R = 8.31
V = 24 * 10**(-5) #m^3
a = 0.1368 #Pa(m^3/mol)^2
b = 0.0000367 #(m^3/mol)
T = 293 #kelvin

p = ((R*T)/(V - b)) - (a/V**2) #Pa

p_atm = p*10**(-5) #atm

print(p_atm)