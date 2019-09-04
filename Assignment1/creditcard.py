#only two functions are needed, so there is no need for the whole math library
from math import log10
from math import ceil

#prevents the program from terminating after a single pass. Close with ctrl + c, then enter.
while True:

    #define variables for use in error handling
    APR = False
    C = False
    p = False
    i = False

    #user input and error handling. Gives a message and reprompts user if improper characters are submitted
    while not APR:
        try:
            APR = float(input("What is your APR: %"))
            i = (APR/100)/12
        except ValueError:
            print("Please enter only decimal or integer characters! \n")

    while not C:
        try:
            C = float(input("What is the amount owed on the credit card: $"))
        except ValueError:
            print("Please enter only decimal or integer characters! \n")

    while not p:
        try:
            p = float(input("What is the monthly payment made: $"))
        except ValueError:
            print("Please enter only decimal or integer characters! \n")
    
    i = (APR/100)/12

    #calculate the number of payments to be made
    n = (-1 * (log10(1 - (i * C / p)))) / (log10(i + 1))

    print("You'll make ", ceil(n), " payments.\n")