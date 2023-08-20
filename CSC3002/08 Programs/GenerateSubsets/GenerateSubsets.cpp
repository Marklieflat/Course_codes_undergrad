/*
 * GenerateSubsets.cpp
 * -------------------
 * This program generates all subsets of a set, where the set
 * is represented as a string of individual letters.
 */

#include <iostream>
#include <string>
#include "console.h"
#include "simpio.h"
#include "vector.h"
using namespace std;

/* Function prototypes */

Vector<string> generateSubsets(string set);

/* Main program */

int main() {
   string str = getLine("Enter set as a string of characters: ");
   Vector<string> subsets = generateSubsets(str);
   for (string s : subsets) {
      cout << '"' << s << '"' << endl;
   }
   return 0;
}

/*
 * Function: generateSubsets
 * Usage: Vector<string> subsets = generateSubsets(str);
 * -----------------------------------------------------
 * Generates a vector containing all subsets of the specified
 * set.  Each set is represented as a string in which the letters
 * correspond to the individual elements.  Thus, the string
 * "abd" represents the set { a, b, d }.
 */

Vector<string> generateSubsets(string set) {
   Vector<string> result;
   if (set == "") {
      result.add("");
   } else {
      result = generateSubsets(set.substr(1));
      int n = result.size();
      for (int i = 0; i < n; i++) {
         result.add(set[0] + result[i]);
      }
   }
   return result;
}
