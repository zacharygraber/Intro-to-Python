#All of the work herein is solely mine

def roman(n):
    """
    Input a decimal integer n
    Return a string containing the Roman numeral representation of n
    """

    hundreds = "C" * (n // 100)
    n = n % 100

    fifties = "L" * (n // 50)
    n = n % 50

    tens = "X" * (n // 10)
    n = n % 10

    fives = "V" * (n // 5)
    n = n % 5

    ones = "I" * (n // 1)
    
    if len(str(tens)) > 3:
        if fifties:
            tens = "XC"
            fifties = ""
        elif not fifties:
            tens = "XL"


    if ones == "IIII":
        if fives:
            ones = "IX"
            fives = ""
        elif not fives:
            ones = "IV"

    return hundreds + fifties + tens + fives + ones

if __name__ == "__main__":
    
    for i in range(1,100):
        if i % 5 == 0:
            print()
        print(i, roman(i), ", ", end="")

    print("195", roman(195))