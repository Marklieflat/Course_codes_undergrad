n = float(input('Enter a positive number:'))
def sqrt(n):
    lastGuess = 1
    while True:
        nextGuess = (lastGuess + (n/lastGuess))/2
        if abs(nextGuess-lastGuess) < 0.0001:
            print('The approximation of the square root is:',nextGuess)
            return 
        else:
            lastGuess = nextGuess
sqrt(n)
        