#include <iostream>

using namespace std;

int main()
{
    cout << hex << -1 << ' '
    << (-1 << 1) << ' '
    << (-1 >> 1) << ' '
    << unsigned(-1) << ' '
    << (unsigned(-1) << 1) << ' '
    << (unsigned(-1) >> 1) << endl;
    return 0;
}
