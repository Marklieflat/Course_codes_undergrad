/*
 * File: TwoLetterWords.cpp
 * ------------------------
 * This program generates a list of the two-letter words.  This version
 * of the program uses the mapAll method in the Lexicon class to list
 * the words.
 */

#include <iostream>
#include "lexicon.h"
using namespace std;

/* Function prototypes */

void printTwoLetterWords(string word);

/* Main program */

int main() {
   Lexicon english("EnglishWords.dat");
   english.mapAll(printTwoLetterWords);
   return 0;
}

/*
 * Callback function: printTwoLetterWords
 * Usage: printTwoLetterWords(word);
 * ---------------------------------
 * Prints the value of word on cout if it is a two-letter word.
 */

void printTwoLetterWords(string word) {
   if (word.length() == 2) {
      cout << word << endl;
   }
}
