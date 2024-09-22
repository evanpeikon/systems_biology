# the eulers_method function takes an ODE, initial x and y values (x0 and y0), step size (t) and number of steps (n_steps). 
def eulers_method(ODE, x0, y0, t, n_steps):
  xn = x0 # set starting x value to x0
  yn = y0 # set starting y value to y0
  for i in range(0,n_steps): 
    yn = yn + t * ODE(xn, yn) # new y value is previous y value plus product of step size (t) and function with previous x and y values as inputs
    xn = xn + t  # increment x value by step size (t)
  return yn # return final y value

# use the ODE function to define an ordinary differential equation in dy/dx = f(x,y) form
def ODE(x,y):
  return 3*x**2 - y**2 + 1 # write equation in f(x,y) form here. Example, f(x,y) = 3x^2 - y^ 2 +1

solution = eulers_method(ODE=ODE, x0=0, y0=2, t=0.1, n_steps=10) # input choice of x0, y0, t, and n_steps. ODE=ODE by default since it's assumed you inputted your own equation in the ODE function above. 
print(solution)
