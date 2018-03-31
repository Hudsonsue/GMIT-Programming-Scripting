## G00219132 Susan Hudson Programming & Scripting
## script defines a function to return factorial of entered integers.
## https://en.wikipedia.org/wiki/Factorial
## for positive integer n! is n multiplied by all positive integars less than it
## example 4! = 4*3*2*1 = 24
## 0! = 1   

def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial (n-1)

n = int(input("Enter a positive integar: "))
print ("the factorial of your integar is", factorial(n))

# Test the function with the following values, 5, 7, 10
print ("Check script outputs 120 for factorial 5 ---", factorial (5))
print ("Check script outputs 5040 for factorial 7 ---", factorial (7))
print ("Check script outputs 3628800 for factorial 10 ---", factorial (10))