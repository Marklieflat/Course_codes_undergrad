/*
 * File: MergeSort.cpp
 * -------------------
 * This file implements the merge sort algorithm using arrays rather
 * than vectors.
 */

#include "MergeSort.h"

/*
 * Function: printArray
 * Usage: printArray(array, n);
 * ----------------------------
 * Prints the elements of the array on a single line with the elements
 * enclosed in braces and separated by commas.
 */

void printArray(int array[], int n) {
   cout << "{ ";
   for (int i = 0; i < n; i++) {
      if (i > 0) cout << ", ";
      cout << array[i];
   }
   cout << " }" << endl;
}


void sort(int array[], int n){
    if (n <= 1) return; // The situation that no need to sort
    int array1[n/2]; // Split the whole array into two subarrays
    int array2[n - n/2];
    for (int i = 0; i < n; i++){
        if (i < n/2){
            array1[i] = array[i];
        }
        else{
            array2[i - n/2] = array[i];
        }
    }
    sort(array1, n/2); // Recursively sort the two subarrays
    sort(array2, n - n/2);
    for (int i = 0; i < n; i++){
        array[i] = 0;
    }
    int n1 = n/2; // The capacity of the first subarray
    int n2 = n - n/2;  // The capacity of the second subarray
    int p1 = 0; // Indexes of the two subarrays
    int p2 = 0;
    int check = 0; // Index of the whole merged array
    while (p1 < n1 && p2 < n2){ // when the two subarrays are not merged completely
        if (array1[p1] < array2[p2]){
            array[check++] = array1[p1++];
        }
        else{
            array[check++] = array2[p2++];
        }
    }
    while (p1 < n1){ // When array2 has already been merged
        array[check++] = array1[p1++];
    }
    while (p2 < n2){ // When array1 has already been merged
        array[check++] = array2[p2++];
    }
}
