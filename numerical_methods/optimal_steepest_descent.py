import numpy as np
from scipy.optimize import minimize_scalar

# Step 1: Define the problem equation f(x,y) and the partial derivatives with respect to x and y
def problem_equation(x, y):
  return -8*x + x**2 + 12*y + 4*y**2 - 2*x*y

# Step 2: Define the parial derivatives with respect to x (af_ax) and y (af_ay)
def af_ax(x,y):
  return -8 + 2*x - 2*y

def af_ay(x,y):
  return 12 + 8*y - 2*x

# Step 3: Construct the gradient ∇f|_(x_0,y_0)
def construct_gradient(x,y):
  return np.array([af_ax(x, y), af_ay(x, y)])
  
# Step 4: Find point on line defined by the gradient x(h) and y(h)
def x_h(x_0, gradient_x, h):
  return x_0 - h * gradient_x

def y_h(y_0, gradient_y, h):
  return y_0 - h * gradient_y

# Step 5: Compute g(h) = f(x(h), y(h)) 
def g_h(h, x_0, y_0, gradient_x, gradient_y):
  return problem_equation(x_h(x_0, gradient_x, h), y_h(y_0, gradient_y, h))

# Step 6: Compute the optimal step size h*
def compute_optimal_h(x_0, y_0, gradient_x, gradient_y):
  result = minimize_scalar(g_h, args=(x_0, y_0, gradient_x, gradient_y))
  return result.x

# Step 7: Perform one iteration of optimal steepest descent
def optimal_steepest_descent(x_0, y_0):
  gradient = construct_gradient(x_0, y_0)
  gradient_x = gradient[0]
  gradient_y = gradient[1]
  optimal_h = compute_optimal_h(x_0, y_0, gradient_x, gradient_y)
  x_1 = x_h(x_0, gradient_x, optimal_h)
  y_1 = y_h(y_0, gradient_y, optimal_h)
  return x_1, y_1

## Set initial point (x_0, y_0)
x_0 = 0
y_0 = 0
## Perform steepest descent
solution = optimal_steepest_descent(x_0, y_0)
print('(x1,y1)=', solution)
