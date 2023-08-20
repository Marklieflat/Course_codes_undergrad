/*
 * File: Acronym.cpp
 * -----------------
 * This program generates and displays acronyms.
 */

#include <cctype>
#include <iostream>
#include <string>
using namespace std;

/* Function prototypes */

string acronym(string str);

/* Main program */

int main() {
   cout << "Program to generate acronyms" << endl;
   while (true) {
      cout << "Enter string: ";
      string str;
      getline(cin, str);
      if (str == "") break;
      cout << "The acronym is \"" << acronym(str) << "\"" << endl;
   }
   return 0;
}

/*
 * Function: acronym
 * Usage: string acronym = acronym(str);
 * -------------------------------------
 * Generates the acronym for the given string, which is formed
 * by combining the first letters from a series of words, as in
 *
 *   "self-contained underwater breathing apparatus" -> "scuba"
 *
 * This implementation detects word boundaries by searching through
 * the string for alphabetic characters that are not preceded by
 * earlier alphabetic characters.  On finding an alphabetic character,
 * the code sets the inWord flag to record the fact that the beginning
 * of this word has already been found.
 */

string acronym(string str) {
   string result = "";
   bool inWord = false;
   int nc = str.length();
   for (int i = 0; i < nc; i++) {
      char ch = str[i];
      if (inWord) {
         if (!isalpha(ch)) inWord = false;
      } else {
         if (isalpha(ch)) {
            result += ch;
            inWord = true;
         }
      }
   }
   return result;
}
