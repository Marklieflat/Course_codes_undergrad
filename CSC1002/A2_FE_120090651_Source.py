import turtle
import random
import time

m_screen = None
m_snake = None
foods = []
m_body = []
contact = 0
m_time = 0
m_speedtime = 0
length = 8
m_length = 1
monster_move = True
reupdate = True
process = True
last_direction = 'None'
status = 'None'

def setScreen(w = 660, h = 740):
    global screen
    screen = turtle.Screen()
    screen.setup(width = w, height = h)
    screen.tracer(0)
    screen.title('Snake by Ma Kexuan')
    return screen

def initialize():
    global i_setup, contact, m_time
    i_setup = turtle.Turtle()
    i_setup.pensize(2)
    i_setup.hideturtle()
    i_setup.penup()
    i_setup.goto(-250,290)
    i_setup.pendown()
    i_setup.goto(250,290)
    i_setup.goto(250,-290)
    i_setup.goto(-250,-290)
    i_setup.goto(-250,290)
    i_setup.penup()
    i_setup.goto(-250,210)
    i_setup.pendown()
    i_setup.pensize(3)
    i_setup.goto(250,210)
    i_setup.penup()
    m_screen.update()
    
def showstatus():
    global show, contact, m_time
    show = turtle.Turtle()
    show.hideturtle()
    show.penup()
    show.goto(-220,255)
    show.write('Contact:   %-6s      Time:   %-6s     Motion:     %s '%(contact, m_time, status), False, 'left', font = ("Arial", 14, "normal"))
    m_screen.update()

def refresh():
    global m_time
    if reupdate:
        show.clear()
        m_time = int(time.time()) - int(starttime)
        show.write('Contact:   %-6s      Time:   %-6s     Motion:     %s '%(contact, m_time, status), False, 'left', font = ("Arial", 14, "normal"))
        m_screen.update()
        m_screen.ontimer(refresh, 100)

def description():
    global des
    des = turtle.Turtle()
    des.hideturtle()
    des.penup()
    des.goto(-220,70)
    des.write(
        "Welcome to Mark's version of snake,\n\n"
        "You are going to use the 4 arrow keys to move the snake\n"
        "around the screen, trying to consume all the food items\n"
        "before the monster catches you.\n\n"
        "Click anywhere on the screen to start the game, have fun!", False, 'left', font = ("Arial", 12, "normal"))

def setupTheFood():
    global starttime, foods
    for i in range(1,10):
        food = turtle.Turtle()
        food.number = i
        food.hideturtle()
        x, y = random.randint(-230, 230), random.randint(-290,190)
        food.penup()
        food.goto(x, y)
        food.pendown()
        food.write(i, False, font=('Arial',12))
        foods.append(food)
    m_screen.onclick(None)
    starttime = time.time()
    return foods

def setupSnake():
    snake = turtle.Turtle('square')
    snake.color('red')
    snake.penup()
    snake.goto(0,0)
    snake.pendown()
    snake.direction = None
    screen.update()
    return snake

def setupMonster():
    monster = turtle.Turtle('square')
    monster.color('purple')
    while True:
        x, y = random.randint(-100, 100), random.randint(-100,35)
        if abs(x) > 20 and abs(y) > 20:
            monster.penup()
            monster.goto(x, y)
            monster.pendown()
            screen.update()
            break
        else:
            continue
    return monster

def move_up():
    m_snake.direction = 'Up'
def move_down():
    m_snake.direction = 'Down'
def move_left():
    m_snake.direction = 'Left'
def move_right():
    m_snake.direction = 'Right'
def stop():
    global last_direction
    if m_snake.direction != 'None':
        last_direction = m_snake.direction
        m_snake.direction = 'None'
    else:
        m_snake.direction = last_direction

def autoMoveSnake():
    global process, length, status
    if process == True:
        if m_snake.direction == 'None':
            status = 'Paused'
        elif m_snake.direction == 'Up':
            m_snake.sety(m_snake.ycor() + 20)
            status = 'Up'
            if m_snake.ycor() >= 200:    
                m_snake.direction = "None"
        elif m_snake.direction == 'Down':
            m_snake.sety(m_snake.ycor() - 20)
            status = 'Down'
            if m_snake.ycor() <= -280:    
                m_snake.direction = "None"
        elif m_snake.direction == 'Left':
            m_snake.setx(m_snake.xcor() - 20)
            status = 'Left'
            if m_snake.xcor() <= -240:   
                m_snake.direction = "None"
        elif m_snake.direction == 'Right':
            m_snake.setx(m_snake.xcor() + 20)
            status = 'Right'
            if m_snake.xcor() >= 240:   
                m_snake.direction = "None"
        if status != 'Paused':
            snakebody()
        extendBody()
        end()
        if end() == False:
            process = False
        m_screen.ontimer(autoMoveSnake, m_speedtime)
        m_screen.update()

def moveSnake():
    m_snake.penup()
    m_screen.listen()
    m_screen.onkey(move_up,"Up")
    m_screen.onkey(move_down,'Down')
    m_screen.onkey(move_left,'Left')
    m_screen.onkey(move_right,'Right')
    m_screen.onkey(stop,'space')
    autoMoveSnake()
    m_screen.update()

def moveMonster():           
    if monster_move:
        a = m_snake.xcor()
        b = m_snake.ycor()
        monster_movetime = random.randint(300,700)
        angle = m_monster.towards(a, b)
        if 45 <= angle < 135:
            m_monster.setheading(90)
        if 135 <= angle < 225:
            m_monster.setheading(180)
        if 225 <= angle < 315:
            m_monster.setheading(270)
        if (0 <= angle < 45) or (315 <= angle < 360):
            m_monster.setheading(0)
        count_contact()
        m_monster.penup()
        m_monster.forward(20)
        m_screen.ontimer(moveMonster, monster_movetime)
        m_screen.update()
    
def snakebody():
    global m_body, m_length, m_speedtime
    m_snake.color('blue','black')
    m_snake.stamp()
    m_body.append(m_snake.pos())
    m_snake.color('red')
    m_length += 1
    if m_length >= length:
        m_snake.clearstamps(1)
        m_length -= 1
        m_body.pop(0)
        m_speedtime = 300
    else:
        m_speedtime = 600

def extendBody():
    global foods, length
    for i in foods:
        if i.distance(m_snake) <= 15:
            length += i.number
            i.clear()
            foods.remove(i)
            

def count_contact():
    global contact
    for body in m_body:
        if m_monster.distance(body) <= 10:
            contact += 1

def startup(x, y):
    setupTheFood()
    des.clear()
    moveSnake()
    # moveMonster()
    refresh()

def end():
    global monster_move, reupdate, foods
    ending = turtle.Turtle()
    ending.hideturtle()
    ending.penup()
    if m_snake.distance(m_monster) <= 20:
        ending.pencolor('orange')
        ending.goto(m_snake.pos())
        ending.write('Game Over!', font=('Arial',20,'normal'))
        m_snake.direction = 'Stop'
        monster_move = False
        reupdate = False
        return False
    if len(foods) == 0:
        ending.pencolor('blue')
        ending.goto(m_snake.pos())
        ending.write('Winner!', font=('Arial',20,'normal'))
        m_snake.direction = 'Stop'
        m_snake.direction = 'Stop'
        monster_move = False
        reupdate = False
        return False

if __name__ == '__main__':
    m_screen = setScreen()
    initialize()
    description()
    m_snake = setupSnake()
    m_monster = setupMonster()
    showstatus()
    m_screen.onclick(startup)
    turtle.done()