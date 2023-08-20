/*
 * File: morsecode.cpp
 * -------------------
 * This file implements the morsecode.h interface.
 */

#include "morsecode.h"
using namespace std;
//TODO

/*
 * Function: createMorseCodeMap
 * Usage: Map<string> map = createMorseCodeMap();
 * ----------------------------------------------
 * Returns a map in which each uppercase letter is mapped into its
 * Morse code equivalent.
 */

Map<string,string> createMorseCodeMap() {
   Map<string,string> map;
   map["A"] = ".-";
   map["B"] = "-...";
   map["C"] = "-.-.";
   map["D"] = "-..";
   map["E"] = ".";
   map["F"] = "..-.";
   map["G"] = "--.";
   map["H"] = "....";
   map["I"] = "..";
   map["J"] = ".---";
   map["K"] = "-.-";
   map["L"] = ".-..";
   map["M"] = "--";
   map["N"] = "-.";
   map["O"] = "---";
   map["P"] = ".--.";
   map["Q"] = "--.-";
   map["R"] = ".-.";
   map["S"] = "...";
   map["T"] = "-";
   map["U"] = "..-";
   map["V"] = "...-";
   map["W"] = ".--";
   map["X"] = "-..-";
   map["Y"] = "-.--";
   map["Z"] = "--..";
   return map;
}


//TODO

string translateLettersToMorse(std::string line){
    string output;
    for (int i = 0; i < int(line.length()); i++){
        string current;
        current += line[i];
        string code = LETTERS_TO_MORSE[current];
        if (code != ""){
            output += code;
            output += ' ';
        }
    }
    return output;
}

string translateMorseToLetters(string line){
    string output;
    int start = 0;
    int end;
    for (int i = 0; i < int(line.length()); i++){
        if (line[i] == ' '){
            end = i;
            output += MORSE_TO_LETTERS[line.substr(start, end - start)];
            start = i + 1;
        }
        else if (i == int(line.length()-1)){
            end = i;
            output += MORSE_TO_LETTERS[line.substr(start, end - start + 1)];
        }
    }
    return output;
}

Map<string,string> invertMap(const Map<string,string> & map){
    Map<string,string> newmap;
    for (string key : map){
        newmap.put(map[key],key);
    }
    return newmap;
}





