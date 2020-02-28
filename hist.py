## This is a code for histograms and stuff
import numpy as np
import matplotlib.pyplot as plt

mu = 80
sigma = 10
x = np.random.normal(mu, sigma, 1000)

print("random normal array mean centered",  x[:10])  

print("mean = ", np.mean(x))

plt.hist(x)
plt.show()

print("I'm done")
