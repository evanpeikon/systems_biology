import numpy as np

def linear_regression(x, y):
    n = len(x)  # Number of data points
    sumx = sum(x)
    sumy = sum(y)
    sumxy = sum(xi * yi for xi, yi in zip(x, y))
    sumx2 = sum(xi ** 2 for xi in x)
    
    xm = sumx / n  # Mean of x
    ym = sumy / n  # Mean of y

    # Calculate slope (a1) and intercept (a0) of the linear regression
    a1 = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx ** 2)
    a0 = ym - a1 * xm

    # Calculate the total sum of squares (ST) and the residual sum of squares (SR)
    st = sum((yi - ym) ** 2 for yi in y)  # Total sum of squares
    sr = sum((yi - (a1 * xi + a0)) ** 2 for xi, yi in zip(x, y))  # Residual sum of squares

    # Standard error of the estimate (syx)
    syx = np.sqrt(sr / (n - 2))

    # Coefficient of determination (r²)
    r2 = (st - sr) / st

    return a0, a1, syx, r2

# Example usage:
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
a0, a1, syx, r2 = linear_regression(x, y)

print(f"Intercept (a0): {a0}")
print(f"Slope (a1): {a1}")
print(f"Standard Error (syx): {syx}")
print(f"R-squared (r²): {r2}")
