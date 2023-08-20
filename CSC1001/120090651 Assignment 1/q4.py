while True:
    N = input('Enter a number:')
    try:
        N = eval(N)
        if type(N) == int and N > 0:
            print('%-6s %-6s %-6s' % ('m','m+1','m**(m+1)'))
            for m in range(1,N+1):
                print('%-6s %-6s %-6s' % (m,m+1,m**(m+1)))
            break
        else:
            print('Improper inputs, please try again!')
    except:
        print('Improper inputs, please try again!')