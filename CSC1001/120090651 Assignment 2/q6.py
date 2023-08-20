def check(position, queen):
    for i in range(1,queen):
        if position[i] == position[queen]:
            return False
        if abs(position[i] - position[queen]) == abs(i - queen):
            return False
    return True

def create():
    queen = 1
    position = [0 for row in range(9)]
    while queen > 0:
        position[queen] += 1
        while (position[queen] <= 8) and check(position,queen) == False:
            position[queen] += 1
        if position[queen] <= 8:
            if queen == 8:
                break
            else:
                queen += 1
                position[queen] = 0
        else:
            position[queen] = 0
            queen = queen - 1
    return position[1:]

col = create()
_row = 1
while _row <= 8:
    _column = 1
    boardrow = ''
    while _column <= 9:
        if _column == col[_row-1] + 1 :
            boardrow += 'Q|'
        else:
            boardrow += ' |'
        _column += 1
    print(boardrow)
    _row += 1