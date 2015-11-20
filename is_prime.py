#!/usr/bin/python

def is_prime(x):
    """
    Module to check whether input number
    is prime or not ?
    """

    if x == 1 or x < 2:
        print "Numbers less than two are not Prime numbers."
        return False
    elif x > 1:
      for num in range(2, (x-1)):
        if x % num == 0:
          return False
        else:
          continue
      else:
        return True
  
if __name__ == '__main__':
    n = int(raw_input("Enter your number : "))
    print "Is %s is PRIME : %s" % (n, is_prime(n) )
