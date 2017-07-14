import math

def sum(a, b):
    return map(lambda x, y: x + y, a, b)
    
def subtract(values):
    return reduce(lambda x, y: x-y, values)
    
def multiply(values):
    return reduce(lambda x, y: x*y, values)
    
def divide(a, b):
    return map(lambda x, y: x/float(y) if y != 0 else 'error', a, b)

def power(values):
    return reduce(lambda x, y: x**float(y), values)
    
def sqrt(a):
	return map(lambda x: x ** (1/2.0), a)
    
def is_even(values):
	return filter(lambda x: x%2 == 0, values)
	
def fizzbuzz(values): 
    return filter(lambda x: x%3==0 and x%5==0, values)
    
def pythagorean(n):#as generator
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

pyt = pythagorean(50)
for v in pyt:
    print 'Pythagorean as generator\n', v,

#as list comprehension
pythagorean = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]	
print 'Pythagorean as list comprehension: \n', pythagorean


#tests
print 'Sum: ', sum([15, 7, 47, 5], [45, 34, 12, 1])
print 'Subtract: ', subtract([20, 76, 8])
print 'Multiply: ', multiply([2, 4, 6])
print 'Division: ', divide([2, 4,6], [3, 5, 0])
print 'Power: ', power([3, 3, 2])
print 'Square root: ', sqrt([2, 3, 4, 5]) 
print 'Even Values: ', is_even([20, 10, 5, 33, 98])
print 'FizzBuzz: ', fizzbuzz([15, 34, 30, 100, 9, 20, 60])

################################################################################################################################################
##########################################
#       Calculator Functions
##########################################

# Function1: add two lists together using Lambda and Map
# each element of list1 will be added to the corresponding element of list2
def add_lists(list1, list2):
    return map(lambda x, y: x+y, list1, list2)

# Function2: subtract two lists using Lambda and Map
# each element of list2 will be subtracted from the corresponding element of list1
def subtract_lists(list1, list2):
    return map(lambda x, y: x-y, list1, list2)

# Function3: divide two lists using Lambda and Map
# each element of list1 will be divided by the corresponding element of list2
def divide_lists(list1,list2):
    return map(lambda x, y: x/float(y) if y!= 0 else 'nan', list1, list2)

# Function4a: calculator function to multiply two numbers
def multiply(first, second):
    number_types = (int, long, float, complex)
    if isinstance(first, number_types) and isinstance(second, number_types):
        return first * second
    else:
         return 'error'
        
# Function4b: Adapt the above function to work with lists using Map
# each element of list1 will be multiplied by the corresponding element of list2
def multiply_list(list1, list2): 
    return map(multiply, list1, list2)

# Function5: get the total of a list using Reduce
# every element of the list will be summed to get an overall total
def list_total(mylist):
    return reduce(lambda x, y: x+y, mylist)

# Function6: return the positive values in a list using Filter
def get_positive_vals(mylist):
    return filter(lambda x: x>0, mylist)

# Function7: return a list of squares using List Comprehension
def get_squares(mylist):
    return [ x**2 for x in mylist ]

# Function8: return a list of leap years using List Comprehension
# a leap year is identified as one that either divides evenly by 400
# OR it divides evenly by 4 but not by 100
def get_leapyears(mylist):
    return [ x for x in mylist if ((x%400==0) or (x%4==0 and x%100!=0)) ]

# Function9: generator to return a list of leap years given a start & end year
# a leap year is identified as one that either divides evenly by 400
# OR it divides evenly by 4 but not by 100
def generate_leapyears(start, end):
    for year in range(start, end+1):
        if ((year%400==0) or (year%4==0 and year%100!=0)):
            yield year   

# Function10: generate a list of squares given a list of numbers
def generate_squares(mylist):
    for x in mylist:
        yield x**2
            
##########################################
#               Calls
##########################################

print add_lists([2,5,4],[2,3,0])
print subtract_lists([2,5,4,3],[2,3,0,4])
print divide_lists([1,2,3],[2,1,0])

print multiply_list([2,5,4,3],[2,3,0,4])
print multiply_list([2,5,4,3],['mary',3,0,4])

print list_total([2,5,4,3,-6,999])
print list_total(range(1,101))

print get_positive_vals([-10,-66,999,0,2])
print get_squares([2,5,4,-2])
print get_leapyears([1600,1700,1800,1900,2000, 1992])

leaps = generate_leapyears(1900,2000)
for year in leaps:
    print year,
print

squares = generate_squares(range(1,100))
for num in squares:
    print num,
