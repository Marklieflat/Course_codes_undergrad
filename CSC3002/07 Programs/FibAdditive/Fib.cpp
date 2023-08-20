/*
 * File: Fib.cpp
 * -------------
 * This program lists the terms in the Fibonacci sequence with
 * indices ranging from MIN_INDEX to MAX_INDEX.
 */

#include <iostream>
#include <iomanip>
using namespace std;

/* Constants */

const int MIN_INDEX  = 0;   /* Index of first term to generate */
const int MAX_INDEX = 20;   /* Index of last term to generate  */

/* Private function prototypes */

int fib(int n);
int additiveSequence(int n, int t0, int t1);

/* Main program */

int main() {
   cout << "This program lists the Fibonacci sequence." << endl;
   for (int i = MIN_INDEX; i <= MAX_INDEX; i++) {
      if (i < 10) cout << " ";
      cout << "fib(" << i << ")";
      cout << " = " << setw(4) << fib(i) << endl;
   }
   return 0;
}

/*
 * Function: fib
 * Usage: int f = fib(n);
 * ----------------------
 * Returns the nth term in the Fibonacci sequence.  This version
 * uses a helper function that implements a more general strategy
 * for computing additive sequences.
 */

int fib(int n) {
   return additiveSequence(n, 0, 1);
}

/*
 * Function: additiveSequence
 * Usage: int k = additiveSequence(n, t0, t1);
 * -------------------------------------------
 * Returns the nth term in a general additive sequence in which
 *
 *     t(n) = t(n - 1) + t(n)
 *
 * and the first two terms are t0 and t1.  This implementation is
 * more efficient than the most straightforward recursive strategy
 * and makes use of the fact that the nth term in an additive
 * sequence beginning at t0 and t1 is the (n - 1)st term in a
 * sequence beginning at t1 and t0 + t1.
 */

int additiveSequence(int n, int t0, int t1) {
   if (n == 0) return t0;
   if (n == 1) return t1;
   return additiveSequence(n - 1, t1, t0 + t1);
   //return additiveSequence(n - 1, t0, t1)+additiveSequence(n - 2, t0, t1);
}
