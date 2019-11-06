ex_f = lambda x: x**6 - x - 1
ex_fp= lambda x: 6*(x**5) - 1

def fpa(f):
    h = 0.000001
    return lambda x: (f(x+h)-f(x-h))/(2*h)

def newton(f, fp, x, tau, maxIter):
    def n(x, i, maxIter):
        while f(x) > tau and i < maxIter:
            print("{0} {1:.5f} {2:.5f}".format(i, x, f(x)))
            x = x - f(x)/fp(x)
            i += 1
        if i == maxIter:
            print("number of iterations exceeded...")
        return x
    n(x,0, maxIter)

if __name__ == "__main__":
    #newton(ex_f,ex_fp,1.5,.0001)
    #newton(ex_f,fpa(ex_f),1.5,.0001)
    func = input("Function: ")
    tau = float(input("tau: "))
    x0 = float(input("x0: "))
    iterations = int(input("iterations: "))
    newton(lambda x: eval(func), fpa(lambda x: eval(func)), x0, tau, iterations)
    input("Press any key to continue . . .")