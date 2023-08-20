/*
 * File: NQueens.cpp
 * -----------------
 * This program solves the N-queens problem, which can be
 * stated as follows: Is it possible to place N queens on
 * an NxN chessboard so that no two queens are in the same
 * row, column, or diagonal line.
 */

#include <cctype>
#include <iostream>
#include "console.h"
#include "grid.h"
#include "simpio.h"
using namespace std;

/* Function prototypes */

void displayBoard(Grid<char> & board);
bool solveQueens(Grid<char> & board, int nPlaced);
bool queenIsLegal(Grid<char> & board, int row, int col);

/* Main program */

int main() {
	int n = getInteger("Enter size of board: ");
	Grid<char> board(n, n);
   for (int i = 0; i < n; i++) {
   	for (int j = 0; j < n; j++) {
      	board[i][j] = ' ';
      }
   }
	if (solveQueens(board, 0)) {
		displayBoard(board);
	} else {
		cout << "There is no solution for this board" << endl;
	}
   return 0;
}

/*
 * Function: displayBoard
 * Usage: displayBoard(board);
 * ---------------------------
 * Displays each of the squares in the board.
 */

void displayBoard(Grid<char> & board) {
	int n = board.numRows();
	for (int j = 0; j < n; j++) {
   	cout << "+-";
   }
	cout << "+" << endl;
	for (int i = n - 1; i >= 0; i--) {
		for (int j = 0; j < n; j++) {
			cout << "|" << board[i][j];
		}
		cout << "|" << endl;
		for (int j = 0; j < n; j++) {
         cout << "+-";
      }
      cout << "+" << endl;
	}
}

/*
 * Function: solveQueens
 * Usage: bool flag = solveQueens(board, nPlaced);
 * -----------------------------------------------
 * Tries to solve the N-Queens problem on the specified board,
 * which is already populated with nPlaced queens by earlier
 * recursive calls.  The function returns true if a solution is
 * found, otherwise it returns false.
 */

bool solveQueens(Grid<char> & board, int nPlaced) {
	int n = board.numRows();
	if (nPlaced == n) return true;
	for (int row = 0; row < n; row++) {
		if (queenIsLegal(board, row, nPlaced)) {
			board[row][nPlaced] = 'Q';
			if (solveQueens(board, nPlaced + 1)) return true;
			board[row][nPlaced] = ' ';
		}
	}
	return false;
}

/*
 * Function: queenIsLegal
 * Usage: bool legal = queenIsLegal(board, row, col);
 * --------------------------------------------------
 * Checks the existing board position to determine if a new queen
 * can be placed at the specified row and column.  The algorithm
 * ensures that no queens exist in any columns beyond the current
 * one, so the function need only check for queens in columns less
 * than the specified one.  The variables r1 and r2 are used to keep
 * track of the row numbers along the diagonals starting at the
 * current position.
 */

bool queenIsLegal(Grid<char> & board, int row, int col) {
   int n = board.numRows();
   int r1 = row;
   int r2 = row;
   for (int c = col - 1; c >= 0; c--) {
      r1++;
      r2--;
      if (board[row][c] == 'Q'
         || (r1 < n && board[r1][c] == 'Q')
         || (r2 >= 0 && board[r2][c] == 'Q')) return false;
   }
   return true;
}
