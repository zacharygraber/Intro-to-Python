#all of the work herein is solely mine

def is_magic(ms):
    """
    A magic square is a 2d, square matrix of positive, nonzero integers
    where the sum of every row, column, and diagonal is equal

    INPUT an iterable matrix of nonzero integers
    OUTPUT prints whether or not the square is magic
    RETURN boolean whether or not input is a magic square
    """
    #testing rows
    sumFirstGroup = 0 #since every row, col, and diag is equal, they should all equal the first row tested
    for i in range(len(ms)): #for the index of each row in the square
        sumThisGroup = 0
        for j in ms[i]: #for each item in that row
            sumThisGroup += j
        if not i: #if it's the first row
            sumFirstGroup = sumThisGroup
        elif sumThisGroup != sumFirstGroup:
            print("This is not a magic Square...hide")
            return False
    
    #testing columns
    for i in range(len(ms)): #gets a range the size of the square
        sumThisGroup = 0
        for j in range(len(ms)): #gets another identical range
            sumThisGroup += ms[j][i]
        if sumThisGroup != sumFirstGroup:
            print("This is not a magic Square...hide")
            return False
    
    #for any given size of magic square, there are only 2 diagonals
    #so we can just test both individually against the already known sumFirstGroup
    sumThisGroup = 0
    for i in range(len(ms)): #gets a range the size of the square
        sumThisGroup += ms[i][i] #the first diagonal has coordinates (0,0) (1,1) (2,2) (3,3) (4,4) etc.
    if sumThisGroup != sumFirstGroup:
        print("This is not a magic Square...hide")
        return False
    
    sumThisGroup = 0
    for i in range(len(ms)):
        sumThisGroup += ms[i][len(ms)-1]
    if sumThisGroup != sumFirstGroup:
        print("This is not a magic Square...hide")
        return False
    
    print("This is a magic Square")
    

if __name__ == "__main__":
    ms = [[4, 9, 2],[3,5,7],[8,1,6]]
    is_magic(ms)

    ms = [[4, 9, 2],[3,5,7],[8,2,6]]
    is_magic(ms)

    ms = [[18,1,12],[4,6,9],[3,36,2]]
    is_magic(ms)

    ms = [[8,11,14,1],[13,2,7,12],[3,16,9,6],[10,5,4,15]]
    is_magic(ms)
