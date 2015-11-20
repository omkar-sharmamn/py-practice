#!/usr/bin/python

prime = []
def gen_prime(n):
    for item in range(0, n):
        is_prime(item)
                          
def is_prime(num):
    if num <= 0 or num == 1:
        print "%s : Numbers below 2 are not prime numbers" % num
    else:
        for item in range(2, num):      
            if num % item == 0:
                #print "%s : Not a prime Number" % num
                return False
        else:
            #print "%s : is a prime Number" % num
            prime.append(num)
            return True, prime

if __name__ == '__main__':
    limit = int(raw_input("Enter the limit of prime numbers to be generated : "))    
    print
    gen_prime(limit)
    print 
    print "Prime Numbers : "
    for item in prime: print item 
