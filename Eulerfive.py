#problem euler 5
# 22 Feb 2018
# 
#+= adds a number to a variable,
# changing the variable itself in the process (whereas + would not). Similar to this, there are the following that also modifies the variable:

i=0

while True:  #continues looping until 
  i = 2520 #+= is incrementing by 20 each time it loops, has to be divisible by 20 so no point smaller increments
  for n in range (2,21):
    if i % n != 0:break #stops going through n values when a value of n results in non even division
    i=i+20
    print (n) #temp to check it is looping correctly
    print(i) #temp to check it is looping correctly#temp
  else:    
    print ("i", i)  

    