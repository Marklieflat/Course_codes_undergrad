/*
 * File: Combinatorics.cpp
 * -----------------------
 * This file implements the combinatorics.h interface.
 */

#include "Combinatorics.h"
#include <iostream>

int permutations(int n, int k){
    int result = 1;
    for (int i = n - k + 1; i <= n; i++){
        result *= i;
    }
    return result;
}

int combinations(int n, int k){
    int result = permutations(n, k);
    for (int i = 1; i <= k; i++){
        result /= i;
    }
    return result;
}

