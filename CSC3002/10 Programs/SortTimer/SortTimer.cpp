/*
 * File: SortTimer.cpp
 * -------------------
 * This file generates timing information for the sort algorithm used for
 * the definition of sort.  Note that this implementation is read in by
 * the preprocessor directly from its original source file.
 */

#include <ctime>
#include <iostream>
#include "random.h"
#include "vector.h"
//#include "console.h"
using namespace std;

/* Function prototypes */

void sortTimer(int nElements, int nRepetitions, int nTrials);
double sortTrial(int nElements, int nRepetitions);
double timeTrial(Vector<int> & vec, int nRepetitions, bool doSort);
void sort(Vector<int> & vec);

/*
 * Main program
 * ------------
 * This function consists of a series of calls to
 *
 *    sortTimer(nElements, nRepetitions, nTrials)
 *
 * in which nElements is the number of elements in the array,
 * nRepetitions is the number of times the array is sorted during
 * each trial, and nTrials is the number of independent trials
 * made for that element count.
 */

int main() {
   sortTimer(10, 100000, 5);
   sortTimer(50, 10000, 5);
   sortTimer(100, 1000, 5);
   sortTimer(500, 100, 5);
   sortTimer(1000, 10, 5);
   sortTimer(5000, 10, 5);
   sortTimer(10000, 2, 5);
   sortTimer(50000, 2, 5);
   sortTimer(100000, 2, 5);
   return 0;
}

/*
 * Function: sortTimer
 * Usage: sortTimer(nElements, nRepetitions, nTrials);
 * ---------------------------------------------------
 * Runs a timing experiment for the current sort algorithm where
 * nElements is the number of elements in the array, nRepetitions
 * is the number of times the array is sorted during each trial,
 * and nTrials is the number of independent trials made for that
 * number of elements.
 */

void sortTimer(int nElements, int nRepetitions, int nTrials) {
   for (int i = 0; i < nTrials; i++) {
      double time = sortTrial(nElements, nRepetitions);
      cout << "sortTrial(" << nElements << ") = " << time << endl;
   }
}

/*
 * Function: sortTrial
 * Usage: double time = sortTrial(nElements, nRepetitions);
 * --------------------------------------------------------
 * Runs a single trial using the current sort algorithm.  As before,
 * nElements is the number of elements in the array, and nRepetitions
 * is the number of times the array is sorted during each trial.
 */

double sortTrial(int nElements, int nRepetitions) {
   Vector<int> vec;
   for (int i = 0; i < nElements; i++) {
      vec.add(randomInteger(1, nElements));
   }
   double overhead = timeTrial(vec, nRepetitions, false);
   double total =  timeTrial(vec, nRepetitions, true);
   return total - overhead;
}

/*
 * Function: timeTrial
 * Usage: double time = timeTrial(vec, nRepetitions, doSort);
 * ----------------------------------------------------------
 * Runs the actual timing trial after the elements have been initialized.
 * To determine how much time is spent in the framework itself, the
 * doSort flag determines whether the sort function is called.  By
 * subtracting the time required without sorting from the time required
 * with sorting, the function gives an estimate of the sort time.
 */

double timeTrial(Vector<int> & vec, int nRepetitions, bool doSort) {
   double start = double(clock()) / CLOCKS_PER_SEC;
   for (int rep = 0; rep < nRepetitions; rep++) {
      Vector<int> copy = vec;
      if (doSort) sort(copy);
   }
   double elapsed = double(clock()) / CLOCKS_PER_SEC - start;
   return elapsed / nRepetitions;
}

/*
 * Read in the sort algorithm.  This section requires renaming the main
 * function so that it doesn't interfere with the one in this file.
 */

#ifdef main
#  undef main
#endif

#define main dummyMain

#include "../SelectionSort/SelectionSort.cpp"
//#include "../MergeSort/MergeSort.cpp"
//#include "../QuickSort/QuickSort.cpp"
