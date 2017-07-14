fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result

result = filter(lambda x: x % 2 == 0, fib)
print result
print reduce(lambda x,y: x+y, [47, 11, 42, 13])


#reduce
min = lambda a,b: a if (a<b) else b
print reduce(min, [47, 11, 42, 13])
print reduce(lambda x, y: x+y, range(1, 101))

max = lambda a,b: a if (a>b) else b
print reduce(max, [47, 11, 42, 13]) 
print reduce(lambda x, y: x+y, range(1, 101))

import math

def square(values):
	return map(lambda x: x*x, values)
	print square([47, 11, 42, 13])
	
	
def square_root(values):
	return map(lambda x: math.sqrt(x), values)
	print math.sqrt(144, 100, 81, 9)
	
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print Celsius
print Fahrenheit

triplets = []
for x in range(1,30):
	for y in range(x,30):
		for z in range(y,30):
			if x**2 + y**2 == z**2:
				triplets.append((x,y,z))
				
print triplets[0]
first_x, first_y, first_z = triplets[0]


#OR (Quicker)
max_z = 400
#list comprehension
triplets = [(x,y,z) for x in range(1,max_z) for y in range(x,max_z) for z in range(y,max_z) if x**2 + y**2 == z**2]
print triplets

#generator comprehension
triplets = ((x,y,z) for x in range(1,max_z) for y in range(x,max_z) for z in range(y,max_z) if x**2 + y**2 == z**2)
for value in triplets:
	print value,


	

#Generators
def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

x = city_generator()
print x.next()
print x.next()
print x.next()
print x.next()

def fibonacci(n):
    #Fibonacci numbers generator, first n
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5)
#print f.next()
for x in f:
    print x,
print


#Generators in pythagoras
def generate_triplet(n):
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)
					
triplet_generator = generate_triplet(100)
for value in triplet_generator:
	print value,








