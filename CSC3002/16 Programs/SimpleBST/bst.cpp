/*
 * File: bst.cpp
 * -------------
 * This file implements the bst.h interface, which provides a
 * simplified implementation of binary search trees in which all
 * keys are strings.
 */

#include <iostream>
#include <string>
#include "bst.h"
#include "console.h"
using namespace std;

/* Function prototypes */

Node *findNode(Node *t, string key);
void insertNode(Node * & t, string key);
void listTree(Node *t);
void freeTree(Node *t);

/*
 * Implementation notes: constructor and destructor
 * ------------------------------------------------
 * The constructor simply sets the root of the tree to NULL.  The
 * destructor frees all the nodes in the tree by calling clear.
 */

BST::BST() {
   root = NULL;
}

BST::~BST() {
    clear();
}

/*
 * Implementation notes: add, containsKey, list, clear
 * ---------------------------------------------------
 * The methods in this version of the BST class are all wrappers
 * that call recursive functions on the root of the tree.
 */

void BST::add(string key) {
   insertNode(root, key);
}

bool BST::containsKey(string key) {
   return findNode(root, key) != NULL;
}

void BST::list() {
   listTree(root);
}

void BST::clear() {
   freeTree(root);
   root = NULL;
}

/* Free functions */

/*
 * Function: findNode
 * Usage: Node *node = findNode(t, key);
 * --------------------------------------
 * Finds a node with the specified key in the binary search tree rooted
 * at t.  If a node matching key appears in the tree, findNode returns
 * a pointer to that node.  If the key does not appear, findNode
 * returns NULL.
 */

Node *findNode(Node *t, string key) {
   if (t == NULL) return NULL;
   if (key == t->key) return t;
   if (key < t->key) {
      return findNode(t->left, key);
   } else {
      return findNode(t->right, key);
   }
}

/*
 * Function: insertNode
 * Usage: insertNode(t, key);
 * --------------------------
 * Inserts the specified key at the appropriate location in the
 * binary search tree rooted at t.  Note that t must be passed
 * by reference, since it is possible to change the root.
 */

void insertNode(Node * & t, string key) {
   if (t == NULL) {
      t = new Node;
      t->key = key;
      t->left = t->right = NULL;
      return;
   }
   if (key == t->key) return;
   if (key < t->key) {
      insertNode(t->left, key);
   } else {
      insertNode(t->right, key);
   }
}

/*
 * Function: listTree
 * Usage: listTree(t);
 * -------------------
 * Lists the keys in the binary search tree rooted at t.  By processing
 * the keys recursively using an inorder walk, listTree always produces
 * the keys in lexicographic order.
 */

void listTree(Node *t) {
   if (t != NULL) {
      listTree(t->left);
      cout << t->key << endl;
      listTree(t->right);
     }   
}

/*
 * Function: freeTree
 * Usage: freeTree(t);
 * -------------------
 * Frees all of the nodes in the specified tree.  This function ensures
 * that the current node is not deleted until all its children are.
 */

void freeTree(Node *t) {
   if (t != NULL) {
      freeTree(t->left);
      freeTree(t->right);
      delete t;
   }   
}
