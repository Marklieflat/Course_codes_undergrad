/*
 * File: KnightsTour.cpp
 * ---------------------
 * This program find a knight's tour on an N x M chessboard.
 */

#include "KnightsTour.h"

/*
 * Function: solveKnightsTour
 * Usage: solveKnightsTour(n, m);
 * ------------------------------
 * Solves the knight's tour problem for a n x m chessboard.
 */

void solveKnightsTour(int n, int m) {
   Grid<int> board(n, m);
   if (findKnightsTour(board, 0, 0, 1)) {
      displayBoard(board);
   } else {
      cout << "No tour exists for this board." << endl;
   }
}

/*
 * Function: displayBoard
 * Usage: displayBoard(board);
 * ---------------------------
 * Displays each of the squares in the board along with its sequence
 * number in the tour.
 */

void displayBoard(Grid<int> & board) {
   for (int i = board.numRows() - 1; i >= 0; i--) {
      for (int j = 0; j < board.numCols(); j++) {
         cout << " " << setw(2) << board[i][j];
      }
      cout << endl;
   }
}


int x_step[] = {2,1,-1,-2,-2,-1,1,2}; // Record the next position to go
int y_step[] = {1,2,2,1,-1,-2,-2,-1};

bool findKnightsTour(Grid<int> & board, int row, int col, int seq){
    if (!board.inBounds(row, col)) return false; // Check if the position is off the board
    if (board[row][col] != 0) return false; // Check whether the position has been visited
    if (seq == 64){ // Check if the whole knight tour exists
        board[row][col] = 64;
        return true;
    }
    board[row][col] = seq; // Record the recent step
    for (int i = 0; i < 8; i++){
        if (findKnightsTour(board, row + x_step[i], col + y_step[i], seq + 1)) return true; // Backtracking recursions to find the next solution
    }
    board[row][col] = 0; // if it cannot return true above, then refresh the position to be 0
    return false;
}
