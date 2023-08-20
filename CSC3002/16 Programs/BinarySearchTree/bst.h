/*
 * File: bst.h
 * -----------
 * This file exports the simple BST structure and methods used in the chapter.
 */

#ifndef _bst_h
#define _bst_h

#include <string>

/*
 * Type: BSTNode
 * -------------
 * This type represents a node in the binary search tree.
 */

struct BSTNode {
   std::string key;
   BSTNode *left, *right;
};

/*
 * Function: findNode
 * Usage: BSTNode *np = findNode(t, key);
 * --------------------------------------
 * Finds the node with the specified key in the binary search tree t.
 * If the search is successful, findNode returns a pointer to that
 * node.  If the key does not exist in the tree, findNode returns NULL.
 */

BSTNode *findNode(BSTNode *t, const std::string & key);

/*
 * Function: insertNode
 * Usage: insertNode(t, key);
 * --------------------------
 * Inserts the specified key at the appropriate location in the
 * binary search tree rooted at t.  Note that t must be passed
 * by reference, since it is possible to change the root.
 */

void insertNode(BSTNode * & t, const std::string & key);

/*
 * Function: displayTree
 * Usage: displayTree(t);
 * ----------------------
 * Prints the keys in the binary search tree t in lexicographic order.
 */

void displayTree(BSTNode *t);

#endif
