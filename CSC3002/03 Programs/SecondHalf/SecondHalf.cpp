/*
 * File: SecondHalf.cpp
 * --------------------
 * This program tests the secondHalf function.
 */

#include <iostream>
#include <string>
using namespace std;

/* Function prototypes */

string secondHalf(string str);

/* Main program */

int main() {
   string str = "";
   char digit = '1';
   while (str.length() < 10) {
      cout << "secondHalf(" << '"' << str << '"' << ") = ";
      cout << '"' << secondHalf(str) << '"' << endl;
      str += digit;
      digit++;
   }
   return 0;
}

/*
 * Function: secondHalf
 * Usage: string part2 = secondHalf(str);
 * --------------------------------------
 * Returns the second half of a string, which includes the middle
 * character if the length of the string is odd.
 */

string secondHalf(string str) {
   return str.substr(str.length() / 2);
}
