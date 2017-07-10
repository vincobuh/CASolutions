#CA 3 by Titi Badiya 10052625.
#This is a program that allows users to rent and return cars.

from car import *

class Dealership(object):
		
	def __init__(self):
		self.electric_cars = []
		self.petrol_cars = []
		self.diesel_cars = []
		self.hybrid_cars = []
        
#Populating inventory
	
	def current_stock(self): 
		for i in range(5):
			self.electric_cars.append(ElectricCar())
        for i in range(20):
			self.petrol_cars.append(PetrolCar())
		for i in range(8):
			self.diesel_cars.append(DieselCar())
		for i in range(7):
			self.hybrid_cars.append(HybridCar())

#show current stock

    def stock_count(self): 
        print 'Petrol cars in stock ' + str(len(self.petrol_cars))
        print 'Electric cars in stock ' + str(len(self.electric_cars))
		print 'Diesel Cars in stock: ' + str(len(self.diesel_cars))
        print 'Hybrid Cars in stock: ' + str(len(self.hybrid_cars))
	

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
#Providing option for rental

    def process_rental(self): 
                
        wt = raw_input('What type of Car would you like to rent?:\n P-Petrol\n E-Electric\n D-Diesel\n H-hybrid\n: ') 
        num = int(raw_input('How many would you like to rent?: '))
        if wt == 'P':
            self.rent(self.petrol_cars, num)
        elif wt == 'E':
            self.rent(self.electric_cars, num)
        elif wt =='D':
            self.rent(self.diesel_cars, num)
        elif wt =='H':
            self.rent(self.hybrid_cars, num)
        
        self.stock_count()
#Allows cars to be returned to the stock

	def returns(self, car_list, amount): 
        total = 0
        if amount < 0:
            print 'Please insert number 1-40 '
        elif amount == 0:
            print 'Do you wish to extend your lease.'
        else:
            while total < amount:
                car_list.append(1)
                total = total + 1
            print 'Car(s) returned successfully.'

# Shows list of where car should be returned to

	def CarReturn(self):
		enginetype = raw_input("What type of car are you returning?\nElectric - E\nPetrol - P\nHybrid - H\nDiesel - D\n: ")
        numc = int(raw_input('How many cars are you returning?\n: '))
        if type == 'E' and len(self.electric_cars) + numc <= 5:
            self.returns(self.electric_cars, numc)
        elif type == 'P' and len(self.petrol_cars) + numc <= 20:
            self.returns(self.petrol_cars, numc)
        elif type == 'H' and len(self.hybrid_cars) + numc <= 7:
            self.returns(self.hybrid_cars, numc)
        elif type == 'D'and len(self.diesel_cars) +  numc <= 8:
            self.returns(self.diesel_cars, numc)
			
#User section allows user input
	def user(self):
	print 'Welcome to DBS Car Rental. See below cars in-stock:\n'
	print df
	self.stock_count()
	use = raw_input("Do you wish to rent 'R' or return 'RT' a car?\n: ")
    if use == 'R':
		self.process_rental()
	else:
        self.CarReturn()
		
if __name__ == '__main__':
    rent = Dealership()
    rent.current_stock()
    cont = 'Y'
    
    while cont == 'Y':
        try:
            rent.user()
        except:
            print 'Thank you for visiting DBS rentals.'
        cont = raw_input('Do you wish to continue? Y/N: ')
    print "Safe Trip"
