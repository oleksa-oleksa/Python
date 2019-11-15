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
#print(D)
D = D[:, None]
print("D:", D)
#D = D.reshape((3))
#print(D)
print(0.5*A + D)

D2 = dict([(0, 1), ('1', 2), ('2', 6), (3, 6), (.1, 10)])
print(D2)
res = 0
for k in D2:
    if type(k) == str:
        res += int(k)
        #print(int(k))
    elif type(k) == int:
        res += D2[k]
        #print(D2[k])
    else:
        res /= len(D2)
        print("else")
        #print(len(D2))
    print("k:", k)
    print("res:", res)


class Bernoulli():
    def fit(self, X):
        self.D = {1: 'Yes', 0: 'No'}
        conv = lambda x: 1 if x == 'H' else 0
        res = [conv(x) for x in X]
        self.p = sum(res) / len(res)
    def info(self):
        dec = False
        if self.p < 0.6 and self.p > 0.4:
            dec = True
        return f"The coin is fair: {self.D[int(dec)]} with p value equal {self.p:.3f}"


B = Bernoulli()
B.fit(['H', 'H', 'H', 'T', 'H', 'T', 'T', 'H', 'T', 'T'])
print(B.info())

