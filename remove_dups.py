
def remove_dups(lst):
  new_lst = []
  for item in lst:
    if item not in new_lst:
      new_lst.append(item)

  return new_lst

if __name__ == '__main__':
  print remove_dups([1,2,3,4,2,2,5,5,7,9,9,9,0,0,0])
