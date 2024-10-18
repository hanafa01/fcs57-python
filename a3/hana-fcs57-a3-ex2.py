def ex2(l, num, str):
  if num == 0:
    print(str)
    return
  
  for c in l:
    ex2(l, num-1, str+c)


l = ['a', 'b', 'c']
n = 2

if n > len(l):
  print("choose n less than the length of the array")
else:
  ex2(l,n,"")
