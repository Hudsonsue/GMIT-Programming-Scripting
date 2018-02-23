#problem euler 5
# 22 Feb 2018
#

i = 20
while i > 19:  
  for n in range (2,21):
    if i % n != 0:
      print(n)
  i = i+20
  print ("i", i)