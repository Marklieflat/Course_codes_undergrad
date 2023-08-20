/*
 * File: KLetterWords.cpp
 * ----------------------
 * This program generates a list of k-letter words for a user-supplied
 * value of k.  This version of the program uses a functor class in
 * conjunction with the for_each function in the <algorithm> library.
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
 * This class defines a functor object that takes a word and prints it
 * on the console if it has length k, where k is specified by the client.
 */

class ListKLetterWords {

public:

/*
 * Constructor: ListKLetterWords
 * Usage: ListKLetterWords callback = ListKLetterWords(k);
 * -------------------------------------------------------
 * Creates a functor object that prints out its argument only if it has
 * length k.
 */

   ListKLetterWords(int k) {
      this->k = k;
   }

/*
 * Operator: ()
 * ------------
 * This operator defines the behavior of a ListKLetterWords object
 * when it is called as a function.
 */

   int operator()(string word) {
      if (word.length() == k) {
         cout << word << endl;
      }
   }

private:

/* Instance variables */

   int k;                                       /* Length of desired words */

};

/*
 * Function: listWordsOfLengthK
 * Usage: listWordsOfLengthK(lex, k);
 * ----------------------------------
 * Lists all words in the specified lexicon whose length is equal to k.
 */

void listWordsOfLengthK(const Lexicon & lex, int k) {
   for_each(lex.begin(), lex.end(), ListKLetterWords(k));
}
