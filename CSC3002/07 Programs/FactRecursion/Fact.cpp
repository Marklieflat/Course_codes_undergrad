/*
 * File: Fact.cpp
 * --------------
 * This file generates a list of factorials.  The test program
 * stops when the value of fact(n) is smaller than its predecessor,
 * which means that an overflow must have occurred.
 */

#include <iostream>
#include <iomanip>
using namespace std;

/* Function prototypes */

int fact(int n);

/* Main program */

int main() {
   for (int i = 0; i < 2 || fact(i) > fact(i - 1); i++) {
      cout << setw(2) << i << "! = " << setw(10) << fact(i) << endl;
   }
   return 0;
}

/*
 * Function: fact
 * Usage: int nfact = fact(n);
 * ---------------------------
 * Computes the factorial of n using the following recursive formulation:
 *
 *    fact(0) = 1
 *    fact(n) = n * fact(n - 1)
 */

int fact(int n) {
   if (n == 0) {
      return 1;
   } else {
      return n * fact(n - 1);
   }
}
