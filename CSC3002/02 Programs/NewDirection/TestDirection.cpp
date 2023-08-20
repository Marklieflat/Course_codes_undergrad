/*
 * File: TestDirection.cpp
 * -----------------------
 * This file produces the for loop output shown in the text.
 */

#include <iostream>
#include "direction.h"
using namespace std;

int main() {
   for (Direction dir = NORTH; dir <= WEST; dir++) {
      cout << dir << endl;
   }
   return 0;
}
