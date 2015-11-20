#!/usr/bin/env python

# n=1234
def is_msum(n):
  count = 0
  lst = []
  copy_n = n 
  while count < len(str(copy_n)):
    rem = n % 10
    lst.append(rem)
    count += 1
    n = n // 10
    print "intermediate lst = ", lst
    print "count = ", count
    print "n = ", n


  print "final lst = ", lst
  sum = 0
  for item in lst:
    sum += item

  print
  print "sum = ", sum

if __name__ == '__main__':
    num = int(raw_input("Enter your number to be summed : "))
    is_msum(num)

