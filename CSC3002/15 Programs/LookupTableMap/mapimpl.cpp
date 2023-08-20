/*
 * File: mapimpl.cpp
 * -----------------
 * This file contains the implementation of the map.h interface.  This
 * implementation is specific to keys that are composed of two uppercase
 * letters.  Any other key generates an error.
 */

#ifdef _map_h

#include <string>
#include <cctype>
#include "error.h"
using namespace std;

static void checkKey(string key) {
   if (key.length() != 2 || !isupper(key[0]) || !isupper(key[0])) {
      error("Invalid key");
   }
}

template <typename KeyType,typename ValueType>
Map<KeyType,ValueType>::Map() {
   clear();
}

template <typename KeyType,typename ValueType>
Map<KeyType,ValueType>::~Map() {
   /* Empty */
}

template <typename KeyType,typename ValueType>
int Map<KeyType,ValueType>::size() {
   return count;
}

template <typename KeyType,typename ValueType>
bool Map<KeyType,ValueType>::isEmpty() {
   return count == 0;
}

template <typename KeyType,typename ValueType>
void Map<KeyType,ValueType>::clear() {
   count = 0;
}

template <typename KeyType,typename ValueType>
ValueType Map<KeyType,ValueType>::get(KeyType key) {
   checkKey(key);
   return table[key[0] -'A'][key[1] -'A'];
}

template <typename KeyType,typename ValueType>
void Map<KeyType,ValueType>::put(KeyType key, ValueType value) {
   checkKey(key);
   table[key[0] -'A'][key[1] -'A'] = value;
}

template <typename KeyType,typename ValueType>
bool Map<KeyType,ValueType>::containsKey(KeyType key) {
   checkKey(key);
   return table[key[0] -'A'][key[1] -'A'] != "";
}

#endif
