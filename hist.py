## This is a code for histograms and stuff
import numpy as np
mu = 80
sigma = 10
x = np.random.normal(mu, sigma, 1000)

print("random normal array mean centered",  x[:10])  

print("mean = ", np.mean(x))
