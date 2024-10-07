import numpy as np

def newton_interpolation(x, y, n, xi):
    # Initialize the divided differences table (n+1 x n+1 matrix)
    fdd = np.zeros((n + 1, n + 1))
    
    # Set the first column of divided differences to the values of y
    for i in range(n + 1):
        fdd[i, 0] = y[i]
    
    # Calculate the divided differences
    for j in range(1, n + 1):
        for i in range(n - j + 1):
            fdd[i, j] = (fdd[i + 1, j - 1] - fdd[i, j - 1]) / (x[i + j] - x[i])
    
    # Initialize interpolation variables
    yint = fdd[0, 0]  # Starting value of the interpolated result
    xterm = 1  # Term for (xi - x_k) product
    ea = np.zeros(n)  # To store the error approximations at each order

    # Perform interpolation and compute the error approximation at each step
    for order in range(1, n + 1):
        xterm *= (xi - x[order - 1])
        yint_new = yint + fdd[0, order] * xterm
        ea[order - 1] = yint_new - yint  # Error approximation
        yint = yint_new  # Update the interpolated value
    
    return yint, ea

# Example usage
x = np.array([x0, x1, x2, ..., xn])  # Array of known x-values
y = np.array([y0, y1, y2, ..., yn])  # Array of corresponding y-values
xi = some_value  # The x-value to interpolate at
n = len(x) - 1  # Degree of the polynomial

# Get the interpolated result and error approximations
yint, ea = newton_interpolation(x, y, n, xi)
