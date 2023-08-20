from time import time
starttime = time()
for i in range(1,20000):
    if i % 10 == 0:
        print(i)
endtime = time()
print(endtime-starttime)