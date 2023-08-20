def loopstring(mystr):
    length = len(mystr)
    j = 0
    while j < length:
        print(j, mystr[j])
        j = j + 1
    print('finished')

loopstring('Matrix is a computer simulated world')