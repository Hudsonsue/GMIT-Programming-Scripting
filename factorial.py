## G00219132 Susan Hudson Programming & Scripting
## script defines a function to return factorial of entered integers.
## https://en.wikipedia.org/wiki/Factorial

def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial (n-1)

n = int(input("Enter an integar: "))
print ("the factorial of your integar is", factorial(n))
