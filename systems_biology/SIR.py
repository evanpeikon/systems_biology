import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Set initial values S_0, I_0, and R_0
initial_values = [990, 10, 0]

# set paramter values for r_b, r_s, r_I, r_R, r_D
parameters = {"r_B": 3.0, "r_S": 0.01, "r_I":0.0005, "r_R":0.05, "r_D":0.02}

# create time grid
time_grid = np.linspace(0, 350, 350) # 0-100 seconds w/ 100 increments (1/sec)

# create function to model infectious diseases
def infectious_disease_model(q, time_grid, r_B, r_S, r_I, r_R, r_D):
  S_0, I_0, R_0 = q

  dSdt = r_B + r_S*R_0 - r_I*S_0*I_0
  dIdt = r_I*S_0*I_0 - r_R*I_0 - r_D*I_0
  dRdt = r_R*I_0 - r_S*R_0

  return dSdt, dIdt, dRdt

# solve ordinary differential equations
solution = odeint(infectious_disease_model, initial_values, time_grid, args=(parameters['r_B'], parameters['r_S'], parameters['r_I'], parameters['r_R'], parameters['r_D']))
S_0, I_0, R_0 = solution.T

# plot results
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(facecolor='#dddddd', axisbelow=True)
ax.plot(time_grid, S_0, alpha=1.0, lw=2, label='I')
ax.plot(time_grid, I_0, alpha=1.0, lw=2, label='I')
ax.plot(time_grid, R_0, alpha=1.0, lw=2, label='R')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration')
ax.grid(True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
plt.show()
