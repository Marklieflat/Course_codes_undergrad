/*
 * File: queue.h
 * -------------
 * This interface exports a template version of the Queue class.
 * This version of the interface uses a linked list to implement
 * the queue.
 */

#ifndef _queue_h
#define _queue_h

#include "error.h"

/*
 * Class: Queue<ValueType>
 * -----------------------
 * This class implements a queue of the specified value type.
 */

template <typename ValueType>
class Queue {

public:

/*
 * Constructor: Queue
 * Usage: Queue<ValueType> queue;
 * ------------------------------
 * Initializes a new empty queue.
 */

   Queue();

/*
 * Destructor: ~Queue
 * Usage: (usually implicit)
 * -------------------------
 * Frees any heap storage associated with this queue.
 */

   ~Queue();

/*
 * Method: size
 * Usage: int n = queue.size();
 * ----------------------------
 * Returns the number of values in the queue.
 */

   int size() const;

/*
 * Method: isEmpty
 * Usage: if (queue.isEmpty()) . . .
 * ---------------------------------
 * Returns true if the queue contains no elements.
 */

   bool isEmpty() const;

/*
 * Method: clear
 * Usage: queue.clear();
 * ---------------------
 * Removes all elements from this queue.
 */

   void clear();

/*
 * Method: enqueue
 * Usage: queue.enqueue(value);
 * ----------------------------
 * Adds value to the end of the queue.
 */

   void enqueue(ValueType value);

/*
 * Method: dequeue
 * Usage: ValueType first = queue.dequeue();
 * -----------------------------------------
 * Removes and returns the first item in the queue.  This method
 * signals an error if called on an empty queue.
 */

   ValueType dequeue();

/*
 * Method: peek
 * Usage: ValueType first = queue.peek();
 * --------------------------------------
 * Returns the first value in the queue without removing it.  This
 * method signals an error if called on an empty queue.
 */

   ValueType peek() const;

/*
 * Copy constructor and assignment operator
 * ----------------------------------------
 * These methods implement deep copying for queues.
 */

   Queue(const Queue<ValueType> & src);
   Queue<ValueType> & operator=(const Queue<ValueType> & src);

/* Private section */

/*
 * Implementation notes: Queue data structure
 * ------------------------------------------
 * The list-based queue uses a linked list to store the elements
 * of the queue.  To ensure that adding a new element to the tail
 * of the queue is fast, the data structure maintains a pointer to
 * the last cell in the queue as well as the first.  If the queue is
 * empty, both the head pointer and the tail pointer are set to NULL.
 *
 * The following diagram illustrates the structure of a queue
 * containing two elements, A and B.
 *
 *       +-------+        +-------+        +-------+
 *  head |   o---+------->|   A   |  +--==>|   B   |
 *       +-------+        +-------+  |  |  +-------+
 *  tail |   o---+---+    |   o---+--+  |  |  NULL |
 *       +-------+   |    +-------+     |  +-------+
 *                   |                  |
 *                   +------------------+
 */

private:

/* Type for linked list cell */

   struct Cell {
      ValueType data;                   /* The data value                  */
      Cell *link;                       /* Link to the next cell           */
   };

/* Instance variables */

   Cell *head;                          /* Pointer to the cell at the head */
   Cell *tail;                          /* Pointer to the cell at the tail */
   int count;                           /* Number of elements in the queue */

/* Private method prototypes */

   void deepCopy(const Queue<ValueType> & src);

};

/*
 * Implementation section
 * ----------------------
 * C++ requires that the implementation for a template class be available
 * to the compiler whenever that type is used.  The effect of this
 * restriction is that header files must include the implementation.
 * Clients should not need to look at any of the code beyond this point.
 */

/*
 * Implementation notes: Queue constructor
 * ---------------------------------------
 * The constructor creates an empty linked list and sets the count to 0.
 */

template <typename ValueType>
Queue<ValueType>::Queue() {
   head = tail = NULL;
   count = 0;
}

/*
 * Implementation notes: ~Queue destructor
 * ---------------------------------------
 * The destructor frees any heap memory allocated by the queue.
 */

template <typename ValueType>
Queue<ValueType>::~Queue() {
   clear();
}

/*
 * Implementation notes: size, isEmpty, clear
 * ------------------------------------------
 * These methods use the count variable and therefore run in constant time.
 */

template <typename ValueType>
int Queue<ValueType>::size() const {
   return count;
}

template <typename ValueType>
bool Queue<ValueType>::isEmpty() const {
   return count == 0;
}

template <typename ValueType>
void Queue<ValueType>::clear() {
   while (count > 0) {
      dequeue();
   }
}

/*
 * Implementation notes: enqueue
 * -----------------------------
 * This method allocates a new list cell and chains it in at the tail of
 * the queue.  If the queue is currently empty, the new cell also becomes
 * the head pointer in the queue.
 */

template <typename ValueType>
void Queue<ValueType>::enqueue(ValueType value) {
   Cell *cp = new Cell;
   cp->data = value;
   cp->link = NULL;
   if (head == NULL) {
      head = cp;
   } else {
      tail->link = cp;
   }
   tail = cp;
   count++;
}

/*
 * Implementation notes: dequeue, peek
 * -----------------------------------
 * These methods check for an empty queue and report an error if
 * there is no first element.  The dequeue method also checks for
 * the case in which the queue becomes empty and sets both the head
 * and tail pointers to NULL.
 */

template <typename ValueType>
ValueType Queue<ValueType>::dequeue() {
   if (isEmpty()) error("dequeue: Attempting to dequeue an empty queue");
   Cell *cp = head;
   ValueType result = cp->data;
   head = cp->link;
   if (head == NULL) tail = NULL;
   delete cp;
   count--;
   return result;
}

template <typename ValueType>
ValueType Queue<ValueType>::peek() const {
   if (isEmpty()) error("peek: Attempting to peek at an empty queue");
   return head->data;
}

/*
 * Implementation notes: copy constructor and assignment operator
 * --------------------------------------------------------------
 * These methods follow the standard template, leaving the work to deepCopy.
 */

template <typename ValueType>
Queue<ValueType>::Queue(const Queue<ValueType> & src) {
   deepCopy(src);
}

template <typename ValueType>
Queue<ValueType> & Queue<ValueType>::operator=(const Queue<ValueType> & src) {
   if (this != &src) {
      clear();
      deepCopy(src);
   }
   return *this;
}

/*
 * Implementation notes: deepCopy
 * ------------------------------
 * This function copies the data from the src parameter into the current
 * object.  This implementation simply walks down the linked list in the
 * source object and enqueues each value in the destination.
 */

template <typename ValueType>
void Queue<ValueType>::deepCopy(const Queue<ValueType> & src) {
   head = NULL;
   tail = NULL;
   count = 0;
   for (Cell *cp = src.head; cp != NULL; cp = cp->link) {
      enqueue(cp->data);
   }
}

#endif
