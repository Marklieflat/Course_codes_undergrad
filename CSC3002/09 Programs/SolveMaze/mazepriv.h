/*
 * File: mazepriv.h
 * ----------------
 * This file contains the private section of the Maze class.  The
 * purpose of putting this section in a separate file is to hide the
 * details of the implementation from clients of the maze.h interface.
 */

private:

/* Structure representing a single square */

   struct Square {
      bool marked;
      bool walls[4];
   };

/* Instance variables */

   Grid<Square> maze;
   Point startSquare;
   bool mazeShown;
   double x0;
   double y0;
   int rows;
   int cols;

/* Private functions */

   void computeMazeSize(ifstream & infile);
   void processMazeFile(ifstream & infile);
   void processDividerLine(string line, int y);
   void processPassageLine(string line, int y);
   void setHorizontalWall(Point pt);
   void setVerticalWall(Point pt);
   void setStartSquare(Point pt);
   void drawMaze();
   void drawMazeGrid();
   void drawWalls();
   void drawMarks();
   void drawMark(Point pt);
   void eraseMark(Point pt);
   Point adjacentPoint(Point start, Direction dir);
