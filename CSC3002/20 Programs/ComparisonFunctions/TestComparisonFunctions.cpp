/*
 * File: TestComparisonFunctions.cpp
 * ---------------------------------
 * This program tests various comparison functions.
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include "strlib.h"
#include "vector.h"
using namespace std;

/* Function prototypes */

bool lessIgnoringCase(string s1, string s2);
bool isShorter(string s1, string s2);

/* Main program */

int main() {
   Vector<int> vec;
   vec += 31, 41, 59, 26, 53, 58, 97, 93;
   sort(vec.begin(), vec.end(), greater<int>());
   cout << "greater: " << vec << endl;
   Vector<string> test;
   test += "ABC", "abcd", "AbC", "a", "cba", "CAB", "cabinet";
   sort(test.begin(), test.end(), lessIgnoringCase);
   cout << "lessIgnoringCase: " << test << endl;
   sort(test.begin(), test.end(), isShorter);
   cout << "isShorter: " << test << endl;
   return 0;
}

/*
 * Function: lessIgnoringCase
 * Usage: if (lessIgnoringCase(s1, s2)) . . .
 * ------------------------------------------
 * Returns true if s1 comes before s2 when compared without regard to case.
 * This implementation adopts the simple but inefficient tactic of
 * converting both strings to lowercase and then comparing them
 * using the relational operators for the string class.
 */

bool lessIgnoringCase(string s1, string s2) {
   return toLowerCase(s1) < toLowerCase(s2);
}

/*
 * Function: isShorter
 * Usage: if (isShorter(s1, s2)) . . .
 * -----------------------------------
 * Returns true if s1 is shorter than s2.
 */

bool isShorter(string s1, string s2) {
   return s1.length() < s2.length();
}
