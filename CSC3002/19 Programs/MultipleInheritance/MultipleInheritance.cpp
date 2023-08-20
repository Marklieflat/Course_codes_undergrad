#include <iostream>
using namespace std;

class A {
public:
    int a;
    A() {
        cout << "Constructing A" << endl;
        a = 1;
    }
    display() {
//    virtual display() {
        cout << "Displaying A" << endl;
        cout << a << endl;
    }
};

class B : public A {
//class B : virtual public A {
public:
    int b;
    B() {
        cout << "Constructing B" << endl;
        b = 2;
    }
    display() {
        cout << "Displaying B" << endl;
        cout << a << b << endl;
    }
};

class C : public A {
//class C : virtual public A {
public:
    int c;
    C() {
        cout << "Constructing C" << endl;
        c = 3;
    }
    display() {
        cout << "Displaying C" << endl;
        cout << a << c << endl;
    }
};

class D: public B, public C {
public:
    int d;
    D() {
        cout << "Constructing D" << endl;
        d = 4;
    }
    display() {
        cout << "Displaying D" << endl;
//        cout << b << c << d << endl;
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

    A* pa = &oD;
    pa->display();
    cout << endl;

    B* pb = &oD;
    pb->display();
    cout << endl;

    C* pc = &oD;
    pc->display();
    cout << endl;

    return 0;
}
