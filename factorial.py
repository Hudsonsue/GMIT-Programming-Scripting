# G00219132 Susan Hudson Programming & Scripting
# script defines a function to return factorial of entered integers.
# https://en.wikipedia.org/wiki/Factorial
# for positive integer n! is n multiplied by all positive integars less than it
# example 4! = 4*3*2*1 = 24
# 0! = 1   

def factorial(n):
    """This function returns factorial of positive integar n."""
    """where n = 0 will return 1 as 0! = 1. Where n < 0 returns Invalid argument warning"""
    
    if n == 0:
        return 1
    elif n < 0:
        return print('INVALID ARGUMENT, Positive integars only please!!')
    else:
        return n * factorial (n-1)

n = int(input("Enter a positive integar: "))
print ("the factorial of your integar" ,n, "is", factorial(n))

# Test the function with the following values, 5, 7, 10
# as well as returning the factorial of the entered integar it will return the factorials of 5,7 and 10
print ("the factorial of 5 is:", factorial (5))
print ("the factorial of 7 is:", factorial (7))
print ("the factorial of 10 is:", factorial (10))