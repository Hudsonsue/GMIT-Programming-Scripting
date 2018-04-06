#problem euler 5
# 22 Feb 2018
# 
#+= adds a number to a variable,
# changing the variable itself in the process (whereas + would not). Similar to this, there are the following that also modifies the variable:

i=2520

for n in range (2,21):
  if i % n == 0:
    continue #stops going through n values when a value of n results in non even division
  else:
      i=i+20
    break
  if  n ==20:
    answer = n
print (answer)  



    