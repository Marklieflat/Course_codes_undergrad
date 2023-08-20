/*
 * File: ghanoi.cpp
 * ----------------
 * This file implements the graphical Hanoi functions.
 */

#include <iostream>
#include <string>
#include "error.h"
#include "ghanoi.h"
#include "gobjects.h"
#include "gwindow.h"
#include "vector.h"
using namespace std;

/* Constants */

const int MAX_DISKS = 8;
const double DEFAULT_DELAY_TIME = 200;
const double DISK_HEIGHT_PIXELS = 12;
const double DISK_MAX_PIXELS = 140;
const double DISK_DELTA_PIXELS = 10;
const double FRAME_THICKNESS_PIXELS = 6;

const string COLOR_TABLE[] = {
   "Unused",
   "Red",
   "Yellow",
   "Green",
   "Cyan",
   "Blue",
   "Magenta",
   "Orange",
   "Gray"
};

/* Private state */

static GWindow *gwp;
static int cSign;
static double frameThickness;
static double frameWidth;
static double frameHeight;
static double diskHeight;
static double diskMax;
static double diskDelta;
static double xBase;
static double yBase;
static double frameX[3];
static double delayTime = DEFAULT_DELAY_TIME;
static Vector< Vector<GRect *> > towers;

/* Function prototypes */

static void computeGraphicsParameters(int n);
static void drawFrame();
static GRect *createDisk(int k);
static void addDiskToTower(int tower, GRect *disk);

void initHanoiDisplay(GWindow & gw, int n) {
   if (n > MAX_DISKS) error("Disk limit exceeded");
   gwp = &gw;
   computeGraphicsParameters((n < 4) ? 4 : n);
   drawFrame();
   towers.clear();
   for (int i = 0; i < 3; i++) {
      towers.add(Vector<GRect *>());
   }
   for (int i = n; i > 0; i--) {
      GRect *disk = createDisk(i);
      addDiskToTower(0, disk);
      gwp->add(disk);
   }
}

/*
 * Function: moveSingleDisk
 * Usage: moveSingleDisk(char start, char finish);
 * -----------------------------------------------
 * Moves a single disk from the start tower to the finish
 * tower.  This method generates an error if the start tower
 * is empty or if the move violates the rules of the Hanoi
 * puzzle by placing a larger disk on top of a smaller one.
 */

void moveSingleDisk(char start, char finish) {
   int nDisks = towers[start - 'A'].size();
   if (nDisks == 0) error("The start tower is empty");
   GRect *disk = towers[start - 'A'][nDisks - 1];
   towers[start - 'A'].remove(nDisks - 1);
   nDisks = towers[finish - 'A'].size();
   if (nDisks > 0 && disk->getWidth()
                       > towers[finish - 'A'][nDisks - 1]->getWidth()) {
      error("You cannot place a larger disk on a smaller one");
   }
   addDiskToTower(finish - 'A', disk);
   gwp->repaint();
   pause(delayTime);
}

/*
 * Function: setDelayTime
 * Usage: setDelayTime(msec);
 * --------------------------
 * Sets the number of milliseconds that the program pauses
 * after making a move.  Smaller numbers lead to faster
 * animations.  The default is 200 msec.
 */

void setDelayTime(double msec) {
   delayTime = msec;
}

/* Calculates various parameters for the drawing */

static void computeGraphicsParameters(int n) {
   frameThickness = FRAME_THICKNESS_PIXELS;
   diskHeight = DISK_HEIGHT_PIXELS;
   diskMax = DISK_MAX_PIXELS;
   diskDelta = DISK_DELTA_PIXELS;
   frameWidth = 0.9 * gwp->getWidth();
   frameHeight = 2 * frameThickness + n * diskHeight;
   frameX[1] = gwp->getWidth() / 2;
   frameX[0] = frameX[1] - frameWidth * 0.3;
   frameX[2] = frameX[1] + frameWidth * 0.3;
   xBase = 0.05 * gwp->getWidth();
   yBase = (gwp->getHeight() - cSign * frameHeight) / 2;
}

/* Draws the frame */

static void drawFrame() {
   gwp->fillRect(xBase, yBase, frameWidth, frameThickness);
   for (int i = 0; i < 3; i++) {
      double x = frameX[i] - frameThickness / 2;
      gwp->fillRect(x, yBase - frameHeight, frameThickness, frameHeight);
   }
}

/* Creates disk k at the origin */

static GRect *createDisk(int k) {
   double diskWidth = diskMax - (MAX_DISKS - k) * diskDelta;
   GRect *disk = new GRect(diskWidth, diskHeight - 1);
   disk->setFilled(true);
   disk->setColor(COLOR_TABLE[k]);
   return disk;
}

/* Adds the disk to the top of the specified tower */

static void addDiskToTower(int tower, GRect *disk) {
   int level = towers[tower].size();
   double x = frameX[tower] - disk->getWidth() / 2;
   double y = yBase - (level + 1) * (disk->getHeight() + 1);
   disk->setLocation(x, y);
   towers[tower].add(disk);
}

