/*
 * File: hashmapimpl.cpp
 * ---------------------
 * This file contains the private section of the hashmap.cpp interface.
 * Because of the way C++ compiles templates, this code must be
 * available to the compiler when it reads the header file.
 */

#ifdef _hashmap_h

//#include "error.h"

/* Constant definitions */

const int INITIAL_BUCKET_COUNT = 101;

/*
 * Implementation notes: HashMap constructor and destructor
 * --------------------------------------------------------
 * The constructor allocates the array of buckets and initializes
 * each bucket to the empty list.  The destructor must free the memory,
 * but can do so by calling clear.
 */

template <typename KeyType,typename ValueType>
HashMap<KeyType,ValueType>::HashMap() {
   nBuckets = INITIAL_BUCKET_COUNT;
   buckets = new Cell*[nBuckets];
   for (int i = 0; i < nBuckets; i++) {
      buckets[i] = NULL;
   }
   count = 0;
}

template <typename KeyType,typename ValueType>
HashMap<KeyType,ValueType>::~HashMap() {
   clear();
   delete [] buckets;
}

/*
 * Implementation notes: size, isEmpty
 * -----------------------------------
 * These methods are simple because the structure stores the entry count.
 */

template <typename KeyType,typename ValueType>
int HashMap<KeyType,ValueType>::size() {
   return count;
}

template <typename KeyType,typename ValueType>
bool HashMap<KeyType,ValueType>::isEmpty() {
   return count == 0;
}

/*
 * Implementation notes: clear
 * ---------------------------
 * This method frees all the cells to avoid a memory leak.
 */

template <typename KeyType,typename ValueType>
void HashMap<KeyType,ValueType>::clear() {
   for (int i = 0; i < nBuckets; i++) {
      Cell *cp = buckets[i];
      while (cp != NULL) {
         Cell *oldCell = cp;
         cp = cp->link;
         delete oldCell;
      }
   }
   count = 0;
}

/*
 * Implementation notes: get, put, containsKey
 * -------------------------------------------
 * These methods rely on the private findCell method.
 */

template <typename KeyType,typename ValueType>
ValueType HashMap<KeyType,ValueType>::get(KeyType key) {
   int bucket = hashCode(key) % nBuckets;
   Cell *cp = findCell(bucket, key);
   if (cp == NULL) return ValueType();
   return cp->value;
}

template <typename KeyType,typename ValueType>
void HashMap<KeyType,ValueType>::put(KeyType key, ValueType value) {
   int bucket = hashCode(key) % nBuckets;
   Cell *cp = findCell(bucket, key);
   if (cp == NULL) {
      cp = new Cell;
      cp->key = key;
      cp->link = buckets[bucket];
      buckets[bucket] = cp;
      count++;
   }
   cp->value = value;
}

template <typename KeyType,typename ValueType>
bool HashMap<KeyType,ValueType>::containsKey(KeyType key) {
   int bucket = hashCode(key) % nBuckets;
   return findCell(bucket, key) != NULL;
}

#endif
