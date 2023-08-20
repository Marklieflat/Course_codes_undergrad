/*
 * File: VectorUnitTest.cpp
 * ------------------------
 * This file contains a unit test of the Vector class that uses the
 * C++ assert macro to test that each operation performs as it should.
 */

#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include "vector.h"
using namespace std;

/* Prototypes for the test methods */

void testCharVector();
void testIntVector();
void testCopyConstructorAndAssignment();

template <typename ValueType>
string toString(const Vector<ValueType> & vec);

/* Main test program */

int main() {
   testCharVector();
   testIntVector();
   testCopyConstructorAndAssignment();
   return 0;
}

void testCharVector() {
   Vector<char> v;
   assert(v.isEmpty());
   assert(v.size() == 0);
   v.add('A');
   assert(!v.isEmpty());
   assert(v.size() == 1);
   assert(v.get(0) == 'A');
   assert(v[0] == 'A');
   v.add('C');
   assert(toString(v) == "{A, C}");
   v.insert(1, 'B');
   assert(toString(v) == "{A, B, C}");
   v.remove(0);
   v.remove(v.size() - 1);
   assert(toString(v) == "{B}");
   v.clear();
   assert(v.size() == 0);
   for (char ch = 'A'; ch <= 'Z'; ch++) {
      v.add(ch);
   }
   assert(v.size() == 26);
   for (int i = 0; i < 26; i++) {
      assert(v[i] == char('A' + i));
   }
   v.clear();
   for (char ch = 'A'; ch <= 'Z'; ch++) {
      v.insert(0, ch);
   }
   for (int i = 0; i < 26; i++) {
      assert(v[i] == char('Z' - i));
   }
   Vector<char>::iterator it = v.begin();
   for (int i = 0; it != v.end(); i++) {
      assert(*it++ == char('Z' - i));
   }
   cout << "Vector<char> test succeeded" << endl;
}

void testIntVector() {
   Vector<int> v(25, 42);
   assert(v.size() == 25);
   assert(v[10] == 42);
   for (int i = 0; i < v.size(); i++) {
      v[i] = i;
   }
   for (int i = 0; i < v.size(); i++) {
      assert(v[i] == i);
   }
   v.add(25);
   assert(v.size() == 26);
   assert(v[25] == 25);
   Vector<int>::iterator it = v.begin();
   for (int i = 0; it != v.end(); i++) {
      assert(*it++ == i);
   }
   cout << "Vector<int> test succeeded" << endl;
}

void testCopyConstructorAndAssignment() {
   Vector<string> v1;
   v1.add("A");
   v1.add("B");
   v1.add("C");
   assert(v1.size() == 3);
   Vector<string> v2 = v1;
   assert(v2.size() == 3);
   assert(toString(v2) == "{A, B, C}");
   v2.clear();
   assert(v2.size() == 0);
   assert(v1.size() == 3);
   Vector<string> v3;
   v3 = v1;
   assert(v3.size() == 3);
   assert(toString(v3) == "{A, B, C}");
   v3.clear();
   assert(v3.size() == 0);
   assert(v1.size() == 3);
   cout << "Copy constructor and assignment test succeeded" << endl;
}

/*
 * Template function: toString
 * Usage: string str = toString(vec);
 * ----------------------------------
 * Converts the vector into a string by printing each of its elements.
 * The elements of the list are surrounded by curly braces and separated
 * by commas.
 */

template <typename ValueType>
string toString(const Vector<ValueType> & vec) {
   ostringstream os;
   int len = vec.size();
   os << "{";
   for (int i = 0; i < len; i++) {
      if (i > 0) os << ", ";
      os << vec.get(i);
   }
   os << "}";
   return os.str();
}
