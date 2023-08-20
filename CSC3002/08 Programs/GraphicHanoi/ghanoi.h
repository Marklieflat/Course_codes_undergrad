/*
 * File: ghanoi.h
 * --------------
 * This file defines the interface for the graphical Hanoi functions.
 */

#ifndef _ghanoi_h
#define _ghanoi_h

#include "gwindow.h"

/*
 * Function: initHanoiDisplay
 * Usage: initHanoiDisplay(gw, n);
 * -------------------------------
 * Initializes the graphics window and draws the starting configuration
 * for a Towers of Hanoi puzzle for n disks, where n may not be larger
 * than 8.  If n is 0, this method draws only the frame.  If you want
 * to let the user select the size, you should call initghanoi(0) and
 * then call it again with the user's value.  Doing so ensures that the
 * graphics package is properly initialized.
 */

void initHanoiDisplay(GWindow & gw, int n);

/*
 * Function: moveSingleDisk
 * Usage: moveSingleDisk(char start, char finish);
 * -----------------------------------------------
 * Moves a single disk from the start tower to the finish
 * tower.  This method generates an error if the start tower
 * is empty or if the move violates the rules of the Hanoi
 * puzzle by placing a larger disk on top of a smaller one.
 */

void moveSingleDisk(char start, char finish);

/*
 * Function: setDelayTime
 * Usage: setDelayTime(msec);
 * --------------------------
 * Sets the number of milliseconds that the program pauses after making
 * a move.  Smaller numbers lead to faster animations.  The default is
 * 200 msec.
 */

void setDelayTime(double msec);

#endif
