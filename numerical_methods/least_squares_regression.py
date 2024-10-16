import numpy as np
import math
import matplotlib.pyplot as plt

def linear_regression(x, y):
    # calculate num of data points, (sigma xi), and (sigma yi)
    n = len(x)
    sumx = sum(x)
    sumy = sum(y)

    # calculate (sigma xi*yi) and (sigma xi^2)
    sumxy = sum(xi * yi for xi, yi in zip(x, y)) # calculate sigma x_i*y_i
    sumx2 = sum(xi ** 2 for xi in x) # calculate sigma x_i^2

    # calculate mean of x and y
    xm = sumx / n
    ym = sumy / n

    # calculate slope (a1) and intercept (a0)
    a1 = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx ** 2)
    a0 = ym - a1 * xm

    # calculate the total sum of squares and the residual sum of squares
    sum_of_squares = sum((yi - ym) ** 2 for yi in y)
    residual_sum_of_squares = sum((yi - (a1 * xi + a0)) ** 2 for xi, yi in zip(x, y))

    # standard error of the estimate
    std_error_of_estimate = np.sqrt(residual_sum_of_squares / (n - 2))

    # calcualte oefficient of determination (r^2) and correlation coefficient
    r2 = (sum_of_squares - residual_sum_of_squares) / sum_of_squares
    r = math.sqrt(r2)

    return a0, a1, std_error_of_estimate, r2, r

# plotting function
def plot_regression(x, y, a0, a1):
    plt.scatter(x, y, color="blue", label="Data points")
    y_pred = [a1 * xi + a0 for xi in x]
    plt.plot(x, y_pred, color="red", label=f"Fit: y = {a1:.2f}x + {a0:.2f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# enter values of x and y and perform linear regression
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 1.5, 2, 3, 4, 5, 8, 10, 13]
a0, a1, std_error_of_estimate, r2, r = linear_regression(x, y)

# print results and plot regression line
print('Slope:', a1)
print('Intercept:', a0)
print('Standard Error of Estimate:', std_error_of_estimate)
print('Correlation Coeffient (r):', r)
print('Coefficient of Determination (r^2):', r2)
plot_regression(x, y, a0, a1)
