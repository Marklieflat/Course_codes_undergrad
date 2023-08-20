/*
 * File: WordFrequency.cpp
 * -----------------------
 * This program computes the frequency of words in a text file.  This
 * version of the program uses a mapping function to display the entries.
 */

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cctype>
#include "filelib.h"
#include "map.h"
#include "strlib.h"
#include "vector.h"
using namespace std;

/* Function prototypes */

void countWords(istream & stream, Map<string,int> & wordCounts);
void displayWordCounts(Map<string,int> & wordCounts);
void displayEntry(string key, int value);
void extractWords(string line, Vector<string> & words);

/* Main program */

int main() {
   ifstream infile;
   Map<string,int> wordCounts;
   promptUserForFile(infile, "Input file: ");
   countWords(infile, wordCounts);
   infile.close();
   displayWordCounts(wordCounts);
   return 0;
}

/*
 * Function: countWords
 * Usage: countWords(stream, wordCounts);
 * --------------------------------------
 * Counts the words in the input stream, updating the counts in
 * the wordCounts map for each word in the stream.
 */

void countWords(istream & stream, Map<string,int> & wordCounts) {
   Vector<string> lines, words;
   readEntireFile(stream, lines);
   foreach (string line in lines) {
      extractWords(line, words);
      foreach (string word in words) {
         wordCounts[toLowerCase(word)]++;
      }
   }
}

/*
 * Function: displayWordCounts
 * Usage: displayWordCounts(wordCount);
 * ------------------------------------
 * Displays the count associated with each word in the wordCount map.
 */

void displayWordCounts(Map<string,int> & wordCounts) {
   wordCounts.mapAll(displayEntry);
}

/*
 * Function: displayEntry
 * Usage: displayEntry(key, value);
 * --------------------------------
 * Displays the key and value for a single entry in the map.
 */

void displayEntry(string key, int value) {
   cout << left << setw(15) << key
        << right << setw(5) << value << endl;
}

# include "extractWords-code.h"
