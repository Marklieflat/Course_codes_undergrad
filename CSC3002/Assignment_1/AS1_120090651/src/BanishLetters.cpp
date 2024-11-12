/*
 * File: BanishLetters.cpp
 * -----------------------
 * This program removes all instances of a set of letters from
 * an input file.
 */

#include "BanishLetters.h"
#include "filelib.h"
#include "simpio.h"
#include "strlib.h"
using namespace std;

void banishLetters(){
    ifstream infile;
    ofstream outfile;
    string ban;
    string ban_lower;
    string ban_upper;
    char ch;
    promptUserForFile(infile, "Input file: ");
    promptUserForFile(outfile, "Output file: ");
    cout << "Letters to banish: " ;
    cin >> ban;
    ban_lower = toLowerCase(ban);
    ban_upper = toUpperCase(ban);
    ban = ban_lower + ban_upper; // To recognize the upper case and lower case letter as the same character
    while (infile.get(ch)){
        if (int(ban.find(ch)) == -1){   // if we this letter is not going to be banished, we just output it
            outfile.put(ch);
        }
    }
    infile.close();
    outfile.close();
}
