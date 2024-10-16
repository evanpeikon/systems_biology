import numpy as np
import math
import matplotlib.pyplot as plt

# define function for 2nd order polynomial regression (fit parabola)
def polynomial_regression(x, y, degree=2):
    # fit polynomial and create polynomial function w/ fitted coefficients
    polynomial = np.poly1d(coefficients)

    # predict y values
    y_predicted = polynomial(x)

    # calculate coefficient of determination (r^2) and correlation coefficient
    y_mean = np.mean(y)
    total_sum_of_squares = sum((yi - y_mean) ** 2 for yi in y)
    residual_sum_of_squares = sum((yi - y_predicted_i) ** 2 for yi, y_predicted_i in zip(y, y_predicted))
    r2 = 1 - (residual_sum_of_squares / total_sum_of_squares)
    r = math.sqrt(r2)

    # standard error of the estimate
    n = len(x)
    std_error_of_estimate = np.sqrt(residual_sum_of_squares / (n - 3))

    return coefficients, std_error_of_estimate, r2, r, polynomial

# plotting function f
def plot_polynomial_regression(x, y, polynomial):
    plt.scatter(x, y, color="blue", label="Data points")
    y_predicted = polynomial(x)
    plt.plot(x, y_predicted, color="red", label="Fitted Parabola")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# enter values of x and y and perform polynomial regression
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 1.5, 2, 3, 4, 5, 8, 10, 13]
coefficients, std_error_of_estimate, r2, r, polynomial = polynomial_regression(x, y)

# print results and plot parabola
print('Polynomial Coefficients:', coefficients)
print('Standard Error of Estimate:', std_error_of_estimate)
print('Correlation coefficient (r):', r)
print('Coefficient of Determination (r^2):', r2)
plot_polynomial_regression(np.array(x), np.array(y), polynomial)
