import matplotlib.pyplot as plt
import numpy
#import sklearn

mu = 10
sigma = 2
n = 100

beta0 = 1
beta1 = -2

x = numpy.random.normal(mu, sigma, n)
epsi = numpy.random.normal(0, 1, n)
y = beta0 + (beta1 * x) + epsi

plt.scatter(x,y)
plt.show()
