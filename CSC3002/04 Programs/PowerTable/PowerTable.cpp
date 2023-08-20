/*
 * File: PowerTable.cpp
 * --------------------
 * This program generates a table comparing values
 * of the functions n^2 and 2^n.
 */

#include <iostream>
#include <iomanip>
using namespace std;

/* Private function prototypes */

int raiseToPower(int base, int k);
double raiseToPower(double base, int k);

/* Main program */

int main() {
   cout << "    |    2  |     N   " << endl;
   cout << "  N |   N   |    2    " << endl;
   cout << "----+-------+---------" << endl;
   cout << setprecision(2) << uppercase;
   int delta = 1;
   for (int i = 0; i <= 100; i += delta) {
      cout << setw(3) << i << " |" ;
      cout << setw(6) << raiseToPower(i, 2) << " |" ;
      if (i < 30) {
         cout << setw(8) << raiseToPower(2, i) << endl;
      } else {
         cout << setw(8) << raiseToPower(2.0, i) << endl;
      }
      if (i == 10) delta = 10;
   }
   return 0;
}

/*
 * Function: raiseToPower
 * Usage: power = raiseToPower(base, k);
 * -------------------------------------
 * Returns base raised to the kth power.  This function is
 * overloaded to accept either an int or a double for base.
 */

int raiseToPower(int base, int k) {
   int result = 1;
   for (int i = 0; i < k; i++) {
      result *= base;
   }
   return result;
}

double raiseToPower(double base, int k) {
   double result = 1;
   for (int i = 0; i < k; i++) {
      result *= base;
   }
   return result;
}
