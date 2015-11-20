# Sliding Window Problem
# Read from slide.txt
# First line contains window size and 
# .. second line contains digits to be processed.

try:
  with open("slide.txt", "r") as fh:
    line_lst = fh.readlines()
except IOError:
  print "File cannot be opened for reading."
    
# To print the contents of the text file.
print "Window size : ",  int(line_lst[0].strip('\n'))
print "Numbers Input : ", (line_lst[1].strip('\n')).split()

w =  int(line_lst[0].strip('\n'))
print "w : ", w

strings = (line_lst[1].strip('\n')).split()
slst = [ int(item) for item in strings ]
print "slst : ", slst

sublst = []
for index, num in enumerate(slst):
  sublst.append(num) 
  if len(sublst) == w:
    print min(sublst),
    sublst.pop(0)

