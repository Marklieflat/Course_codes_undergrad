/*
 * File: DumpWordFrequency.cpp
 * ---------------------------
 * This program dumps a listing of word frequency to a text file.  This
 * version of the program uses a functor to combine both the output
 * stream and the reporting function.
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
void dumpWordCounts(ostream & outfile, Map<string,int> & wordCounts);
void extractWords(string line, Vector<string> & words);

/*
 * Class: DumpEntry
 * ----------------
 * This class is a C++ functor that writes the current key-value pair
 * to the output stream whose address is stored in osp.
 */

class DumpEntry {

public:

   DumpEntry(ostream & outfile) {
      osp = &outfile;
   }

   void operator()(const string & key, int value) {
      *osp << left << setw(15) << key
           << right << setw(5) << value << endl;
   }

private:

   ostream *osp;

};

/* Main program */

int main() {
   ifstream infile;
   ofstream outfile;
   Map<string,int> wordCounts;
   promptUserForFile(infile, "Input file: ");
   promptUserForFile(outfile, "Output file: ");
   countWords(infile, wordCounts);
   infile.close();
   dumpWordCounts(outfile, wordCounts);
   outfile.close();
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
 * Function: dumpWordCounts
 * Usage: dumpWordCounts(outfile, wordCount);
 * ------------------------------------------
 * Writes to outfile a table of the words in the wordCount map along
 * with the associated counts.
 */

void dumpWordCounts(ostream & outfile, Map<string,int> & wordCounts) {
   wordCounts.mapAll(DumpEntry(outfile));
}

# include "extractWords-code.h"
