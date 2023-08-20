/*
 * File: ShowFileContents.cpp
 * --------------------------
 * This program displays the contents of a file chosen by the user.
 */

#include <iostream>
#include <fstream>
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

//void copyStream(ifstream & infile, ofstream & outfile)
void copyStream(istream & is, ostream & os);

/* Main program */

int main() {
   ifstream infile;
   promptUserForFile(infile, "Input file: ");
   copyStream(infile, cout);
   infile.close();
   return 0;
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

//void copyStream(ifstream & infile, ofstream & outfile) {
//   while (true) {
//      int ch = infile.get();
//      if (ch == EOF) break;
//      outfile.put(ch);
//   }
//}

void copyStream(istream & is, ostream & os) {
   char ch;
   while (is.get(ch)) {
      os.put(ch);
   }
}
