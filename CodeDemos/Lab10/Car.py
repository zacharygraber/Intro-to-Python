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

# zachsCar = Car("VW", "EOS", 2006)
# zachsCar.showCar()

# secondCar = Car("VW", "EOS", 2006)
# print(zachsCar)
# print(secondCar)
# print(zachsCar == secondCar)

# # print(zachsCar.recall)
# # print(secondCar.recall)
# # print(id(zachsCar.recall) == id(secondCar.recall))

# # zachsCar.recall = True
# # print(zachsCar.recall)
# # print(secondCar.recall)

# # Car.recall = True
# # print(zachsCar.recall)
# # print(secondCar.recall)

# Car.setRecall(True)
# print(zachsCar.recall)

myCar = Car("Chevy", "Malibu", 2003)
print("\nTESTING BLUETOOTH \n" + "~"*50)
print(myCar.bluetoothOn)
myCar.setBluetoothOn(True)
print(myCar.bluetoothOn)

print("\nTESTING ACCELERATE \n" + "~"*50)
myCar.startCar()
print(myCar.speed)
myCar.accelerate(30)
print(myCar.speed)
myCar.accelerate(5)
print(myCar.speed)

print("\nTESTING BRAKES \n" + "~"*50)
myCar.brake()
print(myCar.speed)

print("\nTESTING RUNFOR \n" + "~"*50)
print(myCar.mileage)
myCar.runFor(4)
print(myCar.mileage)
myCar.accelerate(60)
myCar.runFor(10)
print(myCar.mileage)

print("\nTESTING ISSTOPPED \n" + "~"*50)
print(myCar.isStopped())
myCar.brake()
print(myCar.isStopped())

print("\nTESTING BLUETOOTH \n" + "~"*50)