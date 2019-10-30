import math
#all of the work herein is solely that of me, Zachary E. Graber

#s(n), as tested using an unbounded incrementing loop, can
#be passed any integer, where -1<n<998, thus demonstrating that Python
#has a recursion limit of 1,000 times

#calculating p(30) takes several minutes on my modern (i7) laptop,
#simply because the number of stack frames created for p(n) is (2**n)-1.
#This means that to calculate p(30), the function ends up calling itself
#1,073,741,824 times.

#b(n) is a recursive version of the Fibonacci sequence, where 
#the sequence starts at 2, and n is just a 1-based index to a 
#sequence value

def s(n):
    """
    Sums a positive or zero integer.
    """
    
    if n == 0:
        return 0
    else:
        return n + s(n-1)

def s1(n):
    """
    Non-recursive version of s(n)
    """
    return (n * (n+1)) / 2

def p(n):
    """
    From finance.
    """
    if n == 0:
        return 10000
    else:
        return p(n-1) + 0.02*p(n-1)

def p1(n):
    return (1.02**n) * 10000

def b(n):
    #This function is a recursive version of the Fibonacci sequence,
    #where the sequence starts at 2, and n is just a 1-based index to a 
    #sequence value
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return b(n-1) + b(n-2)

def c(n):
    if n == 1:
        return 9
    else:
        return 9*c(n-1) + 10**(n-1) - c(n-1)

def d(n):
    if n == 0:
        return 1
    else:
        return 3*d(n-1) + 1

def d1(n):
    return (3**(n+1)-1) / 2

def c18(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return c18(n-1,k) + c18(n-1,k-1)

#FOR TESTING#############################################################
def c17(n,m):
    return math.factorial(n) / (math.factorial(n-m) * math.factorial(m))

def c19(n,k):
    numerator = n
    for i in range(1,k):
        numerator *= (n-i)
    return numerator / math.factorial(k)
#########################################################################

def B(n):
    if n == 0:
        return 1
    else:
        def 
        return (-1 * sumNot) / (1 + n)
        

if __name__ == "__main__":
    # for i in range(1,10):
    #     print("~"*40)
    #     print(f"s({i}): ",s(i))
    #     print(f"s1({i}): ",int(s1(i)))
    #     print()
    #     print(f"p({i}): ",p(i))
    #     print(f"p1({i}): ",p1(i))
    #     print()
    #     print(f"b({i}): ",b(i))
    #     print()
    #     print(f"c({i}): ",c(i))
    #     print()
    #     print(f"d({i}): ",d(i))
    #     print(f"d1({i}): ",int(d1(i)))

    #TESTING RECURSION DEPTH
    # i = 1
    # while True:
    #     print(i,s(i))
    #     i += 1

    print(B(1))
    print(c17(2,0))