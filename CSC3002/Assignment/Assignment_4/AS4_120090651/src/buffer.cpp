/*
 * File: buffer.cpp (list version without dummy cell)
 * --------------------------------------------------
 * This file implements the EditorBuffer class using a linked
 * list to represent the buffer.
 */

#include <iostream>
#include "buffer.h"
using namespace std;

/*
 * Implementation notes: EditorBuffer constructor
 * ----------------------------------------------
 * This function initializes an empty editor buffer, represented
 * as a doubly linked list.  In this implementation, the ends of
 * the linked list are joined to form a ring, with the dummy cell
 * at both the beginning and the end.  This representation makes
 * it possible to implement the moveCursorToEnd method in constant
 * time, and reduces the number of special cases in the code.
 */

EditorBuffer::EditorBuffer() {
   start = cursor = new Cell;
   start->next = start;
   start->prev = start;
}

EditorBuffer::~EditorBuffer(){
    Cell *cp = start->next;
    while (cp->next != start){ // Start from the dummy cell to iterate
        Cell *follow = cp->next;
        delete cp;
        cp = NULL;
        cp = follow;
    }
    delete start;
    start = NULL;
}

/*
 * Implementation notes: cursor movement
 * -------------------------------------
 * In a doubly linked list, each of these operations runs in
 * constant time.
 */

void EditorBuffer::moveCursorForward() {
    if (cursor->next != start) {
      cursor = cursor->next;
   }
}

void EditorBuffer::moveCursorBackward(){
    if (cursor != start){
        cursor = cursor->prev;
    }
}

void EditorBuffer::moveCursorToStart(){
    cursor = start;
}

void EditorBuffer::moveCursorToEnd(){
    cursor = start->prev;
}

void EditorBuffer::insertCharacter(char ch){
    Cell *cp = new Cell;
    cp->ch = ch;
    cp->next = cursor->next;
    cp->prev = cursor;
    cursor->next = cp;  // Link the previous cell with the new cell
    cp->next->prev = cp; // Back link the next cell with the newly inserted one
    cursor = cp; // Move the cursor to the newly inserted one
}

void EditorBuffer::deleteCharacter(){
    if (cursor->next != start){
        Cell *oldcell = cursor->next;
        cursor->next = oldcell->next; // Move the pointer skip the deleted cell
        oldcell->next->prev = cursor; // Let the cell which is after the deleted cell to back link the cell before the deleted cell
        delete oldcell;
        oldcell = NULL;
    }
}

string EditorBuffer::getText() const {
    Cell *get = start->next;
    string text = "";
    while (get != start){
        text += get->ch;
        get = get->next;
    }
    get = NULL;
    return text;
}

int EditorBuffer::getCursor() const {
    Cell *indexcell = start;
    int index = 0;
    while (indexcell != cursor){
        indexcell = indexcell->next;
        index++;
    }
    indexcell = NULL;
    return index;
}








