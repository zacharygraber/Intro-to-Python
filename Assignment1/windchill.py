#returns windchil, given temp and wind speed
def windChill(T,V):
    return 35.74 + (0.6215 * T) - (35.75 * (V ** 0.16)) + (0.4275 * T * (V ** 0.16))

#avoids closing program after 1 pass. Close with ctrl + c, then enter.
while True:

    T = False
    V = False

    while not T or not V:
        try:
            #asks for user input to define temperature in Fahrenheit (T) and wind speed in mph (V)
            T = float(input("Temperature in Degrees Fahrenheit: "))
            V = float(input("Wind Speed in MPH: "))
        except ValueError:
            print("Please enter only decimal or integer values \n")

    #calls the windchill function with user input as parameters and prints the result
    print(windChill(T,V), "\n")