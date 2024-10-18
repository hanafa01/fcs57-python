Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

x = input("Enter char: ").strip()

if(len(x) == 1):
  for i in Names:
    if x.lower() in i.lower():
      print(i)
else:
  print('Please choose one char');