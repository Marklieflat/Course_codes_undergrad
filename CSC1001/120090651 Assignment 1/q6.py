from math import sin
from math import cos
from math import tan
while True:
    f = input('Enter a trigonometric function name:')
    if f in ['sin','cos','tan']:
        while True:
            try:
                a = eval(input('Please enter the left endpoint a:'))
                b = eval(input('Please enter the right endpoint b:'))
                while True:
                    n = input('Please enter the number of sub-intervals:')
                    try:
                        n = int(n)
                        result = 0
                        if f == 'sin':
                            for i in range(1, n+1):
                                x = float(a + ((b-a)/n) *(i-1/2))
                                integration = ((b-a)/n) * sin(x)
                                result = result + integration
                            print('The result is:',result)
                            break
                        elif f == 'cos':
                            for i in range(1, n+1):
                                x = float(a + ((b-a)/n) *(i-1/2))
                                integration = ((b-a)/n) * cos(x)
                                result = result + integration
                            print('The result is:',result)
                            break
                        elif f == 'tan':
                            for i in range(1, n+1):
                                x = float(a + ((b-a)/n) *(i-1/2))
                                integration = ((b-a)/n) * tan(x)
                                result = result + integration
                            print('The result is:',result)
                            break
                        else:
                            print('Improper inputs, please try again!')
                    except:
                        print('Improper inputs, please try again!')
                break
            except:
                print('Improper inputs, please try again!')
        break
    else:
        print('Improper inputs, please try again!')