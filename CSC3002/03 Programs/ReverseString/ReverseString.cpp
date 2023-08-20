/*
 * File: ReverseString.cpp
 * -----------------------
 * This file tests the implementation of the function reverse,
 * which reverses the characters in a string.
 */

#include <iostream>
#include <string>
using namespace std;

/* Function prototypes */

string reverse(string str);

/* Main program */

int main() {
   cout << "This program reverses strings." << endl;
   cout << "Indicate end of input with a blank line." << endl;
   while (true) {
      cout << "Enter a string: ";
      string str;
      getline(cin, str);
      if (str == "") break;
      cout << "That string backwards is " << reverse(str) << "." << endl;
   }
   return 0;
}

/*
 * Function: reverse
 * Usage: string rev = reverse(str);
 * ---------------------------------
 * Returns a new string that consists of the characters in str in
 * reverse order.
 */

string reverse(string str) {
   string rev;
   for (int i = str.length() - 1; i >= 0; i--) {
      rev += str[i];
   }
   return rev;
}
