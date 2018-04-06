# problem euler 5
#G00219132 Susan Hudson
#https://projecteuler.net/problem=5
# 22 Feb 2018 --finally finished 06 Apr 2018
# 
# This proved the most challenging of the problems set. There are so many possible approaches it 
# became almost impossible. Many defined LCM/GCD but although I could (eventually) understand them
# I wanted a solution that was more logic than maths! 
# below if derived from various solutions in the project Euler discussion forums and stack overflow
# my personal challenge being to understand every line of code and to get there through as much trial and
# error as I could. I still don't get why it was so hard!!

i=2520 ##as already know 2520 lcm of 1-10 can start at 2520

while True:  #keeps going until both loops 'end'
  for n in range (2,21):  
    if i % n == 0:  # if remainder of i/n is 0 it is evenly divisible
      continue #if even division moves to next n in range
    else:
      i=i+20 #if not evenly divisible moves onto next value of i, increments of 20 as highest number want it evenly divided by
      break #stops going through n values when a value of n results in non even division
  if  n ==20: #if n gets to 20 it will already have been evenly divisible for all numbers to 20 so must be result!
    result = i #answer is the value of i when n gets to 20
    break  ##stop loop
print (result) ## as no longer in loops print answer  
