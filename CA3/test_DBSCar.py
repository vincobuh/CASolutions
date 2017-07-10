
#testing the car functionality

import unittest

from car import *
from DBSCarRental import *

class TestCar(unittest.TestCase):

    def test_car_mileage(self):
        self.car = Car()
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())

    def test_car_make(self):
        self.car = Car()
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.car = Car()
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        self.car.setColour('yellow')
        self.assertEqual('yellow', self.car.getColour())

    def test_car_engine_size(self):
        self.car = Car()
        self.assertEqual('', self.car.engineSize)
        self.car.engineSize = '2.0tdi'
        self.assertEqual('2.0tdi', self.car.engineSize)

    def test_electric_car_fuel_cells(self):
		electriccar = ElectricCar()
		self.assertEqual(1, electriccar.getNumberFuelCells())
		electriccar.setNumberFuelCells(4)
		self.assertEqual(4, electriccar.getNumberFuelCells())
		
	def test_petrol_car_cylinders(self):
		petrolcar = PetrolCar()
		self.assertEqual(1, petrolcar.getNumberCylinders())
		petrolcar.setNumberCylinders(4)
		self.assertEqual(4, petrolcar.getNumberCylinders())
		
	def test_diesel_car_litre(self):
		dieselcar = DieselCar()
		self.assertEqual(1, dieselcar.getNumberLitre())
		dieselcar.setNumberLitre(4)
		self.assertEqual(4, dieselcar.getNumberLitre())
		
	def test_hybrid_car_freepiston(self):
		hybridcar = HybridCar()
		self.assertEqual(1, hybridcar.getNumberFreepiston())
		hybridcar.setNumberFreepiston(4)
		self.assertEqual(4, hybridcar.getNumberFreepiston())
	
	def test_make(self):
		cars=[PetrolCar(),DieselCar(),HybridCar(),ElectricCar()]
		carabvs=["P","D","H","E"]
		self.assertEqual(carabvs,[cars[0].getMake(),cars[1].getMake(),cars[2].getMake(),cars[3].getMake()])
		
	def test_currentstock(self):
		stock = Dealership()
		stock.create_current_stock(1,2,3,4)
		self.assertEqual(1,len(stock.petrol_cars))
		self.assertEqual(2,len(stock.diesel_cars))
		self.assertEqual(3,len(stock.hybrid_cars))
		self.assertEqual(4,len(stock.electric_cars))
		
	def test_stockcount(self):
		stockcnt = Dealership()
		stockcnt.create_current_stock(2,3,4,5)
		self.assertEqual([2,3,4,5],stockcnt.stock_count())


if __name__ == '__main__':
    unittest.main()
