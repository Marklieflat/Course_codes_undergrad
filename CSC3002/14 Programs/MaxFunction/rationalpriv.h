/*
 * File: rationalpriv.h
 * --------------------
 * This file contains the private section (and the friends declarations)
 * for the Rational class.
 */

/* Declare the operator functions as friends */

   friend Rational operator+(Rational r1, Rational r2);
   friend Rational operator-(Rational r1, Rational r2);
   friend Rational operator*(Rational r1, Rational r2);
   friend Rational operator/(Rational r1, Rational r2);
   friend bool operator==(Rational r1, Rational r2);
   friend bool operator!=(Rational r1, Rational r2);
   friend bool operator<(Rational r1, Rational r2);
   friend bool operator<=(Rational r1, Rational r2);
   friend bool operator>(Rational r1, Rational r2);
   friend bool operator>=(Rational r1, Rational r2);

private:

/* Private function */

   int gcd(int x, int y);

/* Instance variables */

   int num;    /* The numerator of this Rational object   */
   int den;    /* The denominator of this Rational object */
