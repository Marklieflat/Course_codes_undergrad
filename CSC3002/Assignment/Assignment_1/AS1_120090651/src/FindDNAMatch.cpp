/*
 * File: FindDNAMatch.cpp
 * ----------------------
 * This file solves the DNA matching exercise from the text.
 */

#include "FindDNAMatch.h"
#include <iostream>
#include <string>
using namespace std;

string matchingStrand(string strand){ // To match the base
    int strandlen = strand.length();
    string result;
    for (int i = 0; i < strandlen; i++){
        char output = strand[i];
        switch (output){
            case 'A':
                result += 'T';
                break;
            case 'T':
                result += 'A';
                break;
            case 'C':
                result += 'G';
                break;
            case 'G':
                result += 'C';
                break;
            default:
                result += 'X';
                break;
        }
    }
    return result;
}

int findDNAMatch(string s1, string s2, int start){
    int pos = s2.find(s1,start);
    return pos;
}

void findAllMatches(string s1, string s2){
    string s1trans = matchingStrand(s1);
    int start = 0;
    if (findDNAMatch(s1trans, s2, start) == -1){ // From the starting point we cannot find the matching base sequence
        cout << "These two DNA " << s1 << " and " << s2 << " cannot match" << endl;
    }
    while (findDNAMatch(s1trans, s2, start) != -1){
        int i = findDNAMatch(s1trans, s2, start);
        cout << "These two DNA " << s1 << " and " << s2 << " match at position " << i+1 << endl;
        start = i + 1; // We start from the next character of the already matched point to find the other matches
    }

}
