# Susan Hudson Collatz exercise
# week 3 exercise programming & scripting
# Collatz: https://en.wikipedia.org/wiki/Collatz_conjecture
# the exercise was completed by reference to lecture videos and the Python tutorial https://docs.python.org/3/tutorial/


n = int(input("enter an integer: "))

print ("The integer entered is",n)
print ("The collatz sequence of",n,"is")

while n >1:
    if n % 2 == 0:
            n = n / 2  
    else:
           n = n* 3 + 1
    print (int (n))