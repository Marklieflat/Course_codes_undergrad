/*
 * File: map.h
 * -----------
 * This interface exports a simplified version of the Map class.
 */

#ifndef _map_h
#define _map_h

/*
 * Class: Map<KeyType,ValueType>
 * -----------------------------
 * The Map class maintains an association between keys and values of
 * the specified types.
 */

template <typename KeyType,typename ValueType>
class Map {

public:

/*
 * Constructor: Map
 * Usage: Map<KeyType,ValueType> map;
 * ----------------------------------
 * Initializes a new empty map that associates keys and values.
 */

   Map();

/*
 * Destructor: ~Map
 * Usage: (usually implicit)
 * -------------------------
 * Frees any heap storage associated with this map.
 */

   ~Map();

/*
 * Method: size
 * Usage: int nEntries = map.size();
 * ---------------------------------
 * Returns the number of entries in this map.
 */

   int size();

/*
 * Method: isEmpty
 * Usage: if (map.isEmpty()) . . .
 * -------------------------------
 * Returns true if this map contains no entries.
 */

   bool isEmpty();

/*
 * Method: clear
 * Usage: map.clear();
 * -------------------
 * Removes all entries from this map.
 */

   void clear();

/*
 * Method: containsKey
 * Usage: if (map.containsKey(key)) . . .
 * --------------------------------------
 * Returns true if there is an entry for key in this map.
 */

   bool containsKey(KeyType key);

/*
 * Method: get
 * Usage: ValueType value = map.get(key);
 * --------------------------------------
 * Returns the value associated with key in this map.  If key is not
 * found, get returns the default value for the value type.
 */

   ValueType get(KeyType key);

/*
 * Method: put
 * Usage: map.put(key, value);
 * ---------------------------
 * Associates key with value in this map.  Any previous value associated
 * with key is replaced by the new value.
 */

   void put(KeyType key, ValueType value);

#include "mappriv.h"
};

#include "mapimpl.cpp"
#endif
