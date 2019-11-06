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
    #TODO: IMPLEMENT
    pass

#2
def odd(x):
    #TODO:IMPLEMENT
    pass

#3
#Recursive
#input parameter: n
#OUTPUT RE value
def b(n):
    #TODO: IMPLEMENT
    pass

#4
#TAIL RECURSIVE for function B
def btr(n,s):
    #TODO: IMPLEMENT
    pass

#5 
#MEMOIZATION 
#USE THIS DICTIONARY for function B
d = {2:0,1:0}
def bm(n):
    #TODO: IMPLEMENT
    pass

###################################################

#7
#input parameter: N
#output: Recursive VALUE
#RECURSIVE IMPLMENTATION
def gg(n):
    #TODO: IMPLEMENT
    pass

#8
#TAIL RECURSIVE version of gg
def gtr(n,s):
    #TODO:IMPLEMENT
    pass

#9
# MEMOIZATION DICTIONARY INSIDE version of gg
def gm(n):
    #TODO: IMPLEMENT
    pass

if __name__ == "__main__":

    # Function numbers 1 - 6

    for i in range(1,10): 
        print("f({0}) = {1}, {2}, {3}, {4}".format(i, b(i),btr(i,0),bm(i) ))

    fblist = [b, lambda i: btr(i,0), bm ]
    tlist = [round(ftimer(f,700)*10**5,2) for f in fblist]
    print(tlist)
    print()

    fglist = [gg, lambda i: gtr(i,0),gm]

    # Function numbers 7 - 9 

    for i in range(0,10):
        print("f({0}) = {1}, {2}, {3}, {4}".format(i,gg(i),gtr(i,0),gm(i)))

    tlist = [round(ftimer(f,700)*10**5,2) for f in fglist]
    print(tlist)