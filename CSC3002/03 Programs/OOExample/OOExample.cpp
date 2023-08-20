/*
 * File: OOExample.cpp
 * -------------------
 * This program demonstrates the differences between the legacy C
 * language and the object-oriented C++ language in implementing
 * some simple string operations.
 */

#include <iostream>
#include <cstring>
#include <string>
//#include "console.h"
using namespace std;

int main() {

    /* strlen example */

   char cstr[] = "hello, world";
   cout << "The length of the C string \"" << cstr << "\" is: " << strlen(cstr) << "!" << endl;

   string str = "hello, world";
   cout << "The length of the C++ string \"" << str << "\" is: " << str.length() << "!" << endl;

    /* strcpy example */

   char cstr1[] = "Sample string";
   char cstr2[40];
   char cstr3[40];
   strcpy (cstr2, cstr1);
   strcpy (cstr3, "copy successful!");
   cout << "cstr1: " << cstr1 << "; cstr2: " << cstr2 << "; " << cstr3 << endl;

   string str1 = "Sample string";
   string str2;
   string str3;
   str2 = str1;
   str3 = "copy successful!";
   cout << "str1: " << str1 << "; str2: " << str2 << "; " << str3 << endl;

    /* strcat example */

   char cstr4[80];
   strcpy (cstr4, "These ");
   strcat (cstr4, "strings ");
   strcat (cstr4, "are ");
   strcat (cstr4, "concatenated.");
   cout << "cstr4: " << cstr4 << endl;

   string str4;
   str4 += "These ";
   str4 += "strings ";
   str4 += "are ";
   str4 += "concatenated.";
   cout << "str4: " << str4 << endl;


   return 0;
}
