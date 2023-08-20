/*
 * File: sort.h
 * ------------
 * This interface exports a function that sorts an array of ints.
 */

#ifndef _sort_h
#define _sort_h

/* Prototypes */
template <typename ValueType>
void sort(ValueType array[], int n);

template <typename ValueType>
void swap(ValueType & x, ValueType & y);

/*
 * Function: sort
 * Usage: sort(array);
 * -------------------
 * This function sorts the elements of the array into increasing order.
 */

template <typename ValueType>
void sort(ValueType array[], int n) {
    for (int i = 0; i < n; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (array[j] < array[minIndex]) minIndex = j;
        }
        swap(array[i], array[minIndex]);
    }
}

template <typename ValueType>
void swap(ValueType & x, ValueType & y) {
   ValueType tmp = x;
   x = y;
   y = tmp;
}

#endif
