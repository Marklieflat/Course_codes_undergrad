/*
 * File: OddEven.cpp
 * -----------------
 * This program uses mutual recursion to implement the functions
 * isOdd and isEven for nonnegative numbers.
 */

#include <iostream>
using namespace std;

/* Function prototypes */

bool isOdd(unsigned int n);
bool isEven(unsigned int n);
void isOddEven(unsigned int n);

/* Main program */

int main() {
   isOddEven(0);
   isOddEven(1);
   isOddEven(10);
   isOddEven(11);
   return 0;
}

/*
 * Function: isOdd
 * Usage: if (isOdd(n)) . . .
 * --------------------------
 * Returns true if the unsigned number n is odd.  A number is odd
 * if it is not even.
 */

bool isOdd(unsigned int n) {
   return !isEven(n);
}

//bool isOdd(unsigned int n) {
//   if (n == 0) return false;
////   if (n == 1) return true;
//   return isEven(n-1);
//}

/*
 * Function: isEven
 * Usage: if (isEven(n)) . . .
 * ---------------------------
 * Returns true if the unsigned number n is even.  A number is even
 * either (1) if it is zero or (2) if its predecessor is odd.
 */

bool isEven(unsigned int n) {
   if (n == 0) return true;
//   if (n == 1) return false;
   return isOdd(n-1);
//   return !isEven(n-1);
}

//bool isEven(unsigned int n) {
//   if (n == 0) return true;
////   if (n == 1) return false;
//   return isEven(n-2);
//}

//bool isEven(unsigned int n) {
//   return !isOdd(n);
//}

void isOddEven(unsigned int n) {
   cout << "isOdd(" << n << ") -> " << (isOdd(n) ? "true" : "false") << endl;
   cout << "isEven(" << n << ") -> " << (isEven(n) ? "true" : "false") << endl;
}
