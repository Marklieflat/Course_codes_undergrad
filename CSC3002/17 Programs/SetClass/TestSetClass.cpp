/*
 * File: TestSetClass.cpp
 * ----------------------
 * This file contains a self-narrating test of the Set class.
 */

#include <iostream>
#include <sstream>
#include <string>
#include "console.h"
#include "set.h"
#include "strlib.h"
using namespace std;

/* Function prototypes */

void testCharSet();
Set<char> charSet(const string & str);
string charString(const Set<char> & set);

/* Main program */

int main() {
   cout << boolalpha;
   testCharSet();
   return 0;
}

void testCharSet() {
   Set<char> lcletters = charSet("abcdefghijklmnopqrstuvwxyz");
   Set<char> vowels = charSet("aeiou");
   Set<char> consonants = charSet("bcdfghjklmnpqrstvwxyz");
   Set<char> onePointTiles = charSet("aeilnorstu");
   Set<char> highPointTiles = charSet("kjxqz");
   Set<char> descenders = charSet("gjpqy");
   Set<char> empty;
   cout << "lcletters.size() = " << lcletters.size() << endl;
   cout << "vowels.size() = " << vowels.size() << endl;
   cout << "charString(consonants) = " << charString(consonants) << endl;
   cout << "vowels.contains('a') = " << vowels.contains('a') << endl;
   cout << "vowels.contains('x') = " << vowels.contains('x') << endl;
   cout << "empty.contains('x') = " << empty.contains('x') << endl;
   cout << "vowels.isSubsetOf(onePointTiles) = "
        << vowels.isSubsetOf(onePointTiles) << endl;
   cout << "vowels.isSubsetOf(highPointTiles) = "
        << vowels.isSubsetOf(highPointTiles) << endl;
   cout << "empty.isSubsetOf(highPointTiles) = "
        << empty.isSubsetOf(highPointTiles) << endl;
   cout << "empty.isEmpty() = " << empty.isEmpty() << endl;
   cout << "consonants.isEmpty() = " << consonants.isEmpty() << endl;
   cout << "charString(highPointTiles + vowels) = "
        << charString(highPointTiles + vowels) << endl;
   cout << "charString(highPointTiles * vowels) = "
        << charString(highPointTiles * vowels) << endl;
   cout << "charString(onePointTiles * vowels) = "
        << charString(onePointTiles * vowels) << endl;
   cout << "charString(onePointTiles - vowels) = "
        << charString(onePointTiles - vowels) << endl;
}

/*
 * Function: charSet
 * Usage: Set<char> set = charSet(str);
 * ------------------------------------
 * Creates a Set<char> from a string by adding each character in turn.
 */

Set<char> charSet(const string & str) {
   Set<char> set;
   int nChars = str.length();
   for (int i = 0; i < nChars; i++) {
      set.add(str[i]);
   }
   return set;
}

/*
 * Function: charString
 * Usage: string str = charString(set);
 * ------------------------------------
 * Creates a string that lists the elements of the set in ASCII order.
 * This implementation cycles through the possible characters because the
 * Set implementation in this chapter does not yet implement the range-based
 * for loop.
 */

string charString(const Set<char> & set) {
   string str = "{";
   for (int i = 0; i <= 256; i++) {
      char ch = char(i);
      if (set.contains(ch)) {
      	if (str.length() > 1) str += ", ";
         str += ch;
   	}
   }
   str += "}";
   return str;
}
