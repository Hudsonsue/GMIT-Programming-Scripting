# Adapted from a program created by Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# it also introduced the ord function

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Hudson"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Week 1 Exercise
# my name is Susan, so the first and last letter of my name (S+N = 19+14)
# give the number 33, Fibonacci number is 3524578

#Week 2 Exercise
# My surname is Hudson
# The first letter H is number 72
# The last letter n is number 110
# Fibonacci number 182 is 48558529144435440119720805669229197641
# Ord() is returning the unicode value of the characters specified --in my case H and n. 
