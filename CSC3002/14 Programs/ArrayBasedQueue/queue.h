/*
 * File: queue.h
 * -------------
 * This interface exports a template version of the Queue class.
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
 * Implementation notes
 * --------------------
 * The array-based queue stores the elements in successive index
 * positions in an array, just as a stack does.  What makes the
 * queue structure more complex is the need to avoid shifting
 * elements as the queue expands and contracts.  In the array
 * model, this goal is achieved by keeping track of both the
 * head and tail indices.  The tail index increases by one each
 * time an element is enqueued, and the head index increases by
 * one each time an element is dequeued.  Each index therefore
 * marches toward the end of the allocated array and will
 * eventually reach the end.  Rather than allocate new memory,
 * this implementation lets each index wrap around back to the
 * beginning as if the ends of the array of elements were joined
 * to form a circle.  This representation is called a ring buffer.
 *
 * The elements of the queue are stored in a dynamic array of
 * the specified element type.  If the space in the array is ever
 * exhausted, the implementation doubles the array capacity.
 * Note that the queue capacity is reached when there is still
 * one unused element in the array.  If the queue is allowed to
 * fill completely, the head and tail indices have the same
 * value, and the queue appears empty.
 */

private:

   static const int INITIAL_CAPACITY = 10;

/* Instance variables */

   ValueType *array;                    /* A dynamic array of the elements */
   int capacity;                        /* The allocated size of the array */
   int head;                            /* The index of the head element   */
   int tail;                            /* The index of the tail element   */

/* Private method prototypes */

   void deepCopy(const Queue<ValueType> & src);
   void expandCapacity();

};

/*
 * Implementation section
 * ----------------------
 * Clients should not need to look at any of the code beyond this point.
 */

/*
 * Implementation notes: Queue constructor
 * ---------------------------------------
 * The constructor allocates the array storage and initializes the fields.
 */

template <typename ValueType>
Queue<ValueType>::Queue() {
   capacity = INITIAL_CAPACITY;
   array = new ValueType[capacity];
   head = 0;
   tail = 0;
}

/*
 * Implementation notes: ~Queue
 * ----------------------------
 * The destructor frees any memory that is allocated by the implementation.
 */

template <typename ValueType>
Queue<ValueType>::~Queue() {
   delete[] array;
}

/*
 * Implementation notes: size
 * --------------------------
 * The size is calculated from head and tail using modular arithmetic.
 */

template <typename ValueType>
int Queue<ValueType>::size() const {
   return (tail + capacity - head) % capacity;
}

/*
 * Implementation notes: isEmpty
 * -----------------------------
 * The queue is empty whenever the head and tail pointers are equal.  This
 * interpretation means that the queue must always leave one unused space.
 */

template <typename ValueType>
bool Queue<ValueType>::isEmpty() const {
   return head == tail;
}

/*
 * Implementation notes: clear
 * ---------------------------
 * The clear method need not take account of where in the ring buffer the
 * existing values are stored and can simply reset the head and tail indices.
 */

template <typename ValueType>
void Queue<ValueType>::clear() {
   head = tail = 0;
}

/*
 * Implementation notes: enqueue
 * -----------------------------
 * This method first checks to see whether there is enough room for the
 * element and then expands the array storage if necessary.  Because it
 * is otherwise impossible to differentiate the case when a queue is
 * empty from when it is completely full, this implementation expands
 * the queue when the size is one less than the capacity.
 */

template <typename ValueType>
void Queue<ValueType>::enqueue(ValueType value) {
   if (size() == capacity - 1) expandCapacity();
   array[tail] = value;
   tail = (tail + 1) % capacity;
}

/*
 * Implementation notes: dequeue, peek
 * -----------------------------------
 * These methods check for an empty queue and report an error if
 * there is no first element.
 */

template <typename ValueType>
ValueType Queue<ValueType>::dequeue() {
   if (isEmpty()) error("dequeue: Attempting to dequeue an empty queue");
   ValueType result = array[head];
   head = (head + 1) % capacity;
   return result;
}

template <typename ValueType>
ValueType Queue<ValueType>::peek() const {
   if (isEmpty()) error("peek: Attempting to peek at an empty queue");
   return array[head];
}

/*
 * Implementation notes: Deep copying support
 * ------------------------------------------
 * These methods implement deep copying for queues.
 */

template <typename ValueType>
Queue<ValueType>::Queue(const Queue<ValueType> & src) {
   deepCopy(src);
}

template <typename ValueType>
Queue<ValueType> & Queue<ValueType>::operator=(const Queue<ValueType> & src) {
   if (this != &src) {
      delete[] array;
      deepCopy(src);
   }
   return *this;
}

template <typename ValueType>
void Queue<ValueType>::deepCopy(const Queue<ValueType> & src) {
   int count = src.size();
   capacity = count + INITIAL_CAPACITY;
   array = new ValueType[capacity];
   for (int i = 0; i < count; i++) {
      array[i] = src.array[(src.head + i) % src.capacity];
   }
   head = 0;
   tail = count;
}

/*
 * Implementation notes: expandCapacity
 * ------------------------------------
 * This private method doubles the capacity of the dynamic array whenever
 * it runs out of space.  For simplicity, this implementation also shifts
 * all the elements back to the beginning of the array.
 */

template <typename ValueType>
void Queue<ValueType>::expandCapacity() {
   int count = size();
   ValueType *oldArray = array;
   array = new ValueType[2 * capacity];
   for (int i = 0; i < count; i++) {
      array[i] = oldArray[(head + i) % capacity];
   }
   capacity *= 2;
   head = 0;
   tail = count;
   delete[] oldArray;
}

#endif
