/*
 * File: TestVector.cpp
 * --------------------
 * This program tests the Vector package by creating a test
 * program that implements the following commands:
 *
 *     size         -- Prints the size of the vector
 *     isEmpty      -- Prints whether the vector is empty
 *     clear        -- Clears the vector
 *     get k        -- Returns index k
 *     set k str    -- Sets index k to str
 *     add str      -- Adds str to the end of the vector
 *     insert k str -- Inserts str before index k
 *     remove k     -- Removes element k
 *     list         -- List the elements of the vector
 *     help         -- List these commands
 *     quit         -- Quits the program
 */

#include <iostream>
#include <string>
#include "vector.h"
#include "simpio.h"
#include "strlib.h"
#include "tokenscanner.h"
using namespace std;

/* Function prototypes */

void executeCommand(TokenScanner & scanner, Vector<string> & vec);
void helpCommand();
void listVector(Vector<string> & vec);
void printString(string str);

/* Main program */

int main() {
   Vector<string> vec;
   TokenScanner scanner;
   scanner.ignoreWhitespace();
   scanner.scanNumbers();
   scanner.scanStrings();
   while (true) {
      scanner.setInput(getLine("> "));
      executeCommand(scanner, vec);
   }
   return 0;
}

void executeCommand(TokenScanner & scanner, Vector<string> & vec) {
   string cmd = scanner.nextToken();
   if (cmd == "size") {
      cout << vec.size() << endl;
   } else if (cmd == "isEmpty") {
      cout << ((vec.isEmpty()) ? "true" : "false") << endl;
   } else if (cmd == "clear") {
      vec.clear();
   } else if (cmd == "get") {
      int k = stringToInteger(scanner.nextToken());
      cout << "vec[" << k << "] = " << vec[k] << endl;
   } else if (cmd == "set") {
      int k = stringToInteger(scanner.nextToken());
      vec[k] = scanner.getStringValue(scanner.nextToken());
   } else if (cmd == "add") {
      vec.add(scanner.getStringValue(scanner.nextToken()));
   } else if (cmd == "insert") {
      int k = stringToInteger(scanner.nextToken());
      vec.insert(k, scanner.getStringValue(scanner.nextToken()));
   } else if (cmd == "remove") {
      int k = stringToInteger(scanner.nextToken());
      vec.remove(k);
   } else if (cmd == "list") {
      listVector(vec);
   } else if (cmd == "help") {
      helpCommand();
   } else if (cmd == "quit") {
      exit(0);
   } else if (cmd != "") {
      cout << "Unrecognized command: " << cmd << endl;
   }
}

/*
 * Function: helpCommand
 * Usage: helpCommand();
 * ---------------------
 * Lists the available commands.
 */

void helpCommand() {
   cout << "Available commands:" << endl;
   cout << "  size         -- Prints the size of the vector" << endl;
   cout << "  isEmpty      -- Prints whether the vector is empty" << endl;
   cout << "  clear        -- Clears the vector" << endl;
   cout << "  get k        -- Returns index k" << endl;
   cout << "  set k str    -- Sets index k to str" << endl;
   cout << "  add str      -- Adds str to the end of the vector" << endl;
   cout << "  insert k str -- Inserts str before index k" << endl;
   cout << "  remove k     -- Removes element k" << endl;
   cout << "  list         -- List the elements of the vector" << endl;
   cout << "  help         -- List these commands" << endl;
   cout << "  quit         -- Quits the program" << endl;
}

/*
 * Function: listVector
 * Usage: listVector(vec);
 * -----------------------
 * Lists the elements of the vector one per line using a mapping function.
 */

void listVector(Vector<string> & vec) {
   vec.mapAll(printString);
}

/*
 * Function: printString
 * Usage: printString(str);
 * ------------------------
 * This function is the callback function used in listVector.
 */

void printString(string str) {
   cout << str << endl;
}
