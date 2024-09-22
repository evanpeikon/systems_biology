# you can learn more about markov chains and how this code works here: https://github.com/evanpeikon/dynamicalsys

import numpy as np
import matplotlib.pyplot as plt

transition_matrix =  np.array([[0.5, 0.4,0.6],[0.2, 0.2, 0.3], [0.3, 0.4, 0.1]])
initial_state = np.array([[0],[1],[0]])
cycles = 50

def markov_model(transition_matrix, initial, cycles):
  state_at_t = []
  state_at_t.append(initial)
  for i in range(0,cycles):
    t = np.dot(transition_matrix, state_at_t[i])
    state_at_t.append(t)
  state_at_t_tuples = [tuple(np.round(array.flatten(), 3)) for array in state_at_t]
  variable_1 = [t[0] for t in state_at_t_tuples]
  variable_2 = [t[1] for t in state_at_t_tuples]
  variable_3 = [t[2] for t in state_at_t_tuples]

  fig, ax = plt.subplots()
  ax.plot(range(len(variable_1)), variable_1, label='Variable 1', marker='o')
  ax.plot(range(len(variable_2)), variable_2, label='Variable 2', marker='o')
  ax.plot(range(len(variable_3)), variable_3, label='Variable 3', marker='o')
  ax.set_xlabel('time(t)')
  ax.set_ylabel('state of the dynamical system (x(t))')
  ax.set_title('State of system as a function of time')
  ax.legend()
  ax.grid(True)
  return fig, ax and state_at_t_tuples

print(markov_model(transition_matrix, initial_state, cycles))
