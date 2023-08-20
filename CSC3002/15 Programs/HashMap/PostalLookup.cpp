/*
 * File: PostalLookup.cpp
 * ----------------------
 * This program looks up a state abbreviation from a map containing
 * the abbreviations of the 50 U.S. states.
 */

#include <iostream>
#include "hashmap.h"
//include "simpio.h"
using namespace std;

/* Function prototypes */

void initStateMap(HashMap<string,string> & map);

/* Main program */

int main() {
   HashMap<string,string> stateMap;
   initStateMap(stateMap);
   while (true) {
      cout << "Enter two-letter state code: ";
      string code;
      getline(cin, code);
      if (code == "") break;
      if (stateMap.containsKey(code)) {
         cout << code << " = " << stateMap.get(code) << endl;
      } else {
         cout << code << " = ???" << endl;
      }
   }
   return 0;
}

/*
 * Function: initStateMap
 * Usage: initStateMap(map);
 * -------------------------
 * Initializes the map so that it contains the two-letter abbreviations
 * for the 50 states.
 */

void initStateMap(HashMap<string,string> & map) {
   map.put("AK", "Alaska");
   map.put("AL", "Alabama");
   map.put("AR", "Arkansas");
   map.put("AZ", "Arizona");
   map.put("CA", "California");
   map.put("CO", "Colorado");
   map.put("CT", "Connecticut");
   map.put("DE", "Delaware");
   map.put("FL", "Florida");
   map.put("GA", "Georgia");
   map.put("HI", "Hawaii");
   map.put("IA", "Iowa");
   map.put("ID", "Idaho");
   map.put("IL", "Illinois");
   map.put("IN", "Indiana");
   map.put("KS", "Kansas");
   map.put("KY", "Kentucky");
   map.put("LA", "Louisiana");
   map.put("MA", "Massachusetts");
   map.put("MD", "Maryland");
   map.put("ME", "Maine");
   map.put("MI", "Michigan");
   map.put("MN", "Minnesota");
   map.put("MO", "Missouri");
   map.put("MS", "Mississippi");
   map.put("MT", "Montana");
   map.put("NC", "North Carolina");
   map.put("ND", "North Dakota");
   map.put("NE", "Nebraska");
   map.put("NH", "New Hampshire");
   map.put("NJ", "New Jersey");
   map.put("NM", "New Mexico");
   map.put("NV", "Nevada");
   map.put("NY", "New York");
   map.put("OH", "Ohio");
   map.put("OK", "Oklahoma");
   map.put("OR", "Oregon");
   map.put("PA", "Pennsylvania");
   map.put("RI", "Rhode Island");
   map.put("SC", "South Carolina");
   map.put("SD", "South Dakota");
   map.put("TN", "Tennessee");
   map.put("TX", "Texas");
   map.put("UT", "Utah");
   map.put("VA", "Virginia");
   map.put("VT", "Vermont");
   map.put("WA", "Washington");
   map.put("WI", "Wisconsin");
   map.put("WV", "West Virginia");
   map.put("WY", "Wyoming");
}
