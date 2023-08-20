/*
 * File: RemoveComments.cpp
 * ------------------------
 * Prints out a file after removing comments.
 */

#include "RemoveComments.h"
#include <iostream>
#include <fstream>
using namespace std;

void removeComments(istream & is, ostream & os){
    char fstchar,sechar; // Get the first character and second character of the line
    while (is.get(fstchar)){
        if (fstchar == '/'){
            is.get(sechar);
            if (sechar == '*'){
                while (true){
                    if (fstchar == '*' && sechar == '/') break; // If the line is commented, then ignore the line
                    fstchar = sechar; // Iterate from the '/*' to the '*/' character by character
                    is.get(sechar);
                }
            }
            else if (sechar == '/'){
                while (true){
                    is.get(fstchar);
                    if (fstchar == '\n'){ // When the first character is at the end of the line, then change the line
                        os.put('\n');
                        break;
                    }
                }
            }
            else { // When '/' is regarded as the division in maths
                os.put(fstchar);
                os.put(sechar);
            }
        }
        else{ // No comment recognized, just output the original lines
            os.put(fstchar);
        }
    }
}
