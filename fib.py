#!/usr/bin/python


def fibonacci(n):
    a, b = 0, 1
    count = 0
    print "Inital varaibles : "
    print "a : %s" % a
    print "b : %s" % b
    print "Fibonacci Series : "
    while b < n:
        print b
        a, b = b, a+b

if __name__ == "__main__":
    print "Enter the limit of fibonacci elements .. "
    n = int(raw_input("(last number in the series will be lesser than this limit) : " ))
    fibonacci(n)
