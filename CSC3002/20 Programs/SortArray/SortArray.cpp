/*
 * File: SortArray.cpp
 * -------------------
 * This file uses the sort function from the STL <algorithm> library to
 * sort a C++ array.
 */

#include <iostream>
#include <algorithm>
using namespace std;

/* Main program */

int main() {
   int array[] = { 56, 25, 37, 58, 95, 19, 73, 30 };
   int n = 8;
   cout << "Before sort: ";
   for (int i = 0; i < n; i++) {
      if (i > 0) cout << ", ";
      cout << array[i];
   }
   cout << endl;
   sort(array, array + n);
   cout << "After sort:  ";
   for (int i = 0; i < n; i++) {
      if (i > 0) cout << ", ";
      cout << array[i];
   }
   cout << endl;
   return 0;
}
