def hex_dec(hex):
    result = 0
    cTable = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    for i in range(len(hex)-1,-1,-1):
        if hex[0] in cTable:
            result += (cTable[hex[0]] * 16**i)
        else:
            result += (int(hex[0]) * 16**i)
        hex = hex[1:]
    return result

if __name__ == "__main__":
    hex = input("Hex: ")
    print(hex_dec(hex))