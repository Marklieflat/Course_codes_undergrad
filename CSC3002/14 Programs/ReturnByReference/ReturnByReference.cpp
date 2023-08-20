#include <iostream>
using namespace std;

int & ReturnByReference(int a)
{
    cout << "Into ReturnByReference:" << endl;
    cout << "&a = " << &a << "; a = " << a << endl;
//    int* b = &a;
    int* b = new int(a);
    cout << "&b = " << &b << "; b = " << b << "; *b = " << *b << endl;
    cout << "Out of ReturnByReference:" << endl;
    return *b;
}

int CallByReference(int & a)
{
    cout << "Into CallByReference:" << endl;
    cout << "&a = " << &a << "; a = " << a << endl;
    cout << "Out of CallByReference:" << endl;
    return a;
}

int main()
{
    int a = 1;
    cout << "&a = " << &a << "; a = " << a << endl;
    a = CallByReference(ReturnByReference(a)=a+1);
    cout << "&a = " << &a << "; a = " << a << endl;
    return 0;
}