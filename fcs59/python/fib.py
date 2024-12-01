n = int(input('Enter a number: '))

a = 0
b = 1

if n < 0:
    print('Enter positive number')
elif n == 0:
    print(0)
else:
    for i in range(n):
        print(a, end=" ")
        next = a + b
        a = b
        b = next