/*
 * File: PowersOfTwo.cpp
 * ---------------------
 * This program generates a list of the powers of
 * two up to an exponent limit entered by the user.
 */

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
using namespace std;

/* Function prototypes */

int getInteger(string prompt);
int raiseToPower(int n, int k);

/* Main program */

int main() {
   cout << "This program lists powers of two." << endl;
   int limit = getInteger("Enter exponent limit: ");
   for (int i = 0; i <= limit; i++) {
      cout << setw(2) << i
           << setw(8) << raiseToPower(2, i) << endl;
   }
   return 0;
}

/*
 * Function: getInteger
 * Usage: int n = getInteger(prompt);
 * ----------------------------------
 * Requests an integer value from the user.  The function begins by
 * printing the prompt string on the console and then waits for the
 * user to enter a line of input data.  If that line contains a
 * single integer, the function returns the corresponding integer
 * value.  If the input is not a legal integer or if extraneous
 * characters (other than whitespace) appear on the input line,
 * the implementation gives the user a chance to reenter the value.
 */

int getInteger(string prompt) {
   int value;
   string line;
   while (true) {
      cout << prompt;
      getline(cin, line);
      istringstream stream(line);
      stream >> value >> ws;
      if (!stream.fail() && stream.eof()) break;
      cout << "Illegal integer format. Try again." << endl;
   }
   return value;
}

/*
 * Function: raiseToPower
 * Usage: p = raiseToPower(n, k);
 * ------------------------------
 * Returns the integer n raised to the kth power.
 */

int raiseToPower(int n, int k) {
   int result = 1;
   for (int i = 0; i < k; i++) {
      result *= n;
   }
   return result;
}
