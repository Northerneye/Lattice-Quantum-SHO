import vegas
import math
import matplotlib.pyplot as plt

global t
t = 0

def f(x):
    global t
    a = .5
    N = 8
    m = 1

    dx2 = 0.
    x[0] = t
    for d in range(N):
        dx2 += (m/(2*a)*(x[(d+1)%N] - x[d])**2 + a*.5*(x[d])**2)
    return math.exp(-dx2)/1000

myResults = []
fullResults = []
for x in range(10):
    integ = vegas.Integrator(8*[[-5,5]])
    result = integ(f, nitn=100, neval=20000)
    #print(result.summary())
    print("t = "+str(t))
    print('result = %s    Q = %.2f' % (result, result.Q))
    myResults.append(float(str(result)[:len(str(result))-4]))
    actual = (math.exp(-t**2/2)/math.pi**.25)**2*math.exp(-.5*4)
    fullResults.append(actual)
    print('actual '+str(actual))
    print("")
    t += .2

plt.plot([0,.2,.4,.6,.8,1,1.2,1.4,1.6,1.8], myResults, 'go')
plt.plot([0,.2,.4,.6,.8,1,1.2,1.4,1.6,1.8], fullResults, '--')
plt.show()
