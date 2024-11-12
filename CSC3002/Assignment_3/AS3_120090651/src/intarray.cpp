/*
 * File: intarray.cpp
 * ------------------
 * This file inplements the intarray.h interface.
 */

#include "intarray.h"
#include "error.h"
#include "strlib.h"
using namespace std;

IntArray::IntArray(int n){
    nElements = n;
    array = new int[nElements];
    for (int i = 0; i < n; i++){
        array[i] = 0;
    }
}

IntArray::~IntArray(){
    delete[] array;
}

int IntArray::size(){
    return nElements;
}

int IntArray::get(int index){
    if (index < 0 || index >= nElements){
        error("This index is outside of the array bounds.");
    }
    else{
        return array[index];
    }
}

void IntArray::put(int index, int value){
    if (index < 0 || index >= nElements){
        error("This index is outside of the array bounds.");
    }
    else{
        array[index] = value;
    }
}

int & IntArray::operator[](int index){
    if (index < 0 || index >= nElements){
        error("This index is outside of the array bounds.");
    }
    else{
        return array[index];
    }
}

IntArray::IntArray(const IntArray & src){
    deepCopy(src);
}

IntArray & IntArray::operator=(const IntArray & src){
    if (this != & src){ // Test whether src is the same as the lvalue
        delete[] array;
        deepCopy(src);
    }
    return *this;  // return the instance pointed by the pointer 'this'
}

void IntArray::deepCopy(const IntArray & src){
    array = new int[src.nElements];
    for (int i = 0; i < src.nElements; i++){
        array[i] = src.array[i]; // Assign the value of each element to the new IntArray
    }
    nElements = src.nElements; // Assign the number of elements to the new IntArray
}






