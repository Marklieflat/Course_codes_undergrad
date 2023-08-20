/*
 * File: bst.cpp
 * -------------
 * This file implements the bst.h interface.
 */

#include <iostream>
#include <string>
#include "bst.h"
using namespace std;

BSTNode *findNode(BSTNode *t, const string & key) {
   if (t == NULL) return NULL;
   if (key == t->key) return t;
   if (key < t->key) {
      return findNode(t->left, key);
   } else {
      return findNode(t->right, key);
   }
}

void insertNode(BSTNode * & t, const string & key) {
   if (t == NULL) {
      t = new BSTNode;
      t->key = key;
      t->left = t->right = NULL;
   } else {
      if (key != t->key) {
         if (key < t->key) {
            insertNode(t->left, key);
         } else {
            insertNode(t->right, key);
         }
      }
   }
}

void displayTree(BSTNode *t) {
   if (t != NULL) {
      displayTree(t->left);
      cout << t->key << endl;
      displayTree(t->right);
   }
}
