/*
 * File: Coastline.cpp
 * -------------------
 * This program draws a fractal coastline.  This version of the
 * program uses an equilateral wedge, as in the snowflake fractal.
 */

#include <iostream>
#include <cmath>
#include "gtypes.h"
#include "gwindow.h"
#include "random.h"
#include "simpio.h"

/* Constants */

const double LINE_FRACTION = 0.9;

/* Function prototypes */

GPoint drawCoastlineSegment(GWindow & gw, GPoint pt,
                            double len, double theta, int order);

/* Main program */

int main() {
   GWindow gw(600, 400);
   int order = getInteger("Enter order of fractal: ");
   double x0 = gw.getWidth() * (1 - LINE_FRACTION) / 2;
   double y0 = gw.getHeight() / 2;
   double len = gw.getWidth() * LINE_FRACTION;
   drawCoastlineSegment(gw, GPoint(x0, y0), len, 0, order);
   return 0;
}

/*
 * Function: drawCoastlineSegment
 * Usage: GPoint end = drawCoastlineSegment(gw, pt, len, theta, order);
 * --------------------------------------------------------------------
 * Draws a fractal edge starting from the point pt and then extending
 * len units in direction theta.  If order is 0, the fractal edge is
 * a straight line.  If order is greater than zero, the edge is divided
 * into four line segments, each of which is a fractal edge of the next
 * lower order.  The function returns the end point of the line.
 * The only difference between this function and drawFractalLine is
 * that the direction of the fractal bump is chosen randomly.
 */

GPoint drawCoastlineSegment(GWindow & gw, GPoint pt,
                            double len, double theta, int order) {
   if (order == 0) {
      return gw.drawPolarLine(pt, len, theta);
   } else {
      double dTheta = randomChance(0.5) ? +60 : -60;
      pt = drawCoastlineSegment(gw, pt, len / 3, theta, order - 1);
      pt = drawCoastlineSegment(gw, pt, len / 3, theta + dTheta, order - 1);
      pt = drawCoastlineSegment(gw, pt, len / 3, theta - dTheta, order - 1);
      return drawCoastlineSegment(gw, pt, len / 3, theta, order - 1);
   }
}
