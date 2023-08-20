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
   Lexicon::iterator it = english.begin();
   while (it != english.end()) {
      if (it->length() == 2) {
         cout << *it << endl;
      }
      it++;
   }
   return 0;
}
