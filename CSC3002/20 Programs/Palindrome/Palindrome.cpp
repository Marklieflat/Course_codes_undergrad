/*
 * File: Palindrome.cpp
 * --------------------
 * This file uses the STL high-level operations to implement the
 * isPalindrome predicate.
 */

#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

/* Function prototypes */

bool isPalindrome(string str);

/* Main program */

int main() {
   cout << "This program tests for palindromes." << endl;
   cout << "Enter a blank line to stop." << endl;
   while (true) {
      string word;
      cout << "Enter a word: ";
      getline(cin, word);
      if (word == "") break;
      if (isPalindrome(word)) {
         cout << word << " is a palindrome." << endl;
      } else {
         cout << word << " is not a palindrome." << endl;
      }
   }
   return 0;
}

/*
 * Function: isPalindrome
 * Usage: if (isPalindrome(str)) . . .
 * -----------------------------------
 * Returns true if str is a palindrome, which is a string that
 * reads the same backwards and forwards.
 */

bool isPalindrome(string str) {
   string rev = str;
   reverse(rev.begin(), rev.end());
   return equal(str.begin(), str.end(), rev.begin());
}

