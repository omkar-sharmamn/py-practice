#!/usr/bin/env python

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return factorial(x-1) * x

if __name__ == '__main__':
    number = int(raw_input("Enter your number to get its factorial : "))
    print "Factorial of %s is %s." % (number, factorial(number) )
