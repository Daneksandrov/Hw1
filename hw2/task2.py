def foo(a, b, c):
    cnt = 0
    for i in range(a, b):
        if i % c == 0:
            cnt += 1
    print('Count = ', cnt)


a1 = int(input('enter the first number: '))
b1 = int(input('enter the second number: '))
c1 = int(input('enter the third number: '))
foo(a1, b1, c1)
