/*
 * File: stringmap.cpp
 * -------------------
 * This file implements the stringmap.h interface.
 */

#include <string>
#include "stringmap.h"
using namespace std;

/*
 * Implementation notes: StringMap constructor and destructor
 * ----------------------------------------------------------
 * All dynamic allocation is handled by the Vector class.
 */

StringMap::StringMap() { }
StringMap::~StringMap() { }

/*
 * Implementation notes: put, get
 * ------------------------------
 * These methods use findKey to search for the specified key.
 */

string StringMap::get(const string & key) const {
   int index = findKey(key);
   return (index == -1) ? "" : bindings.get(index).value;
}

void StringMap::put(const string & key, const string & value) {
   int index = findKey(key);
   if (index == -1) {
      KeyValuePair entry;
      entry.key = key;
      index = bindings.size();
      bindings.add(entry);
   }
   bindings[index].value = value;
}

/*
 * Private method: findKey
 * -----------------------
 * Returns the index at which the key appears, or -1 if the key is not found.
 */

int StringMap::findKey(const string & key) const {
   for (int i = 0; i < bindings.size(); i++) {
      if (bindings.get(i).key == key) return i;
   }
   return -1;
}
