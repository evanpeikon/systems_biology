import math

def fmaxsimp(x1, xu, f, tol=1e-6):
    # Constants
    phi = (1 + math.sqrt(5)) / 2  # Golden ratio
    rho = 2 - phi  # Inverse of the golden ratio
    # Initial guesses
    u = x1 + rho * (xu - x1)
    v = u
    w = u
    x = u
    # Function evaluations at u
    fx = f(u)
    fv = fx
    fw = fx
    # Midpoint of the current interval
    xm = 0.5 * (x1 + xu)
    # Step size and previous step size
    d = 0
    e = 0
    while abs(x - xm) > tol:  # Main loop
        para = abs(e) > tol
        if para:  # Parabolic fit logic
            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            s = 2 * (q - r)
            if s > 0:
                p = -p
            s = abs(s)
            # Check if parabola is acceptable
            if abs(p) < abs(0.5 * s * e) and p > s * (x1 - x) and p < s * (xu - x):
                e = d
                d = p / s
            else:
                para = False
        if not para:  # Golden section step
            if x >= xm:
                e = x1 - x
            else:
                e = xu - x
            d = rho * e
        u = x + d
        fu = f(u)
        if fu >= fx:  # Change condition for maximization
            if u >= x:
                x1 = x
            else:
                xu = x
            v = w
            fv = fw
            w = x
            fw = fx
            x = u
            fx = fu
        else:
            if u < x:
                x1 = u
            else:
                xu = u
            if fu >= fw or w == x:
                v = w
                fv = fw
                w = u
                fw = fu
            elif fu >= fv or v == x or v == w:
                v = u
                fv = fu
        # Update midpoint
        xm = 0.5 * (x1 + xu)
    return x, fx  # Return the maximum point and function value

# Example usage with a function to maximize
def sample_function(x):
    return 2*math.sin(x) - x**2/10  # Inverted quadratic, maximum at x = 2

x1 = 0
xu = 5
maximum_x, maximum_fx = fmaxsimp(x1, xu, sample_function)

print(f"Maximum x: {maximum_x}, Maximum f(x): {maximum_fx}")
