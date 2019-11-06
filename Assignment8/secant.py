ex_f = lambda x: x**6 - x - 1

def secant(f, x0, x1, tau):
    error = f(x1)*((x1-x0)/(f(x1)-f(x0)))
    x2 = x1 - error
    print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(x0,f(x0),f(x1),x0-x1))
    if abs(error) <= tau:
        pass
    else:
        secant(f, x1, x2, tau)

if __name__ == "__main__":
    secant(ex_f,2.0,1.0,0.0001)