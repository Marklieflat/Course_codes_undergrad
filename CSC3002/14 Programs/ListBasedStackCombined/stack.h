/*
 * File: stack.h
 * -------------
 * This interface exports the Stack class, which implements a collection
 * that processes values in a last-in/first-out (LIFO) order.  This version
 * of the interface uses a linked list as the underlying representation and
 * combines the prototypes and implementation in the body of the class.
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

   Stack() {
      list = NULL;                      /* Start with an empty list      */
      count = 0;                        /* Maintain count for efficiency */
   }

/*
 * Destructor: ~Stack
 * Usage: (usually implicit)
 * -------------------------
 * Frees any heap storage associated with this stack.
 */

   ~Stack() {
      clear();                          /* Clear frees all the cells     */
   }

/*
 * Method: size
 * Usage: int n = stack.size();
 * ----------------------------
 * Returns the number of values in this stack.
 */

   int size() const {
      return count;                     /* Keeping count makes this O(1) */
   }

/*
 * Method: isEmpty
 * Usage: if (stack.isEmpty()) . . .
 * ---------------------------------
 * Returns true if this stack contains no elements.
 */

   bool isEmpty() const {
      return count == 0;                /* Stack is empty if count = 0   */
   }

/*
 * Method: clear
 * Usage: stack.clear();
 * ---------------------
 * Removes all elements from this stack.
 */

   void clear() {
      while (count > 0) {               /* For each element in the stack */
         pop();                         /* Call pop to free the cell     */
      }
   }

/*
 * Method: push
 * Usage: stack.push(value);
 * -------------------------
 * Pushes the specified value onto this stack.
 */

   void push(ValueType value) {
      Cell *cp = new Cell;              /* Create a new cell             */
      cp->data = value;                 /* Store value in the data field */
      cp->link = list;                  /* Link this cell into the list  */
      list = cp;                        /*   at the start of the chain   */
      count++;                          /* Update the count field        */
   }

/*
 * Method: pop
 * Usage: ValueType top = stack.pop();
 * -----------------------------------
 * Removes the top element from this stack and returns it.  This
 * method signals an error if called on an empty stack.
 */

   ValueType pop() {
      if (isEmpty()) {
         error("pop: Attempting to pop an empty stack");
      }
      Cell *cp = list;                  /* Keep pointer to initial cell  */
      ValueType top = cp->data;         /* Keep a copy of the data value */
      list = list->link;                /* Remove cell from the chain    */
      delete cp;                        /* Free the memory for the cell  */
      count--;                          /* Update the count field        */
      return top;                       /* And return the saved value    */
   }

/*
 * Method: peek
 * Usage: ValueType top = stack.peek();
 * ------------------------------------
 * Returns the value of top element from this stack, without removing
 * it.  This method signals an error if called on an empty stack.
 */

   ValueType peek() const {
      if (isEmpty()) {
         error("peek: Attempting to peek at an empty stack");
      }
      return list->data;
   }

/*
 * Copy constructor and assignment operator
 * ----------------------------------------
 * These methods implement deep copying for stacks.
 */

   Stack(const Stack<ValueType> & src) {
      deepCopy(src);
   }

   Stack<ValueType> & operator=(const Stack<ValueType> & src) {
      if (this != &src) {
         clear();
         deepCopy(src);
      }
      return *this;
   }

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
   int count;                           /* Number of elements in the stack */

/*
 * Implementation notes: deepCopy
 * ------------------------------
 * The deepCopy method uses the copyList method to copy the list from src.
 */

   void deepCopy(const Stack<ValueType> & src) {
      count = src.count;
      list = copyList(src.list);
   }

/*
 * Implementation notes: copyList
 * ------------------------------
 * This method generates a recursively constructed copy of the argument.
 */

   Cell *copyList(Cell *list) {
      if (list == NULL) {
         return NULL;
      } else {
         Cell *cp = new Cell;
         cp->data = list->data;
         cp->link = copyList(list->link);
         return cp;
      }
   }

};

#endif
