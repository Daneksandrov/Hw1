s = str(input('enter your string: '))
fs = ''
fd = {}
for i in range(len(s)):
    if s.count(s[i]) > 0 and fs.count(s[i]) == 0:
        fs += s[i]
        fs += str(s.count(s[i]))
        fd[s[i]] = s.count(s[i])
print(fd)