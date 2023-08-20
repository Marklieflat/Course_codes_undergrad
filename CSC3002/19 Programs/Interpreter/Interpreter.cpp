/*
 * File: Interpreter.cpp
 * ---------------------
 * This program simulates the top level of an expression interpreter.  The
 * program reads an expression, evaluates it, and then displays the result.
 */

#include <iostream>
#include <string>
#include "error.h"
#include "exp.h"
#include "parser.h"
#include "tokenscanner.h"
using namespace std;

int main() {
   EvaluationContext context;
   TokenScanner scanner;
   Expression *exp;
   scanner.ignoreWhitespace();
   scanner.scanNumbers();
   while (true) {
      exp = NULL;
      try {
         string line;
         cout << "=> ";
         getline(cin, line);
         if (line == "quit") break;
         scanner.setInput(line);
         Expression *exp = parseExp(scanner);
         int value = exp->eval(context);
         cout << value << endl;
      } catch (ErrorException ex) {
         cerr << "Error: " << ex.getMessage() << endl;
      }
      if (exp != NULL) delete exp;
   }
   return 0;
}
