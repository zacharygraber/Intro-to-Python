import astronomy as astr

def F(m):
    def lbToKg(pnds):
        return pnds * 0.453592
    myWeight = lbToKg(m)
    return (astr.gravitationalConstant * myWeight * astr.earthMass)/(astr.earthDiameter / 2)**2

print("{0:.2f} Newtons.".format(F(143.3)))