/*
 * File: hashmap.cpp
 * -----------------
 * This file contains the hash functions that are used in conjunction
 * with the HashMap class.
 */

#include <iostream>
#include <string>
using namespace std;

/* Constant definitions */

/* Constants */

const int HASH_SEED = 5381;               /* Starting point for first cycle */
const int HASH_MULTIPLIER = 33;           /* Multiplier for each cycle      */
const int HASH_MASK = unsigned(-1) >> 1;  /* The largest positive integer   */

/*
 * Function: hashCode [for strings]
 * Usage: int code = hashCode(key);
 * --------------------------------
 * This function takes a string key and uses it to derive a hash code,
 * which is nonnegative integer related to the key by a deterministic
 * function that distributes keys well across the space of integers.
 * The specific algorithm used here is called djb2 after the initials
 * of its inventor, Daniel J. Bernstein, Professor of Mathematics at
 * the University of Illinois at Chicago.
 */

int hashCode(string str) {
   unsigned hash = HASH_SEED;
   int n = str.length();
   for (int i = 0; i < n; i++) {
      hash = HASH_MULTIPLIER * hash + str[i];
   }
   return int(hash & HASH_MASK);
}

/*
 * Function: hashCode [numeric]
 * Usage: int code = hashCode(key);
 * --------------------------------
 * These versions of the function simply return an integer in the
 * appropriate range.
 */

int hashCode(int key) {
   return key & HASH_MASK;
}

int hashCode(long key) {
   if (sizeof(long) > sizeof(int)) {
      int *ip = (int *) & key;
      key = ip[0] ^ ip[1];
   }
   return int(key) & HASH_MASK;
}

int hashCode(char key) {
   return key & HASH_MASK;
}
