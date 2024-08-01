import math

def binomial_mutations(k,n,p):
  P = (math.factorial(n) / (math.factorial(k) * math.factorial(n-k))) * (p**k) * ((1-p)**(n-k))
  return P

# input parameters
k = 10  #number of successes (mutations)
n = 1000 #number of trials (DNA bases)
p = 0.0035 #probability of success (mutation rate)

probability = binomial_mutations(k,n,p)
print(f"Binomial: The probability of finding exactly {k} mutations in {n} segments is {probability:.5f}")
