import numpy as np
import matplotlib.pyplot as plt

system_rules =  np.array([[0.75, 0.15],[0.25, 0.85]])
initial_state = np.array([[0.4],[0.6]])
cycles = 100

def dynamical_system_generator(system_rules, initial, cycles):
  state_at_t = [] #state at time t, aka x(t)
  state_at_t.append(initial)
  for i in range(0,cycles):
    t_plus_1 = np.dot(system_rules,state_at_t[i])
    state_at_t.append(t_plus_1)
  state_at_t_tuples = [tuple(np.round(array.flatten(), 3)) for array in state_at_t]

  variable_1 = [t[0] for t in state_at_t_tuples]
  variable_2 = [t[1] for t in state_at_t_tuples]

    # Create a scatter plot
  fig, ax = plt.subplots()
  ax.plot(range(len(variable_1)), variable_1, label='Variable 1', marker='o')
  ax.plot(range(len(variable_2)), variable_2, label='Variable 2', marker='o')
  ax.set_xlabel('time(t)')
  ax.set_ylabel('state of the dynamical system (x(t))')
  ax.set_title('State of system as a function of time')
  ax.legend()
  ax.grid(True)
  return fig, ax and state_at_t_tuples

print(dynamical_system_generator(dynamical_system, initial_state, cycles))
