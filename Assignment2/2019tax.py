#All the work herein is solely mine

#Immediately, I notice that married people pay more tax
#Also, these brackets are absolute, and are not realistic.
#In the real world, you would pay 10% on everything up to $9700, then 12% from $9700 up to $39475, etc

def unmarriedTax(income):
    if income <= 9700:
        return income * 0.1
    elif income <= 39475:
        return income * 0.12
    elif income <= 84200:
        return income * 0.22
    elif income <= 160725:
        return income * 0.24
    elif income <= 204100:
        return income * 0.32
    elif income <= 510300:
        return income * 0.35
    else:
        return income * 0.37


# 2 Finish this function
# Calculates the taxes a married person owes for 2019
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def marriedTax(income):
    if income <= 19400:
        return income * 0.1
    elif income <= 78950:
        return income * 0.12
    elif income <= 168400:
        return income * 0.22
    elif income <= 321450:
        return income * 0.24
    elif income <= 408200:
        return income * 0.32
    elif income <= 612350:
        return income * 0.35
    else:
        return income * 0.37
#TO DO: IMPLMEMENT FUNCTION


# Calculates the taxes an individual owes for 2019
# Input Parameters: amount of income in USD income and marital status Boolean maritalStatus
# Return Value: amount taxes owed (USD)
def tax(income, maritalStatus):
    if maritalStatus:
        return marriedTax(income)
    else:
        return unmarriedTax(income)

if __name__ == "__main__":
    ############################
    #   DATA
    ############################
    UrsalaIncome, UrsalaMarried = 160726, True
    KaiserIncome, KaiserMarried = 501000, True
    ShilahIncome, ShilahMarried = 20, True
    ############################
    #   TESTS
    ############################
    print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
    print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
    print("Shilah owes ", tax(ShilahIncome, ShilahMarried))
    print()
    ############################
    #   DATA
    ############################
    UrsalaIncome,UrsalaMarried = 204099, False
    KaiserIncome, KaiserMarried = 510310, False
    ShilahIncome, ShilahMarried = 9400, False
    ############################
    #   TESTS
    ############################
    print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
    print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
    print("Shilah owes ", tax(ShilahIncome, ShilahMarried))