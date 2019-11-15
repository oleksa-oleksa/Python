import numpy as np
# 1. Code understanding
print([int(1), float(1), str(1)])

print([-0.5*2**4, str(643)[-2]] + [tuple(2*[3]), (6 != 1) == True])
print([2, 3] + [4, 5])

'''
def pmae(X, Y, p=0.5):
    sm = 0
    for n, x in enumerate(X):
        sm += (x - Y[n])
    sm /= (n + 1)
    return tuple([sm**p, p])


X = ('apple', 'banana', 'cherry')
Y = ('kyiw', 'odessa', 'lwiw')

#Y = ([[4, 5], [1, 1]])

pmae(X, Y)
'''

# numpy.arange([start, ]stop, [step, ]dtype=None)
# Values are generated within the half-open interval [start, stop)
# (in other words, the interval including start but excluding stop).
A = np.arange(-2, 10, 4).reshape((1, 3))
print("A:", A)

B = np.arange(-100, 101, 10).reshape((7, 3))
#print(B)
C = np.arange(100, -101, -10).reshape((7, 3))
#print(C)

D = np.array([1, 2, 3])**2
print(D)
D = D[:, None]
print("D:", D)
#D = D.reshape((3))
#print(D)
print(0.5*A + D)
