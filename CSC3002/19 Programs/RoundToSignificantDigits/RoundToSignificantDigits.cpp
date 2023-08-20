/*
 * File: RoundToSignificantDigits.cpp
 * ----------------------------------
 * This program tests the RoundToSignificantDigits function,
 * which operates by writing and reading a single stringstream,
 * thereby serving as a demonstration of multiple inheritance.
 */

#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

/* Constants */

const double SPEED_OF_LIGHT = 2.99792458E+08 /* m/sec */;
const double PLANCKS_CONSTANT = 6.626068E-34 /* m2 kg / sec */;

/* Function prototypes */

void testRounding(double value, int nDigits);
double roundToSignificantDigits(double x, int nDigits);

/* Main program */

int main() {
   testRounding(3.141592, 3);
   testRounding(3.141592, 5);
   testRounding(SPEED_OF_LIGHT, 3);
   testRounding(SPEED_OF_LIGHT, 5);
   testRounding(PLANCKS_CONSTANT, 3);
   testRounding(PLANCKS_CONSTANT, 5);
   return 0;
}

/*
 * Function: testRounding
 * Usage: testRounding(value, nDigits);
 * ------------------------------------
 * Generates a single test of the roundToSignificantDigits function.
 */

void testRounding(double value, int nDigits) {
   cout << uppercase << "roundToSignificantDigits("
        << setprecision(8) << value << ", " << nDigits << ") = "
        << roundToSignificantDigits(value, nDigits) << endl;
}

/*
 * Function: roundToSignificantDigits
 * Usage: double rounded = roundToSignificantDigits(x, nDigits);
 * -------------------------------------------------------------
 * Rounds the value x so that it contains only nDigits of
 * significance.
 */

double roundToSignificantDigits(double x, int nDigits) {
   stringstream ss;
   ss << setprecision(nDigits) << x;
   ss >> x;
   return x;
}
