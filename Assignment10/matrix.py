import numpy as np

#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):
    # TODO: Implement function
    return 1


#INPUT scalar n and matrix a
#RETURN scalar product na
def sm(n,a):
    # TODO:Implement function
    return 1


#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    # TODO:Implement function
	return 1

#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    # TODO: Implement function
	return 1

if __name__ == "__main__":
    a = np.array([[1,2,4],[3,4,3]])
    b = np.array([[-1,0],[1,-5],[-3,1]])

    print("numpy product\n", np.dot(a,b))
    d = mm(a,b)
    print(d)

    print("numpy scalar product\n", 4*a)
    e = sm(4,a)
    print(e)

    print("numpy tranpose\n", np.transpose(a))
    f = tp(a)
    print(f)

    print("numpy addition\n", a + a)
    g = add_m(a,a)
    print(g)