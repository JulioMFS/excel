import numpy as np
import pylab as plt

np.random.seed(28)
N = 300
rets = np.random.randn(N)
prices = np.cumsum(rets) + 10
plt.plot(prices);
plt.ylabel("Prices")

