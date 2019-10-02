#All of the work herein is solely mine

def f(x,y,z):
    return 11*x*y + 14*y*z + 15*x*z

def vol(x,y,z):
    return x*y*z == 147840

#some arbitrary starting point
a,b,c = 2,2,36960

#TODO Loops seaching through possible values
currentBest = f(a,b,c)
for x in range(0,101):
    for y in range(0,101):
        for z in range(0,101):
            if vol(x,y,z) and f(x,y,z) < currentBest:
                currentBest = f(x,y,z)
                a = x
                b = y
                c = z


print("H W L Value")
print(a,b,c,f(a,b,c))

if __name__ == "__main__":
    pass