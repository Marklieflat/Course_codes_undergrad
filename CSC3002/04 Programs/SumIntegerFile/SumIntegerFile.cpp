/*
 * File: SumIntegerFile.cpp
 * ------------------------
 * This program calculates and prints the sum of the integers in
 * a data file chosen by the user.  This program makes no attempt
 * to check that the file is formatted correctly and is therefore
 * not appropriate for use in practice.  It does, however, illustrate
 * the use of the extraction operator with files.
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
using namespace std;

/* Function prototypes */

/*
 * Function: promptUserForFile
 * Usage: string filename = promptUserForFile(stream, prompt);
 * -----------------------------------------------------------
 * Asks the user for the name of a file.  The file is opened using
 * the reference parameter <code>stream</code>, and the function
 * returns the name of the file.  If the requested file cannot be
 * opened, the user is given additional chances to enter a valid file.
 *
 * The optional <code>prompt</code> argument provides an input prompt
 * for the user.
 */

string promptUserForFile(ifstream & stream, string prompt = "");
string promptUserForFile(ofstream & stream, string prompt = "");

int stringToInteger(string str);
string integerToString(int n);
void error(string msg);

/* Main program */

int main() {
   ifstream infile;
   promptUserForFile(infile, "Input file: ");
   int total = 0;
   string line;
   while (getline(infile, line)) {
      total += stringToInteger(line);
   }
   infile.close();
   cout << "The sum is " << integerToString(total) << endl;
   return 0;
}

/*
 * Function: stringToInteger
 * Usage: int n = stringToInteger(str);
 * ------------------------------------
 * Converts a string of digits (possibly preceded or followed by whitespace)
 * into the corresponding integer.  If the conversion fails, the function
 * displays an error message and exits with a nonzero status.
 */

int stringToInteger(string str) {
   istringstream stream(str);
   int value;
   stream >> value >> ws;
   if (stream.fail() || !stream.eof()) {
      error("Illegal integer format: " + str);
   }
   return value;
}

/*
 * Function: integerToString
 * Usage: string str = integerToString(n);
 * ---------------------------------------
 * Converts an integer into the corresponding string of digits.
 */

string integerToString(int n) {
   ostringstream stream;
   stream << n;
   return stream.str();
}

void error(string msg) {
   cerr << msg << endl;
   exit(EXIT_FAILURE);
}

string promptUserForFile(ifstream & stream, string prompt) {
    while (true) {
        cout << prompt;
        string filename;
        getline(cin, filename);
        stream.open(filename.c_str());
        if (!stream.fail()) return filename;
        stream.clear();
        cout << "Unable to open that file.  Try again." << endl;
        if (prompt == "") prompt = "Input file: ";
    }
}

string promptUserForFile(ofstream & stream, string prompt) {
    while (true) {
        cout << prompt;
        string filename;
        getline(cin, filename);
        stream.open(filename.c_str());
        if (!stream.fail()) return filename;
        stream.clear();
        cout << "Unable to open that file.  Try again." << endl;
        if (prompt == "") prompt = "Output file: ";
    }
}

