n = int(input("enter n: "))
dict1 = {}
dict2 = {}
f_dict = {}
for i in range(1,n+1):
    dict1[i]=i*i
    dict2[i+n]=i +4
f_dict = dict(list(dict1.items()) + list(dict2.items()))
print(f_dict)
