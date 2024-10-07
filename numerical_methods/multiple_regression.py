def multiple_regression(x1_values, x2_values, y_values, new_x_input, new_y_input):
    # Calculate means
    mean_x1 = sum(x1_values) / float(len(x1_values))
    mean_x2 = sum(x2_values) / float(len(x2_values))
    mean_y = sum(y_values) / float(len(y_values))
    
    # Calculate variances
    var_x1 = sum((x1 - mean_x1) ** 2 for x1 in x1_values)
    var_x2 = sum((x2 - mean_x2) ** 2 for x2 in x2_values)
    
    # Calculate covariance
    covar_x1 = sum((x1_values[i] - mean_x1) * (y_values[i] - mean_y) for i in range(len(x1_values)))
    covar_x2 = sum((x2_values[i] - mean_x2) * (y_values[i] - mean_y) for i in range(len(y_values)))
    
    # Calculate coefficients
    b1 = covar_x1 / var_x1
    b2 = covar_x2 / var_x2
    b0 = mean_y - b1 * mean_x1 - b2 * mean_x2
    
    # Prediction
    y = b0 + b1 * new_x1_input + b2 * new_x2_input
    return y

# Input values and execute function 
x1_values = [0, 2, 2.5, 1, 4, 7]
x2_values = [0, 1, 2, 3, 6, 2]
y_values = [5, 10, 9, 0, 3, 27]
new_x1_input = 5
new_x2_input = 4

solution = multiple_regression(x1_values, x2_values, y_values, new_x1_input, new_x2_input)
print("Predicted y value:", solution)
