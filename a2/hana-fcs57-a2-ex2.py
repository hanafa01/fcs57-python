Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

x = input("Enter char: ")

for i in Names:
  if x in i.lower():
    print(i)
