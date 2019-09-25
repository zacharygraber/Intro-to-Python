#all of the work herein is solely mine
import math

#1 
def y(d,r,t):
    """
    returns the yield of a deposit with principle (d), compound interest rate (r), and time (t)
    """
    return d * math.exp(r * t)

#2
def N(n_0, m, t):
    return n_0 * math.exp(m * t)

#3
def N_t(t):
    return 71.8 * math.exp(-8.96 * math.exp(-0.0685 * t))

#4
def K(t):
    return ((9 / 2.6) * t) / (2 * (t ** 2) +3)

#5
def r(t):
    return 1.5207 * (t ** 4) - 19.166 * (t ** 3) + 62.91 * (t ** 2) + 6.0726 * t + 1026

#6
def p(x):
    return 4 * (x ** 2) - 100 * x - 1000

#7
def W(P_i,P_f):
    return 8.314 * 300 * math.log((P_i / P_f))

#8
def depreciate(c,s,life):
    return (c - s) / life

#9
def L(k,V,A,C):
    return k * (V **2) * A * C

if __name__=="__main__":
    print(y(1000,.02,10))
    print(N(500,100,4))
    print(math.floor(N_t(1000)))
    print(K(1))
    print(r(4))
    print(p(10))
    print(W(10,1))
    print(depreciate(20000,1000,5))
    print(L(0.0033,33.8,512,0.515))