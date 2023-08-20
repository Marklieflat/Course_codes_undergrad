/*
 * File: SortVector.cpp
 * --------------------
 * This file uses the sort function from the STL <algorithm> library to
 * sort a Vector<int>.
 */

#include <iostream>
#include <algorithm>
#include "vector.h"
using namespace std;

/* Main program */

int main() {
   Vector<int> vec;
   vec += 56, 25, 37, 58, 95, 19, 73, 30;
   cout << "Before sort: " << vec << endl;
   sort(vec.begin(), vec.end());
   cout << "After sort:  " << vec << endl;
   return 0;
}
