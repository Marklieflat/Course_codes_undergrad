/*
 * File: TwoLetterWords.cpp
 * ------------------------
 * This program generates a list of the two-letter words.
 */

#include <iostream>
#include "lexicon.h"
using namespace std;

int main() {
   Lexicon english("EnglishWords.dat");
   for (char c0 = 'a'; c0 <= 'z'; c0++) {
      for (char c1 = 'a'; c1 <= 'z'; c1++) {
         string word = string() + c0 + c1;
         if (english.contains(word)) cout << word << endl;
      }
   }

//   Lexicon::iterator begin = english.begin();
//   Lexicon::iterator end = english.end();
//   for (Lexicon::iterator it = begin; it != end; it++) {
//      string word = *it;
//      if (word.length() == 2) {
//         cout << word << endl;
//      }
//   }
   return 0;
}
