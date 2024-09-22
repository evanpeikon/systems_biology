def f(x):
    # Define the function for which you're finding the root
    return x**3 - 6 

def ModFalsePos(xl, xu, es, imax):
    # Initialize variables
    iter = 0            # Iteration counter
    xr = xl             # Initial estimate for root
    ea = 100            # Approximate relative error, initialized to a high value
    fl = f(xl)          # Function value at xl
    fu = f(xu)          # Function value at xu
    il = 0              # Counter for the lower bound stagnation
    iu = 0              # Counter for the upper bound stagnation

    # Main loop
    while True:
        xrold = xr  # Store the old estimate of xr
        
        # Compute the new root estimate using the modified false position formula
        xr = xu - fu * (xl - xu) / (fl - fu)
        fr = f(xr)  # Compute function value at xr
        iter += 1   # Increment iteration counter

        # Calculate relative error if xr is not zero
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100

        # Test the product of f(xl) and f(xr)
        test = fl * fr
        if test < 0:
            xu = xr   # Root is in the lower subinterval, update xu
            fu = f(xu)  # Update fu to reflect new xu
            iu = 0     # Reset stagnation counter for upper bound
            il += 1    # Increment stagnation counter for lower bound

            # Modify fl if stagnation occurs at the lower bound
            if il >= 2:
                fl /= 2
        elif test > 0:
            xl = xr   # Root is in the upper subinterval, update xl
            fl = f(xl)  # Update fl to reflect new xl
            il = 0     # Reset stagnation counter for lower bound
            iu += 1    # Increment stagnation counter for upper bound

            # Modify fu if stagnation occurs at the upper bound
            if iu >= 2:
                fu /= 2
        else:
            ea = 0  # Exact root found
        
        # Exit condition: error less than tolerance or max iterations reached
        if ea < es or iter >= imax:
            break

    return xr  # Return the estimated root

# Example usage:
xl = 1         # Lower bound of interval
xu = 3         # Upper bound of interval
es = 0.01      # Desired relative error (%)
imax = 50      # Maximum number of iterations

root = ModFalsePos(xl, xu, es, imax)
print(f"The root is approximately: {root}")
