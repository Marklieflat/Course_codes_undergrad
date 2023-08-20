/*
 * File: KLetterWords.cpp
 * ----------------------
 * This program generates a list of k-letter words for a user-supplied
 * value of k.
 */

#include <iostream>
#include "lexicon.h"
#include "simpio.h"
using namespace std;

/* Function prototypes */

void listWordsOfLengthK(const Lexicon & lex, int k);

/* Main program */

int main() {
   Lexicon english("EnglishWords.dat");
   int k = getInteger("Enter word length: ");
   listWordsOfLengthK(english, k);
   return 0;
}

/*
 * Function: listWordsOfLengthK
 * Usage: listWordsOfLengthK(lex, k);
 * ----------------------------------
 * Lists all words in the specified lexicon whose length is equal to k.
 */

void listWordsOfLengthK(const Lexicon & lex, int k) {
   foreach (string word in lex) {
      if (word.length() == k) {
         cout << word << endl;
      }
   }
}
