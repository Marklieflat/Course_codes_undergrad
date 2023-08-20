# class Game:
#     def __init__(self, board=[[0,0,0],[0,0,0],[0,0,0]]):
#         self.board = board

#     def draw_board(self):
#         sample = ['    | ','  x | ','  o | ']
#         print(' --- --- ---')
#         for i in range(3):
#             print('|',end='')
#             for j in range(3):
#                 print(sample[self.board[i][j]],end = '')
#             print('\n --- --- ---')

#     def player_one_move(self, row, col):
#         if row < 0 or row > 2 or col < 0 or col > 2:
#             print('Invalid input')
#             return
#         if self.board[row][col] > 0:
#             print('Occupied')
#             return
#         self.board[row][col] = 1
#         self.draw_board()

#     def player_two_move(self, row, col):
#         if row < 0 or row > 2 or col < 0 or col > 2:
#             print('Invalid input')
#             return
#         if self.board[row][col] > 0:
#             print('Occupied')
#             return
#         self.board[row][col] = 2
#         self.draw_board()

# g = Game([[1,2,0],[0,1,2],[0,0,0]])
# g.player_one_move(1,0)

def foo(k):
    k[0] = 1
q = [0]
foo(q)
print(q)