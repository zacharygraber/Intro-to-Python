#TIMER FUNCTION -- deprecated in 3.8 FYI
#so you might get messages -- you can ignore them for now
import time

def ftimer(f,args):
    time_start = time.clock()
    f(args)
    time_elapsed2 = (time.clock()-time_start)
    return time_elapsed2

#1
def even(x):
    return not (x % 2)

#2
def odd(x):
    return bool(x % 2)

#3
#Recursive
#input parameter: n
#OUTPUT RE value
def b(n):
    if n == 1 or n == 2:
        return 0
    elif even(n):
        return n - 1 + b(n - 1)
    else:
        return n**2 + 1 + b(n - 1)

#4
#TAIL RECURSIVE for function B
def btr(n,s):
    if n == 1 or n == 2:
        return s
    elif even(n):
        return btr(n - 1, s + n - 1)
    else:
        return btr(n - 1, s + n**2 + 1)
#5 
#MEMOIZATION 
#USE THIS DICTIONARY for function B
d = {2:0,1:0}
def bm(n):
    if n == 1 or n == 2:
        return d[n]
    elif even(n):
        if n in d:
            return d[n]
        else:
            d[n] = n - 1 + b(n - 1)
            return d[n]
    else:
        if n in d:
            return d[n]
        else:
            d[n] = n**2 + 1 + b(n - 1)
            return d[n]

###################################################

#7
#input parameter: N
#output: Recursive VALUE
#RECURSIVE IMPLMENTATION
def gg(n):
    if n == 0:
        return 1
    else:
        return 1 + 2*gg(n - 1)

#8
#TAIL RECURSIVE version of gg
def gtr(n,s):
    if n == 0:
        return s
    else:
        return gtr(n - 1, s * 2 + 1)

#9
# MEMOIZATION DICTIONARY INSIDE version of gg
def gm(n):
    memo = {0:1} #I'm not sure why the dict is asked for inside the function, since that defeats the purpose of memoization
    if n == 0:
        return memo[n]
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = 1 + 2*gm(n - 1)
            return memo[n]

if __name__ == "__main__":

    # Function numbers 1 - 6

    for i in range(1,10): 
        print("f({0}) = {1}, {2}, {3}".format(i, b(i),btr(i,0),bm(i) ))

    fblist = [b, lambda i: btr(i,0), bm ]
    tlist = [round(ftimer(f,700)*10**5,2) for f in fblist]
    print(tlist)
    print()

    fglist = [gg, lambda i: gtr(i,0),gm]

    # Function numbers 7 - 9 

    for i in range(0,10):
        print("f({0}) = {1}, {2}, {3}".format(i,gg(i),gtr(i,1),gm(i)))

    tlist = [round(ftimer(f,700)*10**5,2) for f in fglist]
    print(tlist)