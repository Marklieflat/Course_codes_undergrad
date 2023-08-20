/*
 * File: TestEmployeeClass.cpp
 * ---------------------------
 * This program checks that each of the three subclasses supports
 * the getName and computeSalary methods.
 */

#include <iostream>
#include "employee.h"
#include "vector.h"
using namespace std;

int main() {
   HourlyEmployee cratchit("Bob Cratchit");
   cratchit.setHourlyRate(1.00);
   cratchit.setHoursWorked(90);
   CommissionedEmployee fezziwig("Mr Fezziwig");
   fezziwig.setBaseSalary(50);
   fezziwig.setCommissionRate(0.05);
   fezziwig.setSalesVolume(2000);
   SalariedEmployee scrooge("Ebenezer Scrooge");
   scrooge.setSalary(500);
   Vector<Employee *> payroll;
   payroll.add(&cratchit);
   payroll.add(&fezziwig);
   payroll.add(&scrooge);
   foreach (Employee *ep in payroll) {
      cout << ep->getName() << ": " << ep->getPay() << endl;
   }
}
