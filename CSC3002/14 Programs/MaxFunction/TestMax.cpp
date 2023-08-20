/*
 * File: TestMax.cpp
 * -----------------
 * This program tests the template version of the max function.
 */

#include <iostream>
#include <string>
#include "rational.h"
using namespace std;

/* Rename max internally to avoid conflict with the algorithms library */

#define max maximum

/* Function prototypes */

template <typename ValueType>
ValueType max(ValueType x, ValueType y);

//string max(const char *x, const char *y);

/* Main program */

int main() {
   cout << "max(17, 42) -> " << max(17, 42) << endl;
   cout << "max(3.14159, 2.71828) -> " << max(3.14159, 2.71828) << endl;
   cout << "max('Z', 'A') -> " << "'" << max('Z', 'A') << "'" << endl;
   cout << "max(\"cat\", \"dog\") -> \"" << max("cat", "dog")
        << "\"" << endl;
//   cout << "max(\"dog\", \"cat\") -> \"" << max("dog", "cat")
//        << "\"" << endl;
   cout << "max(Rational(5,6), Rational(1,2)) -> "
        << max(Rational(5,6), Rational(1,2)) << endl;
   return 0;
}

/*
 * Template function: max
 * Usage: type var = max(v1, v2);
 * ------------------------------
 * Returns the maximum of v1 and v2, which can be of any type that
 * implements the > comparison operator.
 */

template <typename ValueType>
ValueType max(ValueType x, ValueType y) {
   return (x > y) ? x : y;
}

//string max(const char *x, const char *y) {
//   return max(string(x), string(y));
//}
