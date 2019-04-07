inputstr = input()
charlist = []
for c in inputstr:
    charlist.append(int(c))
res = 0
for i in charlist:
    res += i
print(res)