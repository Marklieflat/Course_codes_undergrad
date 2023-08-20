#include <iostream>
using namespace std;

class A {
public:
    int a;
    A() {
        cout << "Constructing A" << endl;
        a = 1;
    }
    void display() {
        cout << "Displaying A" << endl;
        cout << a << endl;
    }
};

class B: public A {
public:
    int b;
    B() {
        cout << "Constructing B" << endl;
        b = 2;
    }
    void display() {
        cout << "Displaying B" << endl;
        cout << a << b << endl;
    }
};

class C: public B {
public:
    int c;
    C() {
        cout << "Constructing C" << endl;
        c = 3;
    }
    virtual void display() {
        cout << "Displaying C" << endl;
        cout << a << b << c << endl;
    }
};

class D: public C {
public:
    int d;
    D() {
        cout << "Constructing D" << endl;
        d = 4;
    }
    void display() {
        cout << "Displaying D" << endl;
        cout << a << b << c << d << endl;
    }
};

int main() {
    A oA;
    oA.display();
    cout << endl;

    B oB;
    oB.display();
    cout << endl;

    C oC;
    oC.display();
    cout << endl;

    D oD;
    oD.display();
    cout << endl;

    oA = oB;
    oA.display();
    cout << endl;

    oC = oD;
    oC.display();
    cout << endl;

    A* pA = &oB;
    pA->display();
    cout << endl;

    C* pC = &oD;
    pC->display();
    cout << endl;
}
