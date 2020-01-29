list1 = [str(i) for i in input('enter the values in the first list: ').split()]
list2 = [str(i) for i in input('enter the values in the second list: ').split()]
if len(list1) >= len(list2):
    print(set(set(list1)-set(list2)).union(set(list2) - set(list1)))

