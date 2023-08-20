/*
 * File: TestSimpleBST.cpp
 * -----------------------
 * This file implements a simple test of the simplified version
 * of the BST class that supports only strings as keys.  The
 * program reads command lines, which must be in one of the
 * following forms:
 *
 *   add <word>
 *   find <word>
 *   list
 *   clear
 *   quit
 */

#include <iostream>
#include <string>
#include "bst.h"
#include "console.h"
#include "simpio.h"
#include "strlib.h"
#include "tokenscanner.h"
using namespace std;

/* Main program */

int main() {
   BST bst;
   TokenScanner scanner;
   scanner.ignoreWhitespace();
   cout << "Simplified BST Test" << endl;
   while (true) {
      cout << "> ";
      scanner.setInput(getLine());
      string cmd = scanner.nextToken();
      if (cmd == "quit") {
         break;
      } else if (cmd == "list") {
         bst.list();
      } else if (cmd == "add") {
         string word = scanner.nextToken();
         bst.add(word);
      } else if (cmd == "find") {
         string word = scanner.nextToken();
         cout << (bst.containsKey(word) ? "Found" : "Not found") << endl;
      } else if (cmd == "clear") {
         bst.clear();
      } else {
         cout << "Unrecognized command " << cmd << endl;
      }
   }
   return 0;
}
