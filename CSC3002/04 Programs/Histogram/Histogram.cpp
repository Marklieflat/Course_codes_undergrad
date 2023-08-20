/*
 * File: Histogram.cpp
 * -------------------
 * This program generates a histogram of scores from an input file.
 */

#include <iostream>
#include <iomanip>
#include <fstream>
#include "filelib.h"
#include "strlib.h"
#include "console.h"
using namespace std;

/* Constants */

static const int N_RANGES = 11;

/* Main program */

int main() {
   ifstream infile;
   Vector<string> buckets(N_RANGES);
   promptUserForFile(infile, "Score file: ");
   string line;
   while (getline(infile, line)) {
      int score = stringToInteger(line);
      if (score < 0 || score > 100) error("Score is out of range");
      buckets[score / 10] += "*";
   }
   infile.close();
   for (int i = 0; i < N_RANGES; i++) {
      cout << setw(3) << 10 * i << ": " << buckets[i] << endl;
   }
   return 0;
}
