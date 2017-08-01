# Program to make a Simple Calculator on R
# That can Add, Subtract, Multiply, Divide, Exponent,
# Squareroot, Cube, Square, Cuberoot and Factorial


Add <- function(num1, num2) {
  return(num1 + num2)
}

Subtract <- function(num1, num2) {
  return(num1 - num2)
}

Multiply <- function(num1, num2) {
  return(num1 * num2)
}

Divide <- function(num1, num2) {
  return(num1 / num2)
}

Exponent <- function(num1, num2) {
   if (num1 == 0 && num2 == 0)
      {return("Error!!")}
   if (num1 == 0)
      {return(0)}
   if (num2 == 0)
      {return(1)}
   else
     {return(num1 ** num2)}
}

Squareroot <- function(num1, num2) {
  if (num2 == 0.5) 
    return(num1 ** 0.5)
  if (num1 < 0)
    return('NaN')
  else 
      return('Error! Please enter(num2 = 0.5)')
}


Cube <- function(num1, num2) {
   if (num2 == 3)
     return(num1 ** num2)
  
   else
     return('Error! Please enter(num2 = 3)')
}


Square  <- function(num1, num2) {
  if (num2 == 2)
    return(num1 ** num2)
  else
    return('Error! Please enter(num2 = 2)')
}
  
Cuberoot <- function(num1, num2) {
   if (num2 == 1/3)
     return(num1 ** num2)
   else
     return('Error! Please enter(num2 = 1/3)')
}

Factorial <- function(num1) {
  if (num1 > 1)
    return(num1 * factorial(num1-1))
  else
    return("Infinity") 
}

#Take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Squareroot")
print("7.Cube")
print("8.Square")
print("9.Cuberoot")
print("10.Factorial, Please enter ONLY num1")
operation = as.integer(readline(prompt="Enter operation[1/2/3/4/5/6/7/8/9/10]: "))

num1 = as.numeric(readline(prompt="Enter first number: "))
num2 = is.numeric(readline(prompt="Enter second number: "))


operator <- switch(operation,"+","-","*","/","**","**","**","**","**","num1 * factorial(num1-1)")
result <- switch(operation, Add(num1, num2), Subtract(num1, num2), Multiply(num1, num2), Divide(num1, num2),
                 Exponent(num1, num2), Squareroot(num1, num2), Cube(num1, num2), Square(num1, num2),
                 Cuberoot(num1, num2), Factorial(num1))

print(paste(num1, operator, num2, "=", result))