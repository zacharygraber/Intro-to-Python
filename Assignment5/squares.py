#all of the work herein is solely mine

def sq(n: int):
    """
    INPUT size of the square
    OUTPUT prints a square of that size using a coordinate system
    RETURNS None
    """
    if n == 1:
        print("*")
        return

    #creates a square (albeit inefficient) matrix of all zeros of size n
    coords = list()
    for i in range(1,n+1):
        thisRow = []
        for j in range(1,n+1):
            thisRow += [0]
        coords += [thisRow]
    
    #maps 1's to coordinates where * should be printed
    for i in range(len(coords)): #for the index of each row in the matrix...
        if i == 0 or i == n-1: #check to see if it's top or bottom border
            for j in range(len(coords[i])):
                coords[i][j] = 1 #set all items in the row to 1
        else: #handles middle rows
            for j in range(len(coords[i])): #for each item in the row...
                if j == 0 or j == n-1:
                    coords[i][j] = 1

    for i in coords:
        for j in i:
            if j == 1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

if __name__ == "__main__":
    sizes = [0,1,2,3,4,5,6,7,15]
    for i in sizes:
        sq(i)
        print()
