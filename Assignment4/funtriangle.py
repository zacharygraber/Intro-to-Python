#All of the work herein is solely mine

#1st Triangle#################################
for i in range(19):
    print("*" * (-1 * abs((i+1) - 10) + 10))
##############################################

print()
print()

#2nd Triangle#################################
for i in range(10):
    print("*" * int((i+1) * (1 + 0.5*i)))
for i in range(8,0,-1):
    print("*" * int((i+1) * (1 + 0.5*i)))
##############################################

print()
print()

#3rd Triangle#################################
for i in range(11):
    print((" " * i) + ("*" * (21 - 2*i)))
##############################################

if __name__ == "__main__":
    pass