/*
 * File: Palindrome.cpp
 * --------------------
 * This program tests for palindromes, which are strings that read the same
 * same backwards and forwards, such as "LEVEL" or "NOON".
 */

#include <iostream>
#include <string>
using namespace std;

/* Function prototypes */

void testPalindrome(string str);
bool isPalindrome(string str);
bool isSubstringPalindrome(string & str, int p1, int p2);

/* Main program */

int main() {
   testPalindrome("");
   testPalindrome("x");
   testPalindrome("level");
   testPalindrome("noon");
   testPalindrome("abcdefghgfedcba");
   testPalindrome("0123443210");
   testPalindrome("xyzzy");
   return 0;
}

/*
 * Function: testPalindrome
 * Usage: testPalindrome(str);
 * ---------------------------
 * Tests if the specified string is a palindrome and reports the results.
 */

void testPalindrome(string str) {
   cout << "isPalindrome(\"" << str << "\") -> ";
   cout << (isPalindrome(str) ? "true" : "false" ) << endl;
}

/*
 * Function: isPalindrome
 * Usage: if (isPalindrome(str)) . . .
 * -----------------------------------
 * Returns true if str is a palindrome, which is a string that reads the
 * same backwards and forwards.  This level of the implementation is
 * simply a wrapper for isSubstringPalindrome, which does the real work.
 */

bool isPalindrome(string str) {
   return isSubstringPalindrome(str, 0, str.length() - 1);
}

/*
 * Function: isSubstringPalindrome
 * Usage: if (isSubstringPalindrome(str, p1, p2)) . . .
 * ----------------------------------------------------
 * Returns true if the characters in str from p1 to p2, inclusive, form
 * a palindrome.  This implementation uses the recursive insight that
 * all strings of length 0 or 1 are palindromes (the simple cases) and
 * that longer strings are palindromes only if their first and last
 * characters match and the remaining substring is a palindrome.
 */

bool isSubstringPalindrome(string & str, int p1, int p2) {
   if (p1 >= p2) {
      return true;
   } else {
      return str[p1] == str[p2] && isSubstringPalindrome(str, p1 + 1, p2 - 1);
   }
}
