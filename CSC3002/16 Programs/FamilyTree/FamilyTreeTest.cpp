/*
 * File: FamilyTreeTest.cpp
 * ------------------------
 * Simple but inadequate test program for the familytree.h interface.
 */

#include <fstream>
#include <iomanip>
#include <iostream>
#include "familytree.h"
#include "filelib.h"
#include "map.h"
#include "simpio.h"
#include "vector.h"
using namespace std;

/* Function prototypes */

FamilyTreeNode *readGenealogyFile(ifstream & infile);
void displayFamilyTree(FamilyTreeNode *person, int indentation = 0);

/* Main program */

int main() {
   ifstream infile;
   promptUserForFile(infile, "Genealogy file: ");
   FamilyTreeNode *root = readGenealogyFile(infile);
   infile.close();
   displayFamilyTree(root);
   return 0;
}

FamilyTreeNode *readGenealogyFile(ifstream & infile) {
   Map<string,FamilyTreeNode *> map;
   FamilyTreeNode *result = NULL;
   while (true) {
      string line;
      getline(infile, line);
      if (infile.fail()) break;
      int colon = line.find(':');
      if (colon == string::npos) {
         result = new FamilyTreeNode(line);
         map[line] = result;
      } else {
         string childName = line.substr(0, colon);
         string parentName = line.substr(colon + 1);
         FamilyTreeNode *child = new FamilyTreeNode(childName);
         FamilyTreeNode *parent = map[parentName];
         map[childName] = child;
         parent->addChild(child);
      }
   }
   return result;
}

void displayFamilyTree(FamilyTreeNode *person, int indentation) {
   cout << setw(indentation) << "" << person->getName() << endl;
   Vector<FamilyTreeNode *> children = person->getChildren();
   for (int i = 0; i < children.size(); i++) {
      displayFamilyTree(children[i], indentation + 2);
   }
}
