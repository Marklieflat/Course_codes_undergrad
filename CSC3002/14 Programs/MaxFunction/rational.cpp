/*
 * File: rational.cpp
 * ------------------
 * This file implements the Rational class.
 */

#include <string>
#include "rational.h"
using namespace std;

/*
 * Implementation notes: Constructors
 * ----------------------------------
 * There are three constructors for the Rational class.  The default
 * constructor creates a Rational with a zero value, the one-argument
 * form converts an integer to a Rational, and the two-argument form
 * allows specifying a fraction.  The constructors ensure that
 * the following invariants are maintained:
 *
 * 1. Zero is always represented as 0/1.
 * 2. The fraction is always reduced to lowest terms.
 * 3. The denominator is always positive.
 */

Rational::Rational() {
   num = 0;
   den = 1;
}

Rational::Rational(int n) {
   num = n;
   den = 1;
}

Rational::Rational(int x, int y) {
   if (x == 0) {
      num = 0;
      den = 1;
   } else {
      int g = gcd(abs(x), abs(y));
      num = x / g;
      den = abs(y) / g;
      if (y < 0) num = -num;
   }
}

/*
 * Implementation notes: toString
 * ------------------------------
 * Rationals that have integer values are converted to integer form;
 * all other values are displayed as fractions.
 */

string Rational::toString() {
   if (den == 1) {
      return to_string(num);
   } else {
      return to_string(num) + "/" + to_string(den);
   }
}

/*
 * Implementation notes: gcd
 * -------------------------
 * This implementation uses Euclid's algorithm to calculate the
 * greatest common divisor.
 */

int Rational::gcd(int x, int y) {
   int r = x % y;
   while (r != 0) {
      x = y;
      y = r;
      r = x % y;
   }
   return y;
}

/*
 * Implementation notes: operators
 * -------------------------------
 * The implementation of the operators follows directly from the
 * definitions.  Note that the equality operators depend on the
 * fraction being store in lowest terms.
 */

ostream & operator<<(ostream & os, Rational rat) {
   os << rat.toString();
   return os;
}

Rational operator+(Rational r1, Rational r2) {
   return Rational(r1.num * r2.den + r2.num * r1.den, r1.den * r2.den);
}

Rational operator-(Rational r1, Rational r2) {
   return Rational(r1.num * r2.den - r2.num * r1.den, r1.den * r2.den);
}

Rational operator*(Rational r1, Rational r2) {
   return Rational(r1.num * r2.num, r1.den * r2.den);
}

Rational operator/(Rational r1, Rational r2) {
   return Rational(r1.num * r2.den, r1.den * r2.num);
}

Rational & operator+=(Rational & r1, Rational r2) {
   return r1 = r1 + r2;
}

Rational & operator-=(Rational & r1, Rational r2) {
   return r1 = r1 - r2;
}

Rational & operator*=(Rational & r1, Rational r2) {
   return r1 = r1 * r2;
}

Rational & operator/=(Rational & r1, Rational r2) {
   return r1 = r1 / r2;
}

Rational operator++(Rational & rat) {
   return rat += 1;
}

Rational operator++(Rational & rat, int) {
   Rational old = rat;
   rat += 1;
   return old;
}

Rational operator--(Rational & rat) {
   return rat -= 1;
}

Rational operator--(Rational & rat, int) {
   Rational old = rat;
   rat -= 1;
   return old;
}

bool operator==(Rational r1, Rational r2) {
   return r1.num == r2.num && r1.den == r2.den;
}

bool operator!=(Rational r1, Rational r2) {
   return !(r1 == r2);
}

bool operator<(Rational r1, Rational r2) {
   return r1.num * r2.den < r2.num * r1.den;
}

bool operator<=(Rational r1, Rational r2) {
   return r1.num * r2.den <= r2.num * r1.den;
}

bool operator>(Rational r1, Rational r2) {
   return r1.num * r2.den > r2.num * r1.den;
}

bool operator>=(Rational r1, Rational r2) {
   return r1.num * r2.den >= r2.num * r1.den;
}
