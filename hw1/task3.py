s = str(input('enter your string: '))
if len(s) >= 2:
    s = s[:2] + s[-2:]
    print(s)
else:
    s=''


