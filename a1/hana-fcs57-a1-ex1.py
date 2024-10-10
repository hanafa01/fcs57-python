age = input('Enter your age: ')

if(int(age)>= 18):
  residence = input('Enter you country residence: ')
  if (residence.strip().lower() == 'lebanon'):
    rank = input('Enter you hacker rank: ')
    if(int(rank) > 110):
      print('Welcome to FCS!')
    else:
      print("Insufficient hacker rank score")
  else:
    print('Foreign Country.')
else:
  print('Insufficient age.')
