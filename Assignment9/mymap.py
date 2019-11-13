import gmplot

#create map Showalter Location
gmap = gmplot.GoogleMapPlotter(39.168451, -86.51891, 15)

#Lindley Hall
l1 = (39.165341, -86.523588)

#Luddy Hall
l2 = (39.172725, -86.523295)

#MAC
l3 = (39.166732, -86.517582)

#List of points
lats = [i[0] for i in (l1,l2,l3)]
lons = [i[1] for i in (l1,l2,l3)]

#add points to map
gmap.scatter(lats, lons, "red", size=30, marker = False)
#add line
gmap.plot(lats, lons, "cornflowerblue", size = 30, marker = False)
#save to map
gmap.draw("Assignment9/hellobloomington.html")