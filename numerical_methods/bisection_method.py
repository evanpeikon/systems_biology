def mathematical_function(x):
  # Define function for which you're finding root below
  return x**3 - 6

def bisection_method(a, b, es, max_iterations):
    iterations = 0 #initialize iteration counter
    midpoints = [0,] #initialize list of midpoints

    for i in range(0,max_iterations):
      c = (a + b) / 2  # Calculate new midpoint
      midpoints.append(c) # Add c to midpoints list
      fa = mathematical_function(a) # Function value at a
      fc = mathematical_function(c) # Function value at c
      evaluator = fa*fc 

      if evaluator < 0:
        b = c  # Root is in lower half, update upper bound
      elif evaluator > 0:
        a = c  # Root is in upper half, update lower bound
      else:
        break # Root identified

      iterations +=1 # increment iteration counter

      ea = abs((midpoints[i+1]-midpoints[i])/midpoints[i+1])*100
      if ea < es: # when ea<es, terminate computation
        break

    return c  # Return the estimated root

# Input parameters
a = 1  # Lower bound of interval
b = 3  # Upper bound of interval
es = 0.1 #
max_iterations = 100 # Maximum number of iterations

root = bisection_method(a, b,es, max_iterations)
print(f"The root is approximately: {root}")
