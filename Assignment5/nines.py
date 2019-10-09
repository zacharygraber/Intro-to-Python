#all of the work herein is solely mine

def div_9(n):
    while n > 9:
        digitSum = 0
        for  i in str(n):
            digitSum += int(i)
        n = digitSum
    if not n == 0:
        return n == 9
    return True

if __name__ == "__main__":
    x = [99,0,18273645,22,14572,954,17000000,99999999]
    for i in x:
        print(div_9(i))

