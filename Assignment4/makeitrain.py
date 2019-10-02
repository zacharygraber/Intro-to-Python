#All of the work herein is solely mine
def dollars(x: int or float):
    """
    Takes in a dollar amount
    Returns a list [quarters, dimes, nickels, pennies]
    """
    q = x // 0.25
    x = x % 0.25

    d = x // 0.1
    x = x % 0.1

    n = x // 0.05
    x = x % 0.05

    p = x / 0.01

    return [q, d, n, float("{:1f}".format(p))]

print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.16))

if __name__ == "__main__":
    pass