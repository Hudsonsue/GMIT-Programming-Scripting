#problem euler 5
# 22 Feb 2018
#
#+= adds a number to a variable,
# changing the variable itself in the process (whereas + would not). Similar to this, there are the following that also modifies the variable:

i=0

while True:
  i += 20
  for n in range (2,21):
    if i % n != 0:break
    print (n)
    print(i)
  
  else:
    
    print ("i", i)  
    