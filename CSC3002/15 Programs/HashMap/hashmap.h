/*
 * File: hashmap.h
 * ---------------
 * This interface exports the HashMap class, which maintains a collection
 * of key-value pairs using a hashtable as the underlying data structure.
 */

#ifndef _hashmap_h
#define _hashmap_h

#include <cstdlib>
#include <string>

/*
 * Class: HashMap<KeyType,ValueType>
 * ---------------------------------
 * The HashMap class maintains an association between keys and values.
 * The types used for keys and values are specified as template parameters,
 * which makes it possible to use this structure with any data type.
 */

template <typename KeyType, typename ValueType>
class HashMap {

public:

/*
 * Constructor: HashMap
 * Usage: HashMap<KeyType,ValueType> map;
 * --------------------------------------
 * Initializes a new empty map that associates keys and values of the
 * specified types.  The type used for the key must define the == operator,
 * and there must be a free function with the following signature:
 *
 *     int hashCode(KeyType key);
 *
 * that returns a positive integer determined by the key.  This interface
 * exports hashCode functions for string and the C++ primitive types.
 */

   HashMap();

/*
 * Destructor: ~HashMap
 * Usage: (usually implicit)
 * -------------------------
 * Frees any heap storage associated with this map.
 */

   ~HashMap();

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
 * Method: get
 * Usage: ValueType value = map.get(key);
 * --------------------------------------
 * Returns the value associated with key in this map.  If key is not
 * found, the get method signals an error.
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

/*
 * Method: containsKey
 * Usage: if (map.containsKey(key)) . . .
 * --------------------------------------
 * Returns true if there is an entry for key in this map.
 */

   bool containsKey(KeyType key);

/*
 * Method: clear
 * Usage: map.clear();
 * -------------------
 * Removes all entries from this map.
 */

   void clear();

#include "hashmappriv.h"
};

/*
 * Function: hashCode
 * Usage: int hash = hashCode(key);
 * --------------------------------
 * Returns a hash code for the specified key, which is always a
 * nonnegative integer.  This function is overloaded to support
 * all of the primitive types and the C++ <code>string</code> type.
 */

int hashCode(std::string key);
int hashCode(int key);
int hashCode(char key);
int hashCode(long key);
//int hashCode(double key);

#include "hashmapimpl.cpp"

#endif
