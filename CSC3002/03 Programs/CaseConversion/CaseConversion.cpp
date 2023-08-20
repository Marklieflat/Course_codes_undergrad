/*
 * File: CaseConversion.cpp
 * ------------------------
 * This file defines several functions that use the <cctype> library
 * for case conversions.  These functions are included in the Stanford
 * "strlib.h" library.
 */

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

/* Rename the functions so that they don't collide with the library */

#define toUpperCaseInPlace _toUpperCaseInPlace
#define toUpperCase _toUpperCase
#define toLowerCaseInPlace _toLowerCaseInPlace
#define toLowerCase _toLowerCase
#define equalsIgnoreCase _equalsIgnoreCase

/* Function prototypes */

void toUpperCaseInPlace(string & str);
string toUpperCase(string str);
void toLowerCaseInPlace(string & str);
string toLowerCase(string str);
bool equalsIgnoreCase(string s1, string s2);
string toUpperCaseSlowly(string str);

/* Main program */

int main() {
   string str = "Hello, world";
   cout << "if str = \"" << str << "\"" << endl;
   toUpperCaseInPlace(str);
   cout << "calling toUpperCaseInPlace(str) leaves str = \""
        << str << "\"" << endl;
   toLowerCaseInPlace(str);
   cout << "calling toLowerCaseInPlace(str) leaves str = \""
        << str << "\"" << endl;
   cout << "toUpperCase(str) -> \"" << toUpperCase(str) << "\"";
   cout << " but str is still \"" << str << "\"" << endl << endl;
   cout << "toUpperCase(\"abc\") -> \"" << toUpperCase("abc") << "\"" << endl;
   cout << "toUpperCase(\"Ab.\") -> \"" << toUpperCase("Ab.") << "\"" << endl;
   cout << "toLowerCase(\"ABC\") -> \"" << toLowerCase("ABC") << "\"" << endl;
   cout << "toLowerCase(\"Ab.\") -> \"" << toLowerCase("Ab.") << "\"" << endl;
   cout << "equalsIgnoreCase(\"abc\", \"AbC\") -> "
        << (equalsIgnoreCase("abc", "AbC") ? "true" : "false") << endl;
   cout << "toUpperCaseSlowly(\"abc\") -> \"" << toUpperCaseSlowly("abc")
        << "\"" << endl;
   cout << "toUpperCaseSlowly(\"Ab.\") -> \"" << toUpperCaseSlowly("Ab.")
        << "\"" << endl;
   return 0;
}

/*
 * Function: toUpperCaseInPlace
 * Usage: toUpperCaseInPlace(str);
 * -------------------------------
 * Changes the argument string by converting every lowercase character
 * to its uppercase counterpart.
 */

void toUpperCaseInPlace(string & str) {
   for (int i = 0; i < str.length(); i++) {
      str[i] = toupper(str[i]);
   }
}

/*
 * Function: toUpperCase
 * Usage: string upper = toUpperCase(str);
 * ---------------------------------------
 * Creates a new string by converting every lowercase character in str
 * to its uppercase counterpart.
 */

string toUpperCase(string str) {
   toUpperCaseInPlace(str);
   return str;
}

/*
 * Function: toLowerCaseInPlace
 * Usage: toLowerCaseInPlace(str);
 * -------------------------------
 * Changes the argument string by converting every uppercase character
 * to its lowercase counterpart.
 */

void toLowerCaseInPlace(string & str) {
   for (int i = 0; i < str.length(); i++) {
      str[i] = tolower(str[i]);
   }
}

/*
 * Function: toLowerCase
 * Usage: string lower = toLowerCase(str);
 * ---------------------------------------
 * Creates a new string by converting every uppercase character in str
 * to its lowercase counterpart.
 */

string toLowerCase(string str) {
   toLowerCaseInPlace(str);
   return str;
}

/*
 * Function: equalsIgnoreCase
 * Usage: if (equalsIgnoreCase(s1, s2)) . . .
 * ------------------------------------------
 * Returns true if s1 and s2 are equal except for differences in case.
 */

bool equalsIgnoreCase(string s1, string s2) {
   if (s1.length() != s2.length()) return false;
   for (int i = 0; i < s1.length(); i++) {
      if (tolower(s1[i]) != tolower(s2[i])) return false;
   }
   return true;
}

#undef toUpperCase
#define toUpperCase toUpperCaseSlowly

/*
 * Function: toUpperCase
 * Usage: string upper = toUpperCase(str);
 * ---------------------------------------
 * Creates a new string by converting every lowercase character in str
 * to its uppercase counterpart.  This version is considerably less
 * efficient but illustrates the string patterns.
 */

string toUpperCase(string str) {
   string result = "";
   for (int i = 0; i < str.length(); i++) {
      result += toupper(str[i]);
   }
   return result;
}
