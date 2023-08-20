/*
 * File: Hanoi.cpp
 * ---------------
 * This program solves the Tower of Hanoi puzzle.
 */

#include <iostream>
#include "console.h"
#include "ghanoi.h"
#include "gwindow.h"
using namespace std;

/* Constants */

const int N_DISKS = 6;

/* Function prototypes */

void moveTower(int n, char start, char finish, char temp);

/* Main program */

int main() {
   GWindow gw(700, 400);
   initHanoiDisplay(gw, N_DISKS);
   moveTower(N_DISKS, 'A', 'B', 'C');
   return 0;
}

/*
 * Function: moveTower
 * Usage: moveTower(n, start, finish, temp);
 * -----------------------------------------
 * Moves a tower of size n from the start spire to the finish
 * spire using the temp spire as the temporary repository.
 */

void moveTower(int n, char start, char finish, char temp) {
   if (n == 1) {
      moveSingleDisk(start, finish);
   } else {
      moveTower(n - 1, start, temp, finish);
      moveSingleDisk(start, finish);
      moveTower(n - 1, temp, finish, start);
   }
}
