/*
 * File: RepeatChar.cpp
 * --------------------
 * This file tests the repeatChar function from the text.
 */

#include <iostream>
#include <string>
using namespace std;

/* Function prototypes */

string repeatChar(int n, char ch);

/* Main program */

int main() {
   cout << "Which character do you want to repeat? " << endl;
   char ch;
   cin >> ch;
   cout << "How many times do you want to repeart? " << endl;
   int re;
   cin >> re;
   cout << repeatChar(re, ch) << endl;
   return 0;
}

/*
 * Function: repeatChar
 * Usage: string str = repeatChar(n, ch);
 * --------------------------------------
 * Returns a new string consisting of n copies of the character ch.
 */

string repeatChar(int n, char ch) {
   string str = "";
   for (int i = 0; i < n; i++) {
      str += ch;
   }
   return str;
}
