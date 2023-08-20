import random
firstlist = []
count=0
def initialize(dimension):
    global firstlist
    for i in range(1,dimension**2):
        firstlist.append(i)
    firstlist.append(' ')
    a=[move_down,move_left,move_left,move_right]
    for i in range (5000):
        a[random.randint(0,3)]()
    return
        
def print_out():
    count = 0
    for i in firstlist:
        print('%-4s' % i,end='')
        count += 1
        if count % dimension == 0:
            print(' ',end='\n')
    return

def move_right():
    global count
    ind = firstlist.index(' ')
    if ind % dimension == 0:
        return False
    firstlist[ind],firstlist[ind-1] = firstlist[ind-1],firstlist[ind]
    count+=1
    return True

def move_left():
    global count
    ind = firstlist.index(' ')
    if (ind+1) % dimension == 0:
        return False
    firstlist[ind], firstlist[ind+1] = firstlist[ind+1], firstlist[ind]
    count+=1
    return True

def move_down():
    global count
    ind = firstlist.index(' ')
    if ind <= dimension-1 :
        return False
    firstlist[ind], firstlist[ind-dimension] = firstlist[ind-dimension],firstlist[ind]
    count+=1
    return True

def move_up():
    global count
    ind = firstlist.index(' ')
    if ind >= dimension**2-dimension:
        return False
    firstlist[ind], firstlist[ind+dimension] = firstlist[ind+dimension], firstlist[ind]
    count+=1
    return True

def check():
    if firstlist[-1] != ' ':
        return False
    for num in range(1,len(firstlist)-1):
            if firstlist[num]<firstlist[num-1]:
                return False
    return True


while True:
    try:
        dimension = int(input('Enter the desired dimension of the puzzle >'))
        inputs = input('Enter the four letters used for left, right, up, and down directions >')
        d_left, d_right, d_up, d_down = inputs.split(' ')
        count = 0
        if dimension >= 3 and dimension <= 10:
            initialize(dimension)
            print_out()
            while True:
                print('Please enter your move (',end="")
                ind = firstlist.index(' ')
                if not ind % dimension == 0:
                    print("right-", d_right,end=',')
                if not ind >= dimension**2-dimension:
                    print("up-", d_up,end=",")
                if not (ind+1) % dimension == 0:
                    print("left-", d_left,end=",")
                if not ind <= dimension-1 :    
                    print("down-", d_down,end=",")
                print(") > ")
                option = input()
                for x in option:
                    if option == d_left:
                        move_left()
                    elif option == d_right:
                        move_right()
                    elif option == d_up:
                        move_up()
                    else:
                        move_down()
                print_out()
                check()
                if check() == True:
                    print('Congratulations! Your total number of moves is:',count)
                    x = input("Enter 'n' to start a new game or enter 'q' to end the game > ")
                    if x == 'n':
                       False 
                    elif x == 'q':
                        break
                    else:
                        print('invalid input! Please try again!')
                        break
        else:
            print('Wrong input, please try again!')
            False
    except:
        print('Wrong input, please try again!')
        False