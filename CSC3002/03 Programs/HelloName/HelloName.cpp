/*
 * File: HelloName.cpp
 * -------------------
 * This program extends the classic "Hello world" program by asking
 * the user for a name, which is then used as part of the greeting.
 */

#include <iostream>
#include <string>
//#include "console.h"
using namespace std;

int main() {
   string name;
   char cname[10];
   cout << "Enter your name: ";
   cin >> name;
   cout << "Enter your name again: ";
   cin >> cname;
   cout << "Hello, " << name << "!" << endl;
   cout << "Hello, " << cname << "!" << endl;
   cout << "Hello, " + name + "!" << endl;
   cout << string("Hello, ") + cname + "!" << endl;
   return 0;
}
