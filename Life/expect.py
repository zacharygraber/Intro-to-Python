import csv
import matplotlib as plt
import numpy as np

filename = "Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"

def worst_county(year):
    def myMean(x,*y):
        return (x + sum(y)) / (1 + len(y))
    with open(filename, newline='') as f:
        csvReader = csv.reader(f) #https://docs.python.org/3/library/csv.html
        csvReader.__next__() # skip the first row (headings)
        firstThing = csvReader.__next__()
        currMin = myMean(float(firstThing[4]),float(firstThing[7])) #start with the first value

        for row in csvReader:
            if int(row[3]) == year:
                countyMean = myMean(float(row[4]),float(row[7]))
                if countyMean < currMin:
                    currMin = countyMean
                    minCounty = (row[0],row[1])
    return minCounty

def plotdata(state, county):
    pass

if __name__ == "__main__":
    # state, county = worst_county(2010)
    # plotdata(state,county)
    print(worst_county(2010))