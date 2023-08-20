/*
 * File: TestDisplayList.cpp
 * -------------------------
 * This program tests the GObject classes by storing pointers to several
 * graphical objects in a vector and then drawing them all at once.  The
 * picture is the same as the GraphicsExample.cpp program from Chapter 2.
 */

#include <iostream>
#include "gwindow.h"
#include "gobjects.h"
#include "vector.h"
using namespace std;

int main() {
   GWindow gw;
   double width = gw.getWidth();
   double height = gw.getHeight();
   GRect *rp = new GRect(width / 4, height / 4, width / 2, height / 2);
   GOval *op = new GOval(width / 4, height / 4, width / 2, height / 2);
   rp->setColor("BLUE");
   op->setColor("GRAY");
   Vector<GObject *> displayList;
   displayList.add(new GLine(0, height / 2, width / 2, 0));
   displayList.add(new GLine(width / 2, 0, width, height / 2));
   displayList.add(new GLine(width, height / 2, width / 2, height));
   displayList.add(new GLine(width / 2, height, 0, height / 2));
   displayList.add(rp);
   displayList.add(op);
   foreach (GObject *sp in displayList) {
      sp->draw(gw);
   }
   foreach (GObject *sp in displayList) {
      delete sp;
   }
   displayList.clear();
   return 0;
}
