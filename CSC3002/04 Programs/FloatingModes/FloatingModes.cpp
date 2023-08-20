/*
 * File: FloatingModes.cpp
 * -----------------------
 * This program demonstrates various options for floating-point
 * output by displaying exp(n) for a range of values.
 */

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
   cout << uppercase << right << showpoint << setprecision(6);
   cout << boolalpha << endl;
   for (int i = -5; i <= +5; i++) {
      double ep = exp(i);
      cout << setw(3) << i;
      cout.setf((_Ios_Fmtflags) 0, ios::floatfield);
      cout << setw(11) << ep;
      cout << setw(13) << fixed << ep;
      cout << setw(15) << scientific << ep << endl;
   }
   return 0;
}
