# the runge_kutta_RK4 function takes an ODE, initial x and y values (x0 and y0), step size (t) and number of steps (n_steps) as input.
def runge_kutta_RK4(ODE, x0, y0, t, n_steps):
  xn = x0  #set starting x value to x0
  yn = y0 # set starting x value to y0
  for i in range(0,n_steps):
    k1 = t * ODE(xn,yn) # calcualte intermediate slope k1
    k2 = t * ODE((xn+(t/2)), (yn+(k1/2))) # calcualte intermediate slope k2
    k3 = t * ODE((xn+(t/2)),(yn+(k2/2))) # calcualte intermediate slope k3
    k4 = t * ODE((xn+t),(yn+k3)) # calcualte intermediate slope k4
    yn = yn + (1/6)*(k1+2*k2+3*k3+k4) # new y value is previous y value plus weighted average of slopes k1-k4
    xn = xn + t # increment x value by step size (t)
  return yn # return final y value

# use the ODE function to define an ordinary differential equation in dy/dx = f(x,y) form
def ODE(x,y):
  return 3*x**2 - y**2 + 1 # write equation in f(x,y) form here. Example, f(x,y) = 3x^2 - y^ 2 +1

solution = runge_kutta_RK4(ODE=ODE, x0=0, y0=2, t=0.1, n_steps=10) # input choice of x0, y0, t, and n_steps. ODE=ODE by default since it's assumed you inputted your own equation in the ODE function above. 
print(solution)
