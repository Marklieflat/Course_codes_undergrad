a = 100
def invest100_7(a):
    a = 1.1*a
    return a

for i in range(7):
    a = invest100_7(a)

print(a)