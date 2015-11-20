#!/usr/bin/env python

def string_reversal(string):
  print "string : ", string
  reverse_lst = []
  for item in range(len(string)-1, -1, -1):
    print string[item]
    reverse_lst.append(string[item])
  
  # Joining the items of that list
  print  ''.join(reverse_lst)

if __name__ == '__main__':
  string_reversal("arun")
