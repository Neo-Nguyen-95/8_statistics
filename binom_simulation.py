import numpy as np
import pandas as pd

# Parameters
n_trials = 10
p_success = 0.4
n_iter = 1000

results = np.random.binomial(n_trials, p_success, n_iter)

# Analyze the result
unique, counts = np.unique(results, return_counts=True)
result_summary = dict(zip(unique, [counts]))

print(pd.DataFrame(result_summary))