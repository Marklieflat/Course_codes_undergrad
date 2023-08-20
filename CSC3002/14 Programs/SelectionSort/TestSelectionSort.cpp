/*
 * File: TestSelectionSort.cpp
 * ---------------------------
 * This file implements a very simple test of the template-based
 * selection sort algorithm that shows it works with two kinds of
 * arrays.
 */

#include <iostream>
#include "sort.h"
using namespace std;

/* Function prototypes */
template <typename ValueType>
void printArray(ValueType array[], int n);

/* Main program */

int main() {
   int intArray[] = { 31, 41, 59, 26, 53, 58, 97, 93 };
   cout << "intArray: ";
   printArray(intArray, 8);
   sort(intArray, 8);
   cout << "Sorted intArray: ";
   printArray(intArray, 8);
   double doubleArray[] = { 3.1, 4.1, 5.9, 2.6, 5.3, 5.8, 9.7, 9.3 };
   cout << "doubleArray: ";
   printArray(doubleArray, 8);
   sort(doubleArray, 8);
   cout << "Sorted doubleArray: ";
   printArray(doubleArray, 8);
   char charArray[] = "TEmplate";
   cout << "charArray: ";
   printArray(charArray, 8);
   sort(charArray, 8);
   cout << "Sorted charArray: ";
   printArray(charArray, 8);
   return 0;
}

template <typename ValueType>
void printArray(ValueType array[], int n) {
   cout << "{";
   for (int i = 0; i < n; i++) {
      if (i > 0) cout << ", ";
      cout << array[i];
   }
   cout << "}" << endl;
}
