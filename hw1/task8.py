dict1 = {1:1000, 2:3000, 3: 100, 4: 6700, 5: 79000}
i = 0
list1 = []
for value in dict1.values():
    if i < len(dict1):
        list1.append(value)
        i+=1
j = 0
for i in range(len(dict1)):
    if j<3:
        j += 1
        print(max(list1))
        list1.remove(max(list1))
