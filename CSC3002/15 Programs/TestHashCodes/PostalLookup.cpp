/*
 * File: PostalLookup.cpp
 * ----------------------
 * This program looks up a state abbreviation from a map containing
 * the abbreviations of the 50 U.S. states.
 */

#include <iostream>
#include "simpio.h"
#include "stringmap.h"
using namespace std;

/* Function prototypes */

void initStateMap(StringMap & map);
void put(StringMap & map, string key, string value);

/* Main program */

int main() {
   StringMap stateMap;
   initStateMap(stateMap);
   while (true) {
      string code = getLine("Enter two-letter state code: ");
      if (code == "") break;
      string name = stateMap.get(code);
      if (name == "") {
         cout << code << " is not a valid abbreviation" << endl;
      } else {
         cout << code << " = " << stateMap.get(code) << endl;
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

void initStateMap(StringMap & map) {
   put(map, "AK", "Alaska");
   put(map, "AL", "Alabama");
   put(map, "AR", "Arkansas");
   put(map, "AZ", "Arizona");
   put(map, "CA", "California");
   put(map, "CO", "Colorado");
   put(map, "CT", "Connecticut");
   put(map, "DE", "Delaware");
   put(map, "FL", "Florida");
   put(map, "GA", "Georgia");
   put(map, "HI", "Hawaii");
   put(map, "IA", "Iowa");
   put(map, "ID", "Idaho");
   put(map, "IL", "Illinois");
   put(map, "IN", "Indiana");
   put(map, "KS", "Kansas");
   put(map, "KY", "Kentucky");
   put(map, "LA", "Louisiana");
   put(map, "MA", "Massachusetts");
   put(map, "MD", "Maryland");
   put(map, "ME", "Maine");
   put(map, "MI", "Michigan");
   put(map, "MN", "Minnesota");
   put(map, "MO", "Missouri");
   put(map, "MS", "Mississippi");
   put(map, "MT", "Montana");
   put(map, "NC", "North Carolina");
   put(map, "ND", "North Dakota");
   put(map, "NE", "Nebraska");
   put(map, "NH", "New Hampshire");
   put(map, "NJ", "New Jersey");
   put(map, "NM", "New Mexico");
   put(map, "NV", "Nevada");
   put(map, "NY", "New York");
   put(map, "OH", "Ohio");
   put(map, "OK", "Oklahoma");
   put(map, "OR", "Oregon");
   put(map, "PA", "Pennsylvania");
   put(map, "RI", "Rhode Island");
   put(map, "SC", "South Carolina");
   put(map, "SD", "South Dakota");
   put(map, "TN", "Tennessee");
   put(map, "TX", "Texas");
   put(map, "UT", "Utah");
   put(map, "VA", "Virginia");
   put(map, "VT", "Vermont");
   put(map, "WA", "Washington");
   put(map, "WI", "Wisconsin");
   put(map, "WV", "West Virginia");
   put(map, "WY", "Wyoming");
}

void put(StringMap & map, string key, string value) {
   map.put(key, value);
   int bucket = hashCode(key) % 7;
   cout << "hashCode(\"" << key << "\") = " << hashCode(key) << " -> "
        << bucket << endl;
}
