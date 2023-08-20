/*
 * File: StartsAndEndsWith.cpp
 * ---------------------------
 * This program tests the StartsWith and EndsWith functions.
 */

#include <iostream>
#include <string>
using namespace std;

/* Function prototypes */

void testStartsWith(string str, string prefix, bool expected);
void testEndsWith(string str, string prefix, bool expected);
bool startsWith(string str, string prefix);
bool endsWith(string str, string suffix);

/* Main program */

int main() {
   testStartsWith("start", "", true);
   testStartsWith("start", "star", true);
   testStartsWith("start", "start", true);
   testStartsWith("start", "startx", false);
   testEndsWith("start", "", true);
   testEndsWith("start", "tart", true);
   testEndsWith("start", "start", true);
   testEndsWith("start", "xstart", false);
}

/*
 * Functions: testStartsWith, testEndsWith
 * ---------------------------------------
 * These functions encapsulate a single test of their respective functions.
 */

void testStartsWith(string str, string prefix, bool expected) {
   bool result = startsWith(str, prefix);
   cout << "startsWith(\"" << str << "\", \"" << prefix << "\") -> ";
   cout << boolalpha << result;
   if (result != expected) cout << " (should be " << expected << ")";
   cout << endl;
}

void testEndsWith(string str, string prefix, bool expected) {
   bool result = endsWith(str, prefix);
   cout << "endsWith(\"" << str << "\", \"" << prefix << "\") -> ";
   cout << boolalpha << result;
   if (result != expected) cout << " (should be " << expected << ")";
   cout << endl;
}

/*
 * Function: startsWith
 * Usage: if (startsWith(str, prefix)) . . .
 * -----------------------------------------
 * Returns <code>true</code> if the string <code>str</code> starts with
 * the specified prefix.
 */

bool startsWith(string str, string prefix) {
   if (str.length() < prefix.length()) return false;
   for (int i = 0; i < prefix.length(); i++) {
      if (str[i] != prefix[i]) return false;
   }
   return true;
}

/*
 * Function: endsWith
 * Usage: if (endsWith(str, suffix)) . . .
 * ---------------------------------------
 * Returns <code>true</code> if the string <code>str</code> ends with
 * the specified suffix.
 */

bool endsWith(string str, string suffix) {
   if (str.length() < suffix.length()) return false;
   int start = str.length() - suffix.length();
   for (int i = 0; i < suffix.length(); i++) {
      if (str[start + i] != suffix[i]) return false;
   }
   return true;
}
