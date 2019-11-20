import csv
import matplotlib.pyplot as plt
import numpy as np

filename = "Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"

def myMean(x,*y):
        return (x + sum(y)) / (1 + len(y))

def worst_county(year):
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
    def get_county_hist(state, county):
        with open(filename, newline="") as f:
            csvReader = csv.reader(f)
            countydata = [[],[]] #female, male
            statedata = [[],[]]
            natdata = [[],[]]
            for row in csvReader:
                if row[0] == state and row[1] == county:
                    countydata[0] += [float(row[4])]
                    countydata[1] += [float(row[7])]
                    statedata[0] += [float(row[6])]
                    statedata[1] += [float(row[9])]
                    natdata[0] += [float(row[5])]
                    natdata[1] += [float(row[8])]
        return (countydata,statedata,natdata)

    countydata, statedata, natdata = get_county_hist(state, county)
    years = np.arange(1985, 2011)

    #### https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
    plt.plot(years, countydata[0], label="Female (County)", color="red")
    plt.plot(years, statedata[0], label="Female (State)", color="red", ls="--")
    plt.plot(years, natdata[0], label="Female (National)", color="red", ls=":")

    plt.plot(years, countydata[1], label="Male (County)", color="blue")
    plt.plot(years, statedata[1], label="Male (State)", color="blue", ls="--")
    plt.plot(years, natdata[1], label="Male (National)", color="blue", ls=":")

    plt.title("{0}, {1}: Life Expectancy".format(county, state))
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (Years)")
    plt.grid(True)
    plt.legend()
    plt.savefig(fname=(f"Life/{state}_{county}.png").replace(" ",""))
    pass



if __name__ == "__main__":
    state, county = worst_county(2010)
    print(state, county)
    plotdata(state, county)