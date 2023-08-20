/*
 * File: CountNegative.cpp
 * -----------------------
 * This program counts the negative values in a Vector<int> by combining
 * features from the <algorithm> and <functional> libraries.
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include "vector.h"
using namespace std;

int main() {
   Vector<int> v;
   v += -1, 0, 17, -4, 11, -2;
   int negCount = count_if(v.begin(), v.end(), bind2nd(less<int>(), 0));
   cout << v << " contains " << negCount << " negative values." << endl;
   return 0;
}

