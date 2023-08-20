/*
 * File: MergeSort.cpp
 * -------------------
 * This file implements the merge sort algorithm.
 */

#include <iostream>
#include <vector>
#include <stdlib.h>
#include <ctime>
using namespace std;

/* Function prototypes */

void sort(vector<int> & vec);
void merge(vector<int> & vec, vector<int> & v1, vector<int> & v2);
void printVector(vector<int> & vec);

/* Main program */

int main() {
   vector<int> vec;
   int i, j;
   srand(time(0));
   for (i = 0; i <= 4000; i++) {
      j = rand() % 4000;
      vec.push_back(j);
   }
   time_t begin, end;
   double diff;
   time(&begin);
   sort(vec);
   diff = difftime(time(&end), begin);
   printVector(vec);
   cout << diff << endl;
   return 0;
}

/*
 * Function: sort
 * --------------
 * This function sorts the elements of the vector into increasing order
 * using the merge sort algorithm, which consists of the following steps:
 *
 * 1. Divide the vector into two halves.
 * 2. Sort each of these smaller vectors recursively.
 * 3. Merge the two vectors back into the original one.
 */

void sort(vector<int> & vec) {
   int n = vec.size();
   if (n <= 1) return;
   vector<int> v1;
   vector<int> v2;
   for (int i = 0; i < n; i++) {
      if (i < n / 2) {
         v1.push_back(vec[i]);
      } else {
         v2.push_back(vec[i]);
      }
   }
   sort(v1);
   sort(v2);
   vec.clear();
   merge(vec, v1, v2);
}

/*
 * Function: merge
 * ---------------
 * This function merges two sorted vectors, v1 and v2, into the vector
 * vec, which should be empty before this operation.  Because the input
 * vectors are sorted, the implementation can always select the first
 * unused element in one of the input vectors to fill the next position.
 */

void merge(vector<int> & vec, vector<int> & v1, vector<int> & v2) {
   int n1 = v1.size();
   int n2 = v2.size();
   int p1 = 0;
   int p2 = 0;
   while (p1 < n1 && p2 < n2) {
      if (v1[p1] < v2[p2]) {
         vec.push_back(v1[p1++]);
      } else {
         vec.push_back(v2[p2++]);
      }
   }
   while (p1 < n1) vec.push_back(v1[p1++]);
   while (p2 < n2) vec.push_back(v2[p2++]);
}

/*
 * Function: printVector
 * Usage: printVector(vec);
 * ------------------------
 * Prints the elements of the integer vector to the cout stream.
 */

void printVector(vector<int> & vec) {
   cout << "[";
   for (int i = 0; i < vec.size(); i++) {
      if (i > 0) cout << ", ";
      cout << vec[i];
   }
   cout << "]" << endl;
}
