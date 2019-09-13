import math
# Task 1: Finish the following four functions

def maxThree(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z

    
def minThree(p1, p2, p3):
    if p1 <= p2 and p1 <= p3:
        return p1
    elif p2 <= p1 and p2 <= p3:
        return p2
    elif p3 <= p1 and p3 <= p2:
        return p3

    
def maxTwoSum(tomato, potato, idaho):
    if tomato <= potato and tomato <= idaho:
        return potato + idaho
    elif potato <= tomato and potato <= idaho:
        return tomato + idaho
    elif idaho <= tomato and idaho <= potato:
        return tomato + potato
    

def minTwoSum(x, y, z):
    if x >= y and x >= z:
        return y + z
    elif y >= x and y >= z:
        return x + z
    elif z >= x and z >= y:
        return x + y
    
    
    
# Task 2: Writing more functions

def circleArea(diam):
    return math.pi * ((diam/2)**2)
    
    
def areaDifference_rect(l1, w1, l2, w2):
    return abs((l1*w1)-(l2*w2))
    
    
def areaDifference_circle(diam1, diam2):
    return abs(circleArea(diam1) - circleArea(diam2))


if __name__ == "__main__":
    print("Max: " + str(maxThree(10,10,10)))
    print("Min: " + str(minThree(3,3,5)))
    print("Sum of Maxes: " + str(maxTwoSum(10,10,10)))
    print("Sum of Mins: " + str(minTwoSum(10,10,10)))
    print("Area: " + str(circleArea(3)))
    print("Area difference rect: " + str(areaDifference_rect(1,2,5,8)))
    print("Area difference circ: " + str(areaDifference_circle(1,2)))