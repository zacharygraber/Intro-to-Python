#all of the work herein is solely mine
x = True
y = False
z = 12
a = 10
b = not (x or not (x or y)) and True

#1#################
if b:
    print("Happy")
elif x:
    print("Valentines")
else:
    print("day!")
###################

#2#################
if (z > a) or (2*a > z):
    print("C200")
if not (z > a) or not (2*a > z):
    print("is bliss")
###################

#3#################
if x and y:
    print(a)
###################

#4#################
if (2 > z) or x:
    print("1")
if not ((2 > z) or x) and (2 == 1):
    print("2")
if not ((2 > z) or x) and not (2 == 1) and (y and not x):
    print("3")
if not ((2 > z) or x) and not (2 == 1) and not (y and not x):
    print("4")
###################

#5#################
###################
