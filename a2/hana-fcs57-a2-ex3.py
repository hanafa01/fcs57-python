numbers = [-12, 4, 12, 25, 67]

x = int(input("Add number: "))

while x != -99:   
  numbers = numbers[:x] + [x] + numbers[x:]
  print(numbers)
  x = int(input("Add number: "))


