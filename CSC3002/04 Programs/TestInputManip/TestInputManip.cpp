#include <iostream>
#include <sstream>
#include <iomanip>
#include <cmath>
//#include "console.h"
using namespace std;

int main() {
    char ch1, ch2, ch3, ch4, ch5, ch6;
    cout << "Enter at least 6 characters: ";
    cin >> noskipws >> ch1 >> ch2
        >> ws >> ch3 >> ch4
        >> skipws >> ch5 >> ch6;
    cout << "ch1 = '" << ch1 << "'; ch2 = '" << ch2
         << "'; ch3 = '" << ch3 << "'; ch4 = '" << ch4
         << "'; ch5 = '" << ch5 << "'; ch6 = '" << ch6
         << "'." << endl;

    istringstream iss(" rui ray");
    string str1, str2;
    iss >> str1 >> noskipws >> str2;
    cout << "str1 = '" << str1 << "'; str2 = '" << str2
         << "'." << endl;
    return(0);
}
