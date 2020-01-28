a, b = [str(i) for i in input('enter the values in the list: ').split()], []
for i in a:
    if b.count(i) == 0:
        b.append(i)
for i in b:
    print(i, end=" ")