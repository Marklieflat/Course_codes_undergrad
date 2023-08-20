/*
 * File: buffer.cpp (stack version)
 * --------------------------------
 * This file implements the EditorBuffer class using a pair of character
 * stacks to represent the buffer.
 */

#include <iostream>
#include "buffer.h"
#include "charstack.h"
#include "console.h"
using namespace std;

/*
 * Implementation notes: Constructor and destructor
 * ------------------------------------------------
 * In this implementation, all dynamic allocation is managed by the
 * CharStack class, which means there is no work for EditorBuffer to do.
 */

EditorBuffer::EditorBuffer() { }
EditorBuffer::~EditorBuffer() { }

/*
 * Implementation notes: moveCursor methods
 * ----------------------------------------
 * The four moveCursor methods use push and pop to transfer values
 * between the two stacks.
 */

void EditorBuffer::moveCursorForward() {
   if (!after.isEmpty()) {
      before.push(after.pop());
   }
}

void EditorBuffer::moveCursorBackward() {
   if (!before.isEmpty()) {
      after.push(before.pop());
   }
}

void EditorBuffer::moveCursorToStart() {
   while (!before.isEmpty()) {
      after.push(before.pop());
   }
}

void EditorBuffer::moveCursorToEnd() {
   while (!after.isEmpty()) {
      before.push(after.pop());
   }
}

/*
 * Implementation notes: character insertion and deletion
 * ------------------------------------------------------
 * Each of the functions that inserts or deletes characters can do so
 * with a single push or pop operation.
 */

void EditorBuffer::insertCharacter(char ch) {
   before.push(ch);
}

void EditorBuffer::deleteCharacter() {
   if (!after.isEmpty()) {
      after.pop();
   }
}

/*
 * Implementation notes: getText and getCursor
 * -------------------------------------------
 * The only difficult part of implementing these operators is making
 * sure that the state of the buffer is restored after copying the
 * characters from the two stacks.
 */

string EditorBuffer::getText() const {
   CharStack beforeCopy = before;
   CharStack afterCopy = after;
   string str = "";
   while (!beforeCopy.isEmpty()) {
      str = beforeCopy.pop() + str;
   }
   while (!afterCopy.isEmpty()) {
      str += afterCopy.pop();
   }
   return str;
}

int EditorBuffer::getCursor() const {
   return before.size();
}
