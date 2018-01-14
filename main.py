import matplotlib.pyplot as plt
import numpy
#import sklearn

#EXERCICE 1
mu = 10
sigma = 2
n = 100

beta0 = 1
beta1 = -2

x = numpy.random.normal(mu, sigma, n)
epsi = numpy.random.normal(0, 1, n)
y = beta0 + (beta1 * x) + epsi

plt.scatter(x,y)
# plt.show()

#EXERCICE 2
def avg(x):
    total = 0
    for i in x:
        total = total + i
    return total/len(x)

print(avg(x))

def var(x):
    total = 0
    av = avg(x)
    for i in x:
        total = total + (i-av)*(i-av)
    return total/len(x-1)

print(var(x))
print(numpy.var(x))

def covar(x, y):
    total = 0
    avx = avg(x)
    avy = avg(y)
    for i, j in zip(x, y):
        total = total + ((i-avx)*(i-avy))
    return total/len(x)

print(covar(x, y))
print(numpy.cov(x, y))

#EXERCICE 3

x[0] = -100
y[0] = 0

