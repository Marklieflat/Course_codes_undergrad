/*
 * File: KLetterWords.cpp
 * ----------------------
 * This program generates a list of k-letter words for a user-supplied
 * value of k.  This version of the program uses a function class to
 * define the callback function.
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
 * Class: ListKLetterWords
 * -----------------------
 * This class defines a function object that takes a word and prints it
 * on the console if it has length k, where k is specified by the client.
 */

class ListKLetterWords {

public:

/*
 * Constructor: ListKLetterWords
 * Usage: ListKLetterWords fn = ListKLetterWords(k);
 * -------------------------------------------------
 * Creates a function object that prints its argument only if it has
 * length k.  This function object is used as the argument to the mapAll
 * method in the Lexicon class.
 */

   ListKLetterWords(int k) {
      this->k = k;
   }

/*
 * Operator: ()
 * ------------
 * Defines the behavior of a ListKLetterWords object when it is called
 * as a function.
 */

   int operator()(string word) {
      if (word.length() == k) {
         cout << word << endl;
      }
   }

private:

/* Instance variables */

   int k;     /* Length of desired words */

};

/*
 * Function: listWordsOfLengthK
 * Usage: listWordsOfLengthK(lex, k);
 * ----------------------------------
 * Lists all words in the specified lexicon whose length is equal to k.
 */

void listWordsOfLengthK(const Lexicon & lex, int k) {
   lex.mapAll(ListKLetterWords(k));
}
