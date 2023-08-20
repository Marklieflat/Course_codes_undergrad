/*
 * File: rational.h
 * ----------------
 * This interface exports a class for representing rational numbers.
 */

#ifndef _rational_h
#define _rational_h

#include <string>
#include <iostream>
/*
 * Class: Rational
 * ---------------
 * The Rational class is used to represent rational numbers, which
 * are defined to be the quotient of two integers.
 */

class Rational {

public:

/*
 * Constructor: Rational
 * Usage: Rational zero;
 *        Rational num(n);
 *        Rational r(x, y);
 * ------------------------
 * Creates a Rational object.  The default constructor creates the
 * rational number 0.  The single-argument form creates a rational
 * equal to the specified integer, and the two-argument form creates
 * a rational number corresponding to the fraction x/y.
 */

   Rational();
   Rational(int n);
   Rational(int x, int y);

/*
 * Method: toString()
 * Usage: string str = r.toString();
 * ---------------------------------
 * Returns the string representation of this rational number.
 */

   std::string toString();

#include "rationalpriv.h"
};

/*
 * Operator: <<
 * ------------
 * Overloads the << operator so that it is able to display Rational values.
 */

std::ostream & operator<<(std::ostream & os, Rational rat);

/*
 * Operators: +, -, *, /
 * ---------------------
 * Overloads these operators so that they work with Rational objects.
 */

Rational operator+(Rational r1, Rational r2);
Rational operator-(Rational r1, Rational r2);
Rational operator*(Rational r1, Rational r2);
Rational operator/(Rational r1, Rational r2);

/*
 * Operators: +=, -=, *=, /=
 * -------------------------
 * Overloads the shorthand assignment operators to work with Rational objects.
 */

Rational & operator+=(Rational & r1, Rational r2);
Rational & operator-=(Rational & r1, Rational r2);
Rational & operator*=(Rational & r1, Rational r2);
Rational & operator/=(Rational & r1, Rational r2);

/*
 * Operators: ++, --
 * -----------------
 * Overloads the increment/decrement operators to work with Rational objects.
 */

Rational operator++(Rational & rat);
Rational operator++(Rational & rat, int);
Rational operator--(Rational & rat);
Rational operator--(Rational & rat, int);

/*
 * Operators: ==, !=, <, <=, >, >=
 * -------------------------------
 * Overloads the relational operators to work with Rational objects.
 */

bool operator==(Rational r1, Rational r2);
bool operator!=(Rational r1, Rational r2);
bool operator<(Rational r1, Rational r2);
bool operator<=(Rational r1, Rational r2);
bool operator>(Rational r1, Rational r2);
bool operator>=(Rational r1, Rational r2);

#endif
