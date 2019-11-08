class Car:

    recall = False
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.bluetoothOn = False
        self.mileage = 0
    
    @staticmethod
    def setRecall(b):
        Car.recall = b

    def showCar(self):
        print("Do you like, my car ~")
        print(self)
    
    def getName(self):
        return self.make + " " + self.model

    def startCar(self):
        self.speed = 0
    
    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)
    
    def setBluetoothOn(self, boolean):
        self.bluetoothOn = boolean
    
    def accelerate(self, speed):
        self.speed += speed
    
    def brake(self):
        self.speed = 0
    
    def runFor(self, time):
        self.mileage += (time * self.speed)
    
    def isStopped(self):
        return not self.speed
    
    def getMileage(self):
        return self.mileage

zachsCar = Car("VW", "EOS", 2006)
zachsCar.showCar()

secondCar = Car("VW", "EOS", 2006)
print(zachsCar)
print(secondCar)
print(zachsCar == secondCar)

# print(zachsCar.recall)
# print(secondCar.recall)
# print(id(zachsCar.recall) == id(secondCar.recall))

# zachsCar.recall = True
# print(zachsCar.recall)
# print(secondCar.recall)

# Car.recall = True
# print(zachsCar.recall)
# print(secondCar.recall)

Car.setRecall(True)
print(zachsCar.recall)
