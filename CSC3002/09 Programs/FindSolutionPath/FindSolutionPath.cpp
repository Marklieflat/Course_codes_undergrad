/*
 * File: FindSolutionPath.cpp
 * --------------------------
 * This program finds a solution path in a maze.
 */

#include <iostream>
#include <string>
#include "console.h"
#include "direction.h"
#include "gwindow.h"
#include "maze.h"
#include "point.h"
#include "vector.h"
using namespace std;

/* Function prototypes */

bool findSolutionPath(Maze & maze, Point start, Vector<Point> & path);
Point adjacentPoint(Point start, Direction dir);
void unmarkAllSquares(Maze & maze);

/* Main program */

int main() {
   GWindow gw;
   Maze maze("SampleMaze.txt", gw);
   Vector<Point> path;
   if (findSolutionPath(maze, maze.getStartPosition(), path)) {
      for (Point pt : path) {
         cout << pt << endl;
      }
   }
   return 0;
}

/*
 * Function: findSolutionPath
 * Usage: bool flag = findSolutionPath(maze, start, path);
 * -------------------------------------------------------
 * Attempts to generate a solution to the current maze from the specified
 * start point.  This function is similar to the solveMaze function in the
 * text, but keeps track of the path as it proceeds.  The solution is
 * returned as a vector of Point objects through the reference parameter path.
 */

bool findSolutionPath(Maze & maze, Point start, Vector<Point> & path) {
   if (maze.isOutside(start)) return true;
   if (maze.isMarked(start)) return false;
//   path.add(start);
   maze.markSquare(start);
   for (Direction dir = NORTH; dir <= WEST; dir++) {
      if (!maze.wallExists(start, dir)) {
         if (findSolutionPath(maze, adjacentPoint(start, dir), path)) {
            path.insert(0, start); // an alternative way to change path is to use the add/remove methods
            return true;
         }
      }
   }
   maze.unmarkSquare(start);
//   path.remove(path.size() - 1);
   return false;
}

/*
 * Function: adjacentPoint
 * Usage: Point finish = adjacentPoint(start, dir);
 * ------------------------------------------------
 * Returns the Point that results from moving one square from start
 * in the direction specified by dir.  For example, if pt is the
 * point (1, 1), calling adjacentPoint(pt, EAST) returns the
 * point (2, 1).  To maintain consistency with the graphics package,
 * the y coordinates increase as you move downward on the screen.  Thus,
 * moving NORTH decreases the y component, and moving SOUTH increases it.
 */

Point adjacentPoint(Point start, Direction dir) {
   switch (dir) {
    case NORTH: return Point(start.getX(), start.getY() - 1);
    case EAST:  return Point(start.getX() + 1, start.getY());
    case SOUTH: return Point(start.getX(), start.getY() + 1);
    case WEST:  return Point(start.getX() - 1, start.getY());
   }
   return start;
}

/*
 * Function: unmarkAllSquares
 * Usage: unmarkAllSquares(maze);
 * ------------------------------
 * Calls unmarkSquare on all of the squares in maze.
 */

void unmarkAllSquares(Maze & maze) {
   for (int x = 0; !maze.isOutside(Point(x, 0)); x++) {
      for (int y = 0; !maze.isOutside(Point(0, y)); y++) {
         maze.unmarkSquare(Point(x, y));
      }
   }
}
