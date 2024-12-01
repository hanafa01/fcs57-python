n = int(input('Enter a number: '))

if n < 0:
    print('Enter positive number')
else:
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            print(i, end=" ") 