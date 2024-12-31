import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Model parameters
b = 0.5  # Birth rate of prey
p = 0.3  # Predation rate
r = 0.5  # Predator reproduction rate per prey consumed
d = 0.1  # Death rate of predators

D0 = 20  # Initial prey population
L0 = 20  # Initial predator population

t = np.linspace(0, 1000, 1000)  # Time range for simulation

def deriv(y, t, b, p, r, d):
    D, L = y
    dDdt = b * D - p * D * L
    dLdt = r * D * L - d * L
    return dDdt, dLdt

# Initial conditions
y0 = D0, L0

# Solve differential equations
ret = odeint(deriv, y0, t, args=(b, p, r, d))
D, L = ret.T

# Plot the results
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, D, 'b', alpha=0.5, lw=2, label='Deers')
ax.plot(t, L, 'r', alpha=0.5, lw=2, label='Lions')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Population (thousands)')
ax.set_ylim(0, 20)
ax.grid(which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
plt.show()
