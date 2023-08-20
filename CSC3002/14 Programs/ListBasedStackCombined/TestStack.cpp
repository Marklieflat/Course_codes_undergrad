/*
 * File: TestStack.cpp
 * -------------------
 * This program tests the Stack package by creating a test
 * program that implements the following commands:
 *
 *     push str  -- Pushes the string onto the stack
 *     pop       -- Pops the stack and displays the value
 *     peek      -- Peeks at the top element
 *     size      -- Prints the size of the stack
 *     isEmpty   -- Prints whether the stack is empty
 *     clear     -- Clears the stack
 *     list      -- List the elements of the stack
 *     help      -- List these commands
 *     quit      -- Quits the program
 */

#include <iostream>
#include <string>
#include "stack.h"
#include "simpio.h"
#include "strlib.h"
#include "tokenscanner.h"
using namespace std;

/* Function prototypes */

void executeCommand(TokenScanner & scanner, Stack<string> & stack);
void helpCommand();
void listStack(const Stack<string> & stack);

/* Main program */

int main() {
   Stack<string> stack;
   TokenScanner scanner;
   scanner.ignoreWhitespace();
   scanner.scanNumbers();
   scanner.scanStrings();
   while (true) {
      scanner.setInput(getLine("> "));
      executeCommand(scanner, stack);
   }
   return 0;
}

void executeCommand(TokenScanner & scanner, Stack<string> & stack) {
   string cmd = scanner.nextToken();
   if (cmd == "push") {
      stack.push(scanner.getStringValue(scanner.nextToken()));
   } else if (cmd == "pop") {
      if (stack.isEmpty()) {
         cout << "Stack is empty" << endl;
      } else {
         cout << stack.pop() << endl;
      }
   } else if (cmd == "peek") {
      if (stack.isEmpty()) {
         cout << "Stack is empty" << endl;
      } else {
         cout << stack.peek() << endl;
      }
   } else if (cmd == "size") {
      cout << stack.size() << endl;
   } else if (cmd == "isEmpty") {
      cout << ((stack.isEmpty()) ? "true" : "false") << endl;
   } else if (cmd == "clear") {
      stack.clear();
   } else if (cmd == "list") {
      listStack(stack);
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
   cout << "  push str  -- Pushes the string onto the stack" << endl;
   cout << "  pop       -- Pops the stack and displays the value" << endl;
   cout << "  peek      -- Peeks at the top element" << endl;
   cout << "  size      -- Prints the size of the stack" << endl;
   cout << "  isEmpty   -- Prints whether the stack is empty" << endl;
   cout << "  clear     -- Clears the stack" << endl;
   cout << "  list      -- List the elements of the stack" << endl;
   cout << "  help      -- List these commands" << endl;
   cout << "  quit      -- Quits the program" << endl;
}

/*
 * Function: listStack
 * Usage: listStack(stack);
 * ------------------------
 * Lists the contents of the stack.  This implementation makes an
 * explicit copy to avoid making changes to the argument stack.
 */

void listStack(const Stack<string> & stack) {
   if (stack.isEmpty()) {
      cout << "Stack is empty" << endl;
   } else {
      Stack<string> stk = stack;
      string contents = stk.pop();
      while (!stk.isEmpty()) {
         contents = stk.pop() + " " + contents;
      }
      cout << contents << endl;
   }
}
