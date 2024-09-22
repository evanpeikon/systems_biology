def g(x):
    # Define the function g(x) used for fixed-point iteration
    return (x**2 + 3) / 5  # Example: g(x) = (x^2 + 3) / 5

def Fixpt(x0, es, imax):
    xr = x0          # Initial guess
    iter = 0         # Iteration counter
    ea = 100         # Approximate relative error initialized to a high value

    # Main loop
    while True:
        xrold = xr                  # Store old root estimate
        xr = g(xrold)               # Perform fixed-point iteration
        iter += 1                   # Increment iteration count

        # Calculate approximate relative error if xr is not zero
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100

        # Check if error is below tolerance or max iterations reached
        if ea < es or iter >= imax:
            break

    return xr  # Return the estimated root

# Example usage:
x0 = 1         # Initial guess
es = 0.01      # Desired relative error (%)
imax = 50      # Maximum number of iterations

root = Fixpt(x0, es, imax)
print(f"The fixed point is approximately: {root}")
