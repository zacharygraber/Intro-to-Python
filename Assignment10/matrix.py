import numpy as np

#INPUT two matrices a,b
#RETURN product ab
def mm(a,b):
    ans = np.zeros((a.shape[0],b.shape[1]))
    for row in range(ans.shape[0]):
        for column in range(ans.shape[1]):
            dp = []
            for i in range(a.shape[1]):
                dp += [a[row][i] * b[i][column]]
            ans[row][column] = sum(dp)
    return ans


#INPUT scalar n and matrix a
#RETURN scalar product na
def sm(n,a):
    ans = np.zeros(a.shape)
    for row in range(a.shape[0]):
        for column in range(a.shape[1]):
            ans[row][column] = a[row][column] * n
    return ans


#INPUT matrix n x m
#RETURN transpose matrix m x n
def tp(a):
    ans = np.zeros((a.shape[1],a.shape[0]))
    for i in range(0,a.shape[0]):
        for j in range(0,a.shape[1]):
            ans[j][i] = a[i][j]
    return ans

#INPUT two matrices a,b
#RETURN sum a + b
def add_m(a,b):
    s = np.zeros(a.shape)
    for row in range(0,a.shape[0]):
        for column in range(0,a.shape[1]):
            s[row][column] = a[row][column] + b[row][column]
    return s

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