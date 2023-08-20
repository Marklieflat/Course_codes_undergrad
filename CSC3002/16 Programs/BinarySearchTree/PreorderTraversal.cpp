/*
 * File: PreorderTraversal.cpp
 * ---------------------------
 * This file contains the code for producing a preorder traversal
 * of the binary search tree containing Disney's seven dwarves.
 */

#include <iostream>
#include <string>
#include "bst.h"
using namespace std;

/* Function prototypes */

void preorderTraversal(BSTNode *t);

/* Main program */

int main() {
   BSTNode *dwarfTree = NULL;
   insertNode(dwarfTree, "Grumpy");
   insertNode(dwarfTree, "Sleepy");
   insertNode(dwarfTree, "Doc");
   insertNode(dwarfTree, "Bashful");
   insertNode(dwarfTree, "Dopey");
   insertNode(dwarfTree, "Happy");
   insertNode(dwarfTree, "Sneezy");
   preorderTraversal(dwarfTree);
   return 0;
}

/*
 * Function: preorderTraversal
 * Usage: preorderTraversal(t);
 * ----------------------------
 * Prints the keys in the binary search tree t using a preorder traversal
 * in which the current node is printed before its children.
 */

void preorderTraversal(BSTNode *t) {
   if (t != NULL) {
      cout << t->key << endl;
      preorderTraversal(t->left);
      preorderTraversal(t->right);
   }
}
