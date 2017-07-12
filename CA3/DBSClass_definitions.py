# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage


class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberLitre = 1

    def getNumberLitre(self):
        return self.__numberLitre

    def setNumberLitre(self, value):
        self.__numberLitre = value
		
class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberFreepiston = 1

    def getNumberFreepiston(self):
        return self.__numberFreepiston

    def setNumberFreepiston(self, value):
        self.__numberFreepiston = value
		
		
