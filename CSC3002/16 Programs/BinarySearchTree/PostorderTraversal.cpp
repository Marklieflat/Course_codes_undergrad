/*
 * File: PostorderTraversal.cpp
 * ----------------------------
 * This file contains the code for producing a postorder traversal
 * of the binary search tree containing Disney's seven dwarves.
 */

#include <iostream>
#include <string>
#include "bst.h"
using namespace std;

/* Function prototypes */

void postorderTraversal(BSTNode *t);

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
   postorderTraversal(dwarfTree);
   return 0;
}

/*
 * Function: postorderTraversal
 * Usage: postorderTraversal(t);
 * -----------------------------
 * Prints the keys in the binary search tree t using a postorder traversal
 * in which the current node is printed after its children.
 */

void postorderTraversal(BSTNode *t) {
   if (t != NULL) {
      postorderTraversal(t->left);
      postorderTraversal(t->right);
      cout << t->key << endl;
   }
}
