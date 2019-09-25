#all of the work herein is solely mine
import math

#DATA
#All data in $/oz
Gold = 1503.35       #up 11.0
Silver = 17.91       #up 0.47
Platinum = 950.60    #down 2.50
Palladium = 1468.82  #down 10.48

Au, Ag, Pl, Pa = "Au", "Ag", "Pl", "Pa"

account = 100000 #$100,000 in cash assets
Au_amt, Ag_amt, Pl_amt, Pa_amt = 0, 0, 0, 0

#Input Nothing
#Return amount of money you have and amount of prec metals
def holdings():
    print("Your current holdings")
    print("Account    = {0:.2f}".format(account))
    print("Gold       = ", Au_amt)
    print("Silver     = ", Ag_amt)
    print("Platinum   = ", Pl_amt)
    print("Palladium  = ", Pa_amt)
    print()


#Input metal type
#Return price of that metal in $/oz
def metalPrice(metal):
    if metal == Au:
        return Gold
    elif metal == Ag:
        return Silver
    elif metal == Pl:
        return Platinum
    elif metal == Pa:
        return Palladium
    else:
        raise NameError

#Input metal and amount in oz to purchase
#Return cost of the amount purchasing
def preciousMetalToDollars(metal, amt):
    return metalPrice(metal) * amt

#Input metal and amt to purchase
#If can afford, add metal to holdings and subtract dollar value from acct
#Otherwise tell can't afford
def purchase(metal, amt):
    global account
    global Au_amt
    global Ag_amt
    global Pl_amt
    global Pa_amt

    cost = preciousMetalToDollars(metal, amt)

    if cost >= account:
        print("You have insufficient funds for this purchase.")
    else:
        account -= cost

        if metal == Au:
            Au_amt += amt
        elif metal == Ag:
            Ag_amt += amt
        elif metal == Pl:
            Pl_amt += amt
        elif metal == Pa:
            Pa_amt += amt
            
        print("You have purchased " + str(amt) + " oz. of " + str(metal) + " for $" + "{:0.2f}".format(cost))
        print("You have $" + "{:0.2f}".format(account) + " remaining in your account.")

if __name__ == "__main__":
    holdings()

    print("{:0.2f}".format(preciousMetalToDollars(Au,4)))
    print("{:0.2f}".format(preciousMetalToDollars(Ag,100)))
    print("{:0.2f}".format(preciousMetalToDollars(Pa,23)))
    print("{:0.2f}".format(preciousMetalToDollars(Pl,17)))

    print()
    purchase(Au,4)
    purchase(Ag,100)
    purchase(Pa,23)
    purchase(Pl,17)
    print()

    holdings()

    purchase(Pl, 100000)