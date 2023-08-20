import random
firstlist = []
def initialize(dimension):
    global firstlist
    for i in range(1,dimension**2):
        firstlist.append(i)
    firstlist.append(' ')
    a = [move_down, move_up, move_left, move_right]
    for i in range(500*dimension):
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
    ind = firstlist.index(' ')
    if ind % dimension == 0:
        return False
    firstlist[ind],firstlist[ind-1] = firstlist[ind-1],firstlist[ind]
    return True

def move_left():
    ind = firstlist.index(' ')
    if (ind+1) % dimension == 0:
        return False
    firstlist[ind], firstlist[ind+1] = firstlist[ind+1], firstlist[ind]
    return True

def move_down():
    ind = firstlist.index(' ')
    if ind <= dimension-1 :
        return False
    firstlist[ind], firstlist[ind-dimension] = firstlist[ind-dimension],firstlist[ind]
    return True

def move_up():
    ind = firstlist.index(' ')
    if ind >= dimension**2-dimension:
        return False
    firstlist[ind], firstlist[ind+dimension] = firstlist[ind+dimension], firstlist[ind]
    return True

def check():
    if firstlist[-1] != ' ':
        return False
    for num in range(1,len(firstlist)-1):
            if firstlist[num] < firstlist[num-1]:
                return False
    return True

def Track_moves():
    count = 0
    while True:
        if move_up() == True:
            count += 1
        elif move_down() == True:
            count += 1
        elif move_left() == True:
            count += 1
        elif move_right() == True:
            count += 1
        if check() == True:
            break
    print('Your total number of moves is:',count)
    return 

while True:
    dimension = int(input('Enter the dimension:'))
    try:
        if dimension >= 3 and dimension <= 10:
            initialize(dimension)
            print_out()
            break
        else:
            print('Wrong input, please try again!')
            False
    except:
        print('Wrong input, please try again!')
        False

inputs = input('Enter the four letters used for left, right, up, and down directions:')
d_left, d_right, d_up, d_down = inputs.split(' ')
count = 0
while True:
    option = input('Please enter your direction:')
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
        print('Congratulations!')
        Track_moves()
        break