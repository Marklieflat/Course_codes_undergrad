/*
 * File: DwarfTree.cpp
 * -------------------
 * This file contains the code for producing the binary search tree
 * containing Disney's seven dwarves.
 */

#include <iostream>
#include <string>
#include "bst.h"
using namespace std;

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
   displayTree(dwarfTree);
   return 0;
}
