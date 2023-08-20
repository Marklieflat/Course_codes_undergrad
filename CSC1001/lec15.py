def binarySum(L,start,stop):
    if start >= stop:
        return 0
    elif start == stop -1:
        return L[start]
    else:
        mid = (start + stop) //2