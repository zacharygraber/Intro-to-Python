#change lat,lon to radians
from math import radians, sin, cos, sqrt, asin 

### TODO: Answer Questions in comments here
# dd() computationally simpler than hd(), meaning that it would be faster to compute
# Although dd() is a simpler solution, it is bound to be less accurate than hd()
#
# Calculating Euclidean distance on a noneuclidean plane is bound to introduce
#     tons of error. Such is the quandary of mapping the Earth: how does one 
#     translate a spherical surface to a flat plane? This is why solutions like the 
#     Mercator projection distort the size of land masses near the poles greatly.
#
#     Maybe unbeknowst to each person, he or she remembers and guages distance
#     in a noneuclidean fashion subconsciously.

#INPUT two tuples that have lat, lon values
#RETURN distance in miles
def hd(loc1,loc2):
    r = 3961 # radius in miles
    radloc1 = (radians(loc1[0]), radians(loc1[1]))
    radloc2 = (radians(loc2[0]), radians(loc2[1]))

    latd = (radloc2[0]-radloc1[0]) / 2
    lond = (radloc2[1]-radloc1[1]) / 2
    d0 = (sin(latd) ** 2) + (cos(radloc1[0]) * cos(radloc2[0]) * (sin(lond) ** 2))
    d1 = 2 * r * asin(sqrt(d0))
    # TODO: Implement function based on the formula above
    return d1 # Template return statement


def dd(loc1,loc2):
    """
    Standard distance formula
    """
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    x = lat1 - lat2
    y = (lon1 - lon2)*cos(radians(lat2))
    return 69.385*sqrt(x**2 + y**2)

def eu_distance(loc1,loc2):
    """
    Euclidian Distance Forumula
    """
    return sqrt(sum([(i-j)**2 for i,j in zip(loc1,loc2)]))


if __name__ == "__main__":
    #Lindley Hall where we had C200
    l1 = (39.165341,-86.523588)

    #Luddy Hall the new Luddy building, where we have C200
    l2 = (39.172725,-86.523295)

    #Distance between Lindley and Luddy
    print(hd(l1,l2))
    print(eu_distance(l1,l2))
    print(dd(l1,l2))