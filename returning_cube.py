# a module is a file that contains definitions - including variables and functions - u can use once it is imported.

# no import and using the module means error.

def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return "Please, enter only multiples of Three"

if __name__ == '__main__':
  num = int(raw_input("Enter your number to be cubed : "))
  print "Result : ", by_three(num)
