from math import sqrt
def isPrime(num):
    for i in range(2, int(sqrt(num) + 1)):
        while (num % i == 0):
            return False
    return True

def notPalindrome(num):
    num = str(num)
    if num == num[::-1]:
        return False
    else:
        return True

def reverse(num):
    num = str(num)
    num = num[::-1]
    return int(num)

count = 0
num = 0
while count < 100:
    if isPrime(num) and notPalindrome(num) and isPrime(reverse(num)) and notPalindrome(reverse(num)):
        count += 1
        if count % 10 == 0:
            print('%5d' % num)
        else:
            print('%5d' % num, end='')
    num += 1
