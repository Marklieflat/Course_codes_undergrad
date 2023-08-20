/*
 * File: SelectionSort.cpp
 * -----------------------
 * This file implements the selection sort algorithm using functions
 * from the STL <algorithm> library.
 */

#include <iostream>
#include <algorithm>
#include "vector.h"
using namespace std;

/* Prototypes */

void sort(Vector<int> & vec);

/* Main program */

int main() {
   Vector<int> vec;
   vec += 56, 25, 37, 58, 95, 19, 73, 30;
   cout << "Before sort: " << vec << endl;
   sort(vec.begin(), vec.end());
   cout << "After sort:  " << vec << endl;
   random_shuffle(vec.begin(), vec.end());
   cout << "Before sort: " << vec << endl;
   sort(vec.begin(), vec.end());
   cout << "After sort:  " << vec << endl;
   return 0;
}

/*
 * Function: sort
 * Usage: sort(vec);
 * -----------------
 * Sorts the elements in the vector by combining high-level operations
 * from the <algorithm> interface.  The selection sort algorithm is
 * described in Chapter 10.
 */

void sort(Vector<int> & vec) {
   for (Vector<int>::iterator lh = vec.begin(); lh != vec.end(); lh++) {
      Vector<int>::iterator rh = min_element(lh, vec.end());
      iter_swap(lh, rh);
   }
}
