list1 = [str(i) for i in input('enter the values in the list: ').split()]
cnt = 0
for i in range(len(list1)):
    word = list1[i]
    if word[:1] == word[-1:]:
        cnt +=1
print(cnt)