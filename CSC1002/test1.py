import random
count = 0
step = 0
def initialize(dimension):                       # To create a list which contains numbers and spaces that is needed in the game
    global firstlist                                 
    for i in range(1,dimension**2):
        firstlist.append(i)
    firstlist.append(' ')
    functions = [move_down,move_up,move_left,move_right]
    for i in range (100000):                    # To reorganize the list
        functions[random.randint(0,3)]()
    return
        
def print_out():                                # To print out the list as a puzzle
    count = 0
    for i in firstlist:
        print('%-4s' % i,end='')
        count += 1
        if count % dimension == 0:              # Change the row to print
            print(' ',end='\n')
    return

def move_right():                               # Allow the user to move the number right
    global step
    ind = firstlist.index(' ')
    firstlist[ind],firstlist[ind-1] = firstlist[ind-1],firstlist[ind]
    step += 1
    return 

def move_left():                                # Allow the user to move the number left
    global step
    ind = firstlist.index(' ')
    firstlist[ind], firstlist[ind+1] = firstlist[ind+1], firstlist[ind]
    step += 1
    return 

def move_down():                                # Allow the user to move the number down
    global step
    ind = firstlist.index(' ')
    firstlist[ind], firstlist[ind-dimension] = firstlist[ind-dimension],firstlist[ind]
    step += 1
    return 

def move_up():                                  # Allow the user to move the number up
    global step
    ind = firstlist.index(' ')
    firstlist[ind], firstlist[ind+dimension] = firstlist[ind+dimension], firstlist[ind]
    step += 1
    return 

def check():                                    # To check whether the game is solved or not
    if firstlist[-1] != ' ':
        return False
    for num in range(1, len(firstlist)-1):
            if firstlist[num] < firstlist[num-1]:
                return False
    return True

print("Welcome to Mark's puzzle game. In as few steps and short time as possible, to let the number of squares on the board, from left to right, from top to bottom in a right arrangement.")        
quit = False
while quit == False:
    firstlist = []
    count = 0
    while True:                                 # The first while-true loop is to print out the puzzle
        dimension = input('Enter the desired dimension of the puzzle >')
        try:
            dimension = int(dimension)
            if dimension >= 3 and dimension <= 10:
                initialize(dimension)
                print_out()
                break
            else:
                print('Wrong input, please try again!')
        except:
            print('Wrong input, please try again!')

    inputs = input('Enter the four letters used for left, right, up, and down directions:')
    d_left, d_right, d_up, d_down = inputs.split(' ')
    step = 0
    while True:                                    # The second loop is to let the user control the game and after each control 
        print('Please enter your direction (', end="")   # testing the puzzle is solved or not
        ind = firstlist.index(' ')
        if not ind % dimension == 0:
            print("right-", d_right, end=' ')
        if not ind >= dimension**2-dimension:
            print("up-", d_up, end=" ")
        if not (ind+1) % dimension == 0:
            print("left-", d_left, end=" ")
        if not ind <= dimension-1 :    
            print("down-", d_down, end=" ")
        print(") >: ", end='')
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
            print('Congratulations! Your total number of moves is:',step)
            break
    print("Enter 'n' to start a new game or 'q' to end the game > ",end='')                           
    while True:             # This part is to ask the user whether to start a new game or not
        answer = input() 
        if answer == 'q':
            quit = True
            break
        elif answer == 'n':
            quit = False
            break
        else:
            print('Wrong input, please try again!')
            print("Enter 'n' to start a new game or 'q' to end the game >")