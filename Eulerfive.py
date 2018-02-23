#problem euler 5
# 22 Feb 2018
#

i = 2520
while i > 9:  
  for n in range (2,21):
    if i % n != 0:
      print(n)
      i = i+20
    else:
      print (i)   
  print ("i", i)