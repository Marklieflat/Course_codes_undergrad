/*
 * File: bst.h
 * -----------
 * This file provides an interface for a simplified binary search
 * tree class.  In this version of the interface, the keys are
 * always strings.
 */

#ifndef _bst_h
#define _bst_h

#include <string>

/*
 * Type: Node
 * -----------
 * The Node structure represents a node in the binary search tree.
 */

struct Node {
   std::string key;
   Node *left, *right;
};

/*
 * Class: BST
 * ----------
 * This class represents a simplified binary search tree in which the
 * keys are always strings.
 */

class BST {
   
public:
   
/*
 * Constructor: BST
 * Usage: BST bst;
 * ---------------
 * Initializes an empty binary search tree.
 */
   
   BST();
   
/*
 * Destructor: ~BST
 * Usage: (usually implicit)
 * -------------------------
 * Deallocates the storage for a tree.
 */
   
   ~BST();

/*
 * Method: add
 * Usage: bst.add(key);
 * --------------------
 * This method adds a new key to this tree.
 */
   
   void add(std::string key);
   
/*
 * Method: containsKey
 * Usage:  if (bst.containsKey(key)) . . .
 * ---------------------------------------
 * Checks to see whether the key is in the BST.
 */
   
   bool containsKey(std::string key);

/*
 * Method: clear
 * Usage: bst.clear();
 * -------------------
 * Removes all elements from this tree.
 */

   void clear();

/*
 * Method: list
 * Usage: bst.list();
 * ------------------
 * Lists the contents of the BST on the cout stream in lexicographic
 * order.
 */
   
   void list();

private:

/* Instance variables */

   Node *root;

};

#endif
