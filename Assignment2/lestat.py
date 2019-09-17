#Assigning variables to types
Ap, Bp, Op, ABp = "A+", "B+", "O+", "AB+"
An, Bn, On, ABn = "A-", "B-", "O-", "AB-"

#Input: Blood types x and y
#Output: Boolean, x can receive from y
def receiveFrom(x, y):
    if x == Ap:
        return y in (Ap, An, Op, On)
    elif x == Bp:
        return y in (Bp, Bn, Op, On)
    elif x == ABp:
        return True
    elif x == On:
        return y == On
    elif x == Op:
        return y in (Op, On)
    elif x == An:
        return y in (An, On)
    elif x == Bn:
        return y in (Bn, On)
    elif x == ABn:
        return y in (ABn, An, Bn, On)
    else:
        raise NameError("Not a recognized blood type")

#Input: Blood types x and y
#Output: Boolean, x can donate to y
def donateTo(x, y):
    if x == Ap:
        return y in (Ap, Bp)
    elif x == Bp:
        return y in (Bp, ABp)
    elif x == ABp:
        return y == ABp
    elif x == On:
        return True
    elif x == Op:
        return y in (Op, Ap, Bp, ABp)
    elif x == An:
        return y in (An, Ap, ABn, ABp)
    elif x == Bn:
        return y in (Bn, Bp, ABn, ABp)
    elif x == ABn:
        return y in (ABn, ABp)
    else:
        raise NameError("Not a recognized blood type")

#create a list with all blood types in it
x = [Ap, Bp, Op, ABp, An, Bn, On, ABn]


for i in x:
    print(i, " donate to ", end="")
    for j in x:
        if donateTo(i, j):
            print(j, " ", end="")
    print()
print()

for i in x:
    print(i, " receive from ", end="")
    for j in x:
        if receiveFrom(i, j):
            print(j, " ", end="")
    print()