import numpy as np
import matplotlib.pyplot as plt

def droplet_volume(R0,k,ti,dt):
  # calcualte initial volume
  V0 = (4/3) * np.pi * R0**3

  # set starting values for V, R, t
  V = V0 # starting volume is V0
  R = R0 # starting radius is R0
  t=ti # starting time is ti=0

  # initialize lists to store computed V and t
  volumes = []
  times = []

  # calculate number of steps
  n_steps = int((tf-ti)/dt) # number of time steps

  for i in range(0,n_steps):
    # calculate radius and volume at ea/ time step
    R = ((3*V)/(4 * np.pi))**(1/3)
    V = V + (-k*4*np.pi*R**2) * dt

    # append calculated volume and current time to respective lists
    volumes.append(V)
    times.append(t)

    # increment time up by dt
    t+=dt

  #plot results
  plt.figure(figsize=(8, 6))
  plt.plot(times, volumes)
  plt.title('V=V(t)')
  plt.xlabel('Time (min)')
  plt.ylabel('Volume (mm^3)')
  plt.grid(True)
  plt.show()

  return V # return final volume

# set inputs and parameters
k = 0.08 # evaporation rate (mm/min)
R0 = 2.5 # initial radius (mm)
ti = 0 # starting time (t=0 min)
tf = 10 # finishing end (t=10 min)
dt = 0.25 # step size for time (min)

# execute function and print final computed volume
solution = droplet_volume(R0=R0, k=k, ti=ti, dt=dt)
print('Final Computed Volume:', solution, 'mm^3')
