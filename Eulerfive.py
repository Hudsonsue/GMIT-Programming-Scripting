#problem euler 5
# 22 Feb 2018
#

i= 0
while i>=0:
  for n in range (2,11):
    if i % n != 0:break
    else:
      i=i+20
  print ("i", i)