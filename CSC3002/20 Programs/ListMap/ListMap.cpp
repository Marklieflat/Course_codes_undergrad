/*
 * File: ListMap.cpp
 * -----------------
 * This program lists the key-value pairs in a Map<string,int>.
 */

#include <iostream>
#include <string>
#include "map.h"
using namespace std;

/* Function prototypes */

void listMap(const Map<string,int> & map);
void listMapEntry(string key, int value);
void listMap2(const Map<string,int> & map);
void listMapEntry2(const string & key, const int & value);

/* Main program */

int main() {
   Map<string,int> map;
   map["one"] = 1;
   map["two"] = 2;
   map["three"] = 3;
   map["four"] = 4;
   map["five"] = 5;
   map["six"] = 6;
   map["seven"] = 7;
   map["eight"] = 8;
   map["nine"] = 9;
   map["ten"] = 10;
   listMap(map);
   cout << endl;
   cout << "Using constant reference parameters:" << endl;
   listMap2(map);
   return 0;
}

/*
 * Function: listMap
 * Usage: listMap(map);
 * --------------------
 * Displays the key-value pairs in the map.  The output appears in
 * lexicographic order because the Map class uses the ordering of
 * the key type.
 */

void listMap(const Map<string,int> & map) {
   map.mapAll(listMapEntry);
}

/*
 * Function: listMapEntry
 * Usage: listMap(key, value);
 * ---------------------------
 * Prints a single key-value pair.  This function is designed to be
 * used as a callback function for the mapAll method in the Map class.
 */

void listMapEntry(string key, int value) {
   cout << key << " = " << value << endl;
}

/*
 * Implementation notes
 * --------------------
 * The remainder of this file tests the same code with a callback
 * function that takes the key and value arguments using constant
 * call by reference.
 */

#define listMap listMap2
#define listMapEntry listMapEntry2

/*
 * Function: listMap
 * Usage: listMap(map);
 * --------------------
 * Displays the key-value pairs in the map.  The output will appear
 * in lexicographic order because the Map class uses the ordering of
 * the key type.
 */

void listMap(const Map<string,int> & map) {
   map.mapAll(listMapEntry);
}

/*
 * Function: listMapEntry
 * Usage: listMap(key, value);
 * ---------------------------
 * Prints out a single key-value pair.  This function is designed to
 * be used in conjunction with the mapAll method in the Map class.
 */

void listMapEntry2(const string & key, const int & value) {
   cout << key << " = " << value << endl;
}
