from math import sqrt
def is_primenumber(numbers):
    for i in range(2, int(sqrt(numbers) + 1)):
        while (numbers % i == 0):
            return False
    return True

while True:
    N = input('Enter an integer:')
    try:
        N = eval(N)
        if N > 2:
            count = 0
            for i in range(2, N):
                if is_primenumber(i) == True:
                    print(i,end='  ')
                    count += 1 
                    if (count % 8 == 0):
                        print(' ', end='\n')
            break
        else:
            print('Improper inputs, please try again!')
    except:
        print('Improper inputs, please try again!')