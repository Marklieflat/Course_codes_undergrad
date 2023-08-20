number = input('Enter your credit card number:')
init = []
def getDigit(number):
    for i in number[-2::-2]:
        i = int(i)
        if i*2 < 10:
            init.append(i*2)
        else:
            init.append((i*2 % 10) + 1)
    return init

def sumOfDoubleEvenPlace(number):
    sumeven = 0
    for i in init:
        sumeven += int(i)
    return sumeven

def sumOfOddPlace(number):
    oddnum = number[1::2]
    sumodd = 0
    for i in oddnum:
        sumodd += int(i)
    return sumodd

def result(number):
    if (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0:
        return True

def isValid(number):
    if number[0] in ['4','5','6'] or (number[0] == 3 and number[1] == 7):
        pass
    if result(number):
        pass
    else:
        return False
    return True

if 13 <= len(number) <= 16:
    getDigit(number)
    sumOfDoubleEvenPlace(number)
    sumOfOddPlace(number)
    result(number)
    isValid(number)
    if isValid(number):
        print('Valid')
    else:
        print('Invalid')
else:
    print('invalid')