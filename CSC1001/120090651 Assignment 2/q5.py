firstlist = list()
for i in range(0,100):
    firstlist.append(False)
for a in range(1,101):
    for b in range(1,100//a + 1):
        firstlist[a*b-1] = not firstlist[a*b-1]
print('Lockers are open:',end='')

for i in range(100):
    if firstlist[i]:
        print(i+1, end=' ')