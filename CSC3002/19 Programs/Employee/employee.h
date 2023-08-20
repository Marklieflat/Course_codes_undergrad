/*
 * File: employee.h
 * ----------------
 * This file provides a skeletal interface for an Employee class with three
 * subclasses: HourlyEmployee, CommissionedEmployee, and SalariedEmployee.
 * Lines marked with // comments are excluded from the abbreviated listing.
 */

#ifndef _employee_h
#define _employee_h

#include <string>

/*
 * Class: Employee
 * ---------------
 * This class defines the root of the Employee hierarchy.  Employee is
 * an abstract class, which means that there are no objects whose primary
 * type is Employee.  Every object is constructed as one of the subclasses.
 * The getPay method is declared using the virtual keyword, which means
 * that it can be overridden by its subclasses.  The "= 0" notation at the
 * end of the prototype marks getPay as a "pure virtual" method, which
 * is implemented only in the subclasses.
 */

class Employee {
public:
   std::string getName();
   virtual double getPay() = 0;
   void setName(std::string name);             //
private:                                       //
   std::string name;                           //
};

/*
 * Subclasses: HourlyEmployee, CommissionedEmployee, SalariedEmployee
 * ------------------------------------------------------------------
 * These classes represent the concrete manifestations of the abstract
 * Employee class.  Each subclass inherits the getName method from
 * Employee, but defines its own version of the getPay method.
 */

class HourlyEmployee : public Employee {
public:
   virtual double getPay();
   void setHourlyRate(double rate);
   void setHoursWorked(double hours);
   HourlyEmployee(std::string name);           //
private:                                       //
   double hourlyRate;                          //
   double hoursWorked;                         //
};

class CommissionedEmployee : public Employee {
public:
   virtual double getPay();
   void setBaseSalary(double dollars);
   void setCommissionRate(double rate);
   void setSalesVolume(double dollars);
   CommissionedEmployee(std::string name);     //
private:                                       //
   double baseSalary;                          //
   double commissionRate;                      //
   double salesVolume;                         //
};

class SalariedEmployee : public Employee {
public:
   virtual double getPay();
   void setSalary(double salary);
   SalariedEmployee(std::string name);         //
private:                                       //
   double salary;                              //
};

#endif
