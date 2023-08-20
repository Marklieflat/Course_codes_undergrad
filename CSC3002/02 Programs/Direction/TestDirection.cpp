/*
 * File: TestDirection.cpp
 * -----------------------
 * This file tests the Direction definition and functions as they
 * appear in the text.
 */

#include <iostream>
#include "direction.h"
// #include "direction.cpp"
using namespace std;

int main() {
   for (Direction dir = NORTH; dir <= WEST; dir = Direction(dir + 1)) {
      cout << "leftFrom(" << directionToString(dir) << ") -> "
           << directionToString(leftFrom(dir)) << endl;
      cout << "rightFrom(" << directionToString(dir) << ") -> "
           << directionToString(rightFrom(dir)) << endl;
   }
   return 0;
}
