class Car:

    recall = False
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def setRecall(self, b):
        recall = b

    def showCar(self):
        print("Do you like, may car ~")
        print(self.make + " " + self.model + " " + str(self.year))
    
    # def __str__(self):
    #     return self.make + " " + self.model + " " + str(self.year)

zachsCar = Car("VW", "EOS", 2006)
zachsCar.showCar()

secondCar = Car("VW", "EOS", 2006)
print(zachsCar)
print(secondCar)
print(zachsCar == secondCar)
