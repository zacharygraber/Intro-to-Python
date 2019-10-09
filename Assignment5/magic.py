#all of the work herein is solely mine
def magic(x):
    """
    INPUT some integer
    OUTPUT the result of the magical encantation
    """
    x += 15 #add 15 to the number (x+15)
    x *= 3 #multiply it by 3 (3(x+15))
    x -= 9 #subtract 9 (3(x+15) - 9)
    x /= 3 #divide it by 3 ((x+15) - 3) = (x + 12)
    x -= 12 #subtract 12 (x + 12 - 12 = x)

    #Essentially all that happens is you add 15 then subtract it.
    return x

if __name__ == "__main__":
    x = int(input("Pick any positive whole number: "))

    print("Your number was", magic(x))