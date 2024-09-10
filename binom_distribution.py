import numpy as np
from scipy.stats import binom

# Parameters
n = 6  # Number of trials
p = 0.4  # Probability of success
k = np.arange(0, n+1)  # Number of success

# Generate a binomial distribution
binom_pmf = binom.pmf(k, n, p)  # Probability of mass function

print(binom_pmf)
