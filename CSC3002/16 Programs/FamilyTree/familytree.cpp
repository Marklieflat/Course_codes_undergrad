/*
 * File: familytree.cpp
 * --------------------
 * This program implements the familytree.h interface.
 */

#include "familytree.h"
#include "vector.h"
using namespace std;

FamilyTreeNode::FamilyTreeNode(const string & name) {
   this->name = name;
   this->parent = NULL;
}

string FamilyTreeNode::getName() {
   return name;
}

void FamilyTreeNode::addChild(FamilyTreeNode *child) {
   children.add(child);
   child->parent = this;
}

FamilyTreeNode *FamilyTreeNode::getParent() {
   return parent;
}

Vector<FamilyTreeNode *> FamilyTreeNode::getChildren() {
   return children;
}
