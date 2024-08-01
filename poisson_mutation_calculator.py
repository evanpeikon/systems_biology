import math

def poisson_mutations(k, lambda_):
    P = (lambda_**k * math.exp(-lambda_)) / math.factorial(k)
    return P

# input parameters
k = 10  # Number of mutations whose probability we want to compute
lambda_ = 3.5 # mutation rate 

probability = poisson_mutations(k, lambda_)
print(f"Poisson: The probability of finding exactly {k} mutations is {probability:.4f}")
