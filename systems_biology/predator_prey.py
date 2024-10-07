import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# model parameters
b = 0.5; p = 0.3; r = 0.5;  d = 0.1
D0 = 20;
L0 = 20;

# initial time and populations
t = np.linspace(0, 1000, 1000)

def deriv(y, t, b, p,r,d):
    D, L = y
    
    dDdt = b*D-p*D*L 
    dLdt = r*D*L-d*L
    return dDdt, dLdt

# Initial conditions vector
y0 = D0, L0
# Integrate the  equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(b,p,r,d))
#ret = odeint(deriv, y0, t, args=(N, beta, gamma))
D,L = ret.T


# Plot the results    
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, D, 'b', alpha=0.5, lw=2, label='Deers')
ax.plot(t, L, 'r', alpha=0.5, lw=2, label='Lions')
ax.set_xlabel('days')
ax.set_ylabel('Number of individual (1000s)')
ax.set_ylim(0,20.0)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
