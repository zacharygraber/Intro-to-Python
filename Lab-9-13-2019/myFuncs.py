def addition(x,y):
    return x+y

def subtraction(y,x):
    return y-x

def multiplication(v1,v2):
    return v1*v2

def division(tomato, potato):
    return tomato / potato

def testFunc(doing, val1, val2, result):
    return doing + " " + str(val1) + " and " + str(val2) + " produces " + str(result)

if __name__ == "__main__":
    v1 = 1
    v2 = 2
    v3 = 5
    v4 = -1
    v5 = 0
    v6 = 8

    a1 = addition(v1,v2)
    print(a1)

    print("Adding " + str(v1) + " and " + str(v2) + " produces " + str(a1))
    print(testFunc("adding", v6, v2, addition(v6,v2)))
