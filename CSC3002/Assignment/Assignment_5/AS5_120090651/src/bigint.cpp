/*
 * File: bigint.cpp
 * ----------------
 * This file implements the bigint.h interface.
 */

#include <cctype>
#include <string>
#include "bigint.h"
#include "error.h"
using namespace std;

/*
 * Implementation notes: BigInt constructor
 * ----------------------------------------
 * The code for this constructor offers a minimal implementation
 * that matches what we would expect on an exam.  In a more
 * sophisticated implementation, it would make sense to include
 * a test to avoid storing leading zeros in the linked list.  In
 * this implementation, calling BigInt("00042") creates a
 * BigInt with a different internal representation than
 * BigInt("42"), which is probably a bad idea.
 */

BigInt::BigInt(string str) {
    //TODO
    Cell *lastpt = NULL;
    int size = str.length();
    for (int i = 0; i < size; i++){
        Cell *cp = new Cell;
        cp->leadingDigits = lastpt;
        cp->finalDigit = str[i] - 48;
        lastpt = cp;
    }
    start = new Cell;
    start = lastpt;
}

/*
 * Implementation notes: BigInt destructor
 * ---------------------------------------
 * The code for the destructor is similar to that of the other
 * classes that contain a linked list.  You need to store the
 * pointer to the next cell temporarily so that you still have
 * it after you delete the current cell.
 */

BigInt::~BigInt() {
    //TODO
    Cell *iterator = start;
    while (iterator->leadingDigits != NULL){
        Cell *cp = iterator->leadingDigits;
        delete iterator;
        iterator = cp;
    }
    delete start;
    start = NULL;
}



/*
 * Implementation notes: toString
 * ------------------------------
 * This method could also be written as a wrapper method that
 * calls a recursive function that creates the reversed string
 * one character at a time.
 */

string BigInt::toString() const {
    //TODO
    Cell *iterator = start;
    string result = "";
    while (iterator != NULL){
        result = to_string(iterator->finalDigit) + result;
        iterator = iterator->leadingDigits;
    }
    return result;
}

/*
 * Implementation notes: operator+ and operator*
 * ------------------------------
 * Implement operator+ and operator*, make BigInt surpport addition and
 * multiplication.
 */

BigInt BigInt::operator+(const BigInt & b2) const {
    //TODO
    int flag = 0; // carry of the addition
    int digit = 0; // digit at the certain place
    Cell *p1 = this->start;
    Cell *p2 = b2.start;
    Cell *p3 = new Cell;
    digit = (p1->finalDigit) + (p2->finalDigit) + flag;
    flag = digit / 10;
    digit = digit % 10;
    p3->finalDigit = digit;
    p3->leadingDigits = NULL;
    p1 = p1->leadingDigits;
    p2 = p2->leadingDigits;
    Cell *result = p3;
    while (p1 != NULL || p2 != NULL){
        int x = (p1 != NULL) ? p1->finalDigit : 0;
        int y = (p2 != NULL) ? p2->finalDigit : 0;
        digit = flag + x + y;
        flag = digit / 10;
        Cell *bit = new Cell;
        bit->finalDigit = digit % 10;
        bit->leadingDigits = NULL;
        p3->leadingDigits = bit;
        p3 = bit;
        bit = NULL;
        if (p1 != NULL){
            p1 = p1->leadingDigits;
        }
        if (p2 != NULL){
            p2 = p2->leadingDigits;
        }
    }
    if (flag > 0){
        Cell *bit = new Cell;
        bit->finalDigit = flag;
        bit->leadingDigits = NULL;
        p3->leadingDigits = bit;
        p3 = bit;
        bit = NULL;
    }
    p3->leadingDigits = NULL;
    return BigInt(result);
}

BigInt BigInt::operator*(const BigInt & b2) const {
    //TODO
    Cell *p1 = this->start;
    Cell *p2 = b2.start;
    int n1 = 0;
    int n2 = 0;
    int temp;
    BigInt result = BigInt("0");
    while (p1 != NULL){
        p2 = b2.start;
        n2 = 0;
        while (p2 != NULL){
            temp = (p1->finalDigit) * (p2->finalDigit);
            BigInt tempres = BigInt(to_string(temp));
            if (n1 + n2 > 0){ // The situation that needs to carry the digit
                for (int i = 0; i < n1 + n2; i++){
                    Cell *last = new Cell;
                    last->finalDigit = 0;
                    last->leadingDigits = tempres.start;
                    tempres.start = last;
                }
            }
            result = result + tempres;
            p2 = p2->leadingDigits;
            n2++;
        }
        p1 = p1->leadingDigits;
        n1++;
    }
    return result;
}

BigInt::BigInt(const BigInt & src){
    deepcopy(src);
}

BigInt BigInt::operator=(const BigInt & src){
    if (this != & src){
        this -> ~BigInt();
        deepcopy(src);
    }
    return *this;
}

void BigInt::deepcopy(const BigInt & src){
    start = NULL;
    Cell *p1 = new Cell;
    Cell *p2 = src.start;
    start = new Cell;
    p1->finalDigit = p2->finalDigit;
    p1->leadingDigits = NULL;
    start = p1;
    while (p2->leadingDigits != NULL){
        p2 = p2->leadingDigits;
        Cell *cp = new Cell;
        cp->leadingDigits = NULL;
        cp->finalDigit = p2->finalDigit;
        p1->leadingDigits = cp;
        p1 = cp;
    }
}
