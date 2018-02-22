#problem euler 5
# 22 Feb 2018
#
divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n=0
i = 20

while n < len(divisors):
  if i % n == 0:
       i = i
  else:
       i = i+20
print (i)