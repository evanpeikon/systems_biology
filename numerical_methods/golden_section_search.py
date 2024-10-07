import math

def gold_max(xlow, xhigh, maxit, es, f):
    R = (math.sqrt(5) - 1) / 2  # Golden ratio constant
    iter = 1
    d = R * (xhigh - xlow)
    x1 = xlow + d
    x2 = xhigh - d
    f1 = f(x1)
    f2 = f(x2)
    if f1 > f2:  # Reverse comparison for maximization
        xopt = x1
        fx = f1
    else:
        xopt = x2
        fx = f2
    while True:
        d = R * d
        xint = xhigh - xlow
        if f1 > f2:  # Reverse comparison for maximization
            xlow = x2
            x2 = x1
            x1 = xlow + d
            f2 = f1
            f1 = f(x1)
        else:
            xhigh = x1
            x1 = x2
            x2 = xhigh - d
            f1 = f2
            f2 = f(x2)
        iter += 1
        if f1 > f2:  # Reverse comparison for maximization
            xopt = x1
            fx = f1
        else:
            xopt = x2
            fx = f2
        if xopt != 0:
            ea = (2 - R) * abs(xint - xopt) * 100
        else:
            ea = 100  # To ensure the loop continues if xopt is zero
        # Exit condition: approximate error (ea) < es or maximum iterations reached
        if ea < es or iter >= maxit:
            break
    return xopt, fx

# Example usage with a sample function f(x)
def sample_function(x):
    return 2*math.sin(x) - x**2/10  # Example quadratic function with a maximum at x = 2

xlow = 0
xhigh = 5
maxit = 100
es = 0.01

optimal_x, optimal_fx = gold_max(xlow, xhigh, maxit, es, sample_function)
print(f"Optimal x: {optimal_x}, Maximum f(x): {optimal_fx}")
