/*
 * File: stack.h
 * -------------
 * This interface exports the Stack class, which implements a collection
 * that processes values in a last-in/first-out (LIFO) order.  This version
 * of the interface uses a linked list as the underlying representation.
 */

#ifndef _stack_h
#define _stack_h

#include "error.h"

/*
 * Class: Stack<ValueType>
 * -----------------------
 * This class implements a stack of the specified value type.
 */

template <typename ValueType>
class Stack {

public:

/*
 * Constructor: Stack
 * Usage: Stack<ValueType> stack;
 * ------------------------------
 * Initializes a new empty stack.
 */

   Stack();

/*
 * Destructor: ~Stack
 * Usage: (usually implicit)
 * -------------------------
 * Frees any heap storage associated with this stack.
 */

   ~Stack();

/*
 * Method: size
 * Usage: int n = stack.size();
 * ----------------------------
 * Returns the number of values in this stack.
 */

   int size() const;

/*
 * Method: isEmpty
 * Usage: if (stack.isEmpty()) . . .
 * ---------------------------------
 * Returns true if this stack contains no elements.
 */

   bool isEmpty() const;

/*
 * Method: clear
 * Usage: stack.clear();
 * ---------------------
 * Removes all elements from this stack.
 */

   void clear();

/*
 * Method: push
 * Usage: stack.push(value);
 * -------------------------
 * Pushes the specified value onto this stack.
 */

   void push(ValueType value);

/*
 * Method: pop
 * Usage: ValueType top = stack.pop();
 * -----------------------------------
 * Removes the top element from this stack and returns it.  This
 * method signals an error if called on an empty stack.
 */

   ValueType pop();

/*
 * Method: peek
 * Usage: ValueType top = stack.peek();
 * ------------------------------------
 * Returns the value of top element from this stack without removing
 * it.  This method signals an error if called on an empty stack.
 */

   ValueType peek() const;

/*
 * Copy constructor and assignment operator
 * ----------------------------------------
 * These methods implement deep copying for stacks.
 */

   Stack(const Stack<ValueType> & src);
   Stack<ValueType> & operator=(const Stack<ValueType> & src);

/* Private section */

private:

/*
 * Implementation notes
 * --------------------
 * This version of the stack.h interface uses a linked list to store
 * the elements of the stack.  The top item is always at the front of
 * the linked list and is therefore always accessible without searching.
 * The instance variable count keeps track of the number of elements so
 * that the size method runs in constant time.
 */

/* Type for linked list cell */

   struct Cell {
      ValueType data;                   /* The data value                  */
      Cell *link;                       /* Link to the next cell           */
   };

/* Instance variables */

   Cell *list;                          /* Initial pointer in the list     */
   int count;                           /* Number of elements              */

/* Private method prototypes */

   void deepCopy(const Stack<ValueType> & src);
   Cell *copyList(Cell *list);

};

/*
 * Implementation section
 * ----------------------
 * C++ requires that the implementation for a template class be available
 * to the compiler whenever that type is used.  Clients should not need
 * to look at any of the code beyond this point.
 */

/*
 * Implementation notes: Stack constructor
 * ---------------------------------------
 * The constructor creates an empty linked list and initializes the count.
 */

template <typename ValueType>
Stack<ValueType>::Stack() {
   list = NULL;
   count = 0;
}

/*
 * Implementation notes: Stack destructor
 * --------------------------------------
 * The destructor frees any heap memory that is allocated by the
 * implementation.  Because clear frees each element it processes,
 * this implementation of the destructor simply calls that method.
 */

template <typename ValueType>
Stack<ValueType>::~Stack() {
   clear();
}

/*
 * Implementation notes: size, isEmpty
 * -----------------------------------
 * These methods use the count variable and therefore run in constant time.
 */

template <typename ValueType>
int Stack<ValueType>::size() const {
   return count;
}

template <typename ValueType>
bool Stack<ValueType>::isEmpty() const {
   return count == 0;
}

/*
 * Implementation notes: clear
 * ---------------------------
 * This method pops the stack until it is empty, thereby freeing each cell.
 */

template <typename ValueType>
void Stack<ValueType>::clear() {
   while (count > 0) {
      pop();
   }
}

/*
 * Implementation notes: push
 * --------------------------
 * This method chains a new element onto the front of the list where it
 * becomes the top of the stack.
 */

template <typename ValueType>
void Stack<ValueType>::push(ValueType value) {
   Cell *cp = new Cell;
   cp->data = value;
   cp->link = list;
   list = cp;
   count++;
}

/*
 * Implementation notes: pop, peek
 * -------------------------------
 * These methods check for an empty stack and report an error if
 * there is no top element.  The pop method frees the cell to ensure
 * that the implementation does not leak memory as it executes.
 */

template <typename ValueType>
ValueType Stack<ValueType>::pop() {
   if (isEmpty()) error("pop: Attempting to pop an empty stack");
   Cell *cp = list;
   ValueType result = cp->data;
   list = list->link;
   count--;
   delete cp;
   return result;
}

template <typename ValueType>
ValueType Stack<ValueType>::peek() const {
   if (isEmpty()) error("peek: Attempting to peek at an empty stack");
   return list->data;
}

/*
 * Implementation notes: copy constructor and assignment operator
 * --------------------------------------------------------------
 * These methods follow the standard template, leaving the work to deepCopy.
 */

template <typename ValueType>
Stack<ValueType>::Stack(const Stack<ValueType> & src) {
   deepCopy(src);
}

template <typename ValueType>
Stack<ValueType> & Stack<ValueType>::operator=(const Stack<ValueType> & src) {
   if (this != &src) {
      clear();
      deepCopy(src);
   }
   return *this;
}

/*
 * Implementation notes: deepCopy
 * ------------------------------
 * The deepCopy method uses the copyList method to copy the list from src.
 */

template <typename ValueType>
void Stack<ValueType>::deepCopy(const Stack<ValueType> & src) {
   count = src.count;
   list = copyList(src.list);
}

/*
 * Implementation notes: copyList
 * ------------------------------
 * This method generates a recursively constructed copy of the argument.
 * The typename keyword and the qualifier on the Cell type are required
 * because the return type is outside the scope of the method declaration.
 */

template <typename ValueType>
typename Stack<ValueType>::Cell *Stack<ValueType>::copyList(Cell *list) {
   if (list == NULL) {
      return NULL;
   } else {
      Cell *cp = new Cell;
      cp->data = list->data;
      cp->link = copyList(list->link);
      return cp;
   }
}

#endif
