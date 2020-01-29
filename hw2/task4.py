def foo(a, b, c):
    list1 = []
    list2 = []
    while a < b:
        list1.append(a)
        a += c
    print(list1)


a1 = int(input('enter the first number: '))
b1 = int(input('enter the second number: '))
c1 = int(input('enter step: '))
foo(a1, b1, c1)
