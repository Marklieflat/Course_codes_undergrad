/*
 * File: VectorExamples.cpp
 * ------------------------
 * This file checks various examples from the text to make sure
 * they work as advertised.
 */

#include <iostream>
#include "vector.h"
using namespace std;

/* Function prototypes */

void iterateBackwards(const Vector<int> & vec);
void iterateForwardByTwos(const Vector<int> & vec);

/* Main program */

int main() {
   Vector<int> vec;
   vec += 1, 2, 3, 4, 5, 6, 7, 8, 9;
   cout << "The vector backwards:" << endl;
   iterateBackwards(vec);
   cout << endl;
   cout << "The elements with even indices (odd values):" << endl;
   iterateForwardByTwos(vec);
   vec.insert(0, 0);
   cout << endl;
   cout << "The elements with even indices (even values):" << endl;
   iterateForwardByTwos(vec);
   return 0;
}

void iterateBackwards(const Vector<int> & vec) {
   Vector<int>::iterator it = vec.end();
   while (it != vec.begin()) {
      cout << *--it << endl;
   }
}

void iterateForwardByTwos(const Vector<int> & vec) {
   for (Vector<int>::iterator it = vec.begin();
                              it < vec.end();
                              it += 2) {
      cout << *it << endl;
   }
}
