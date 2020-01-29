def pow1():
    n = int(input('Enter n: '))
    cnt = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i * i)
            cnt += 1
    print('Count = ', cnt)


pow1()
