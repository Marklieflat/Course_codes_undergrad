/*
 * File: employee.cpp
 * ------------------
 * This file provides a stub implementation of the employee.h interface.
 */

#include <string>
#include "employee.h"
using namespace std;

string Employee::getName() {
   return name;
}

void Employee::setName(string name) {
   this->name = name;
}

HourlyEmployee::HourlyEmployee(string name) {
   setName(name);
}

double HourlyEmployee::getPay() {
   return hoursWorked * hourlyRate;
}

void HourlyEmployee::setHourlyRate(double rate) {
   hourlyRate = rate;
}

void HourlyEmployee::setHoursWorked(double hours) {
   hoursWorked = hours;
}

CommissionedEmployee::CommissionedEmployee(string name) {
   setName(name);
}

double CommissionedEmployee::getPay() {
   return baseSalary + commissionRate * salesVolume;
}

void CommissionedEmployee::setBaseSalary(double dollars) {
   baseSalary = dollars;
}

void CommissionedEmployee::setCommissionRate(double rate) {
   commissionRate = rate;
}

void CommissionedEmployee::setSalesVolume(double dollars) {
   salesVolume = dollars;
}

SalariedEmployee::SalariedEmployee(string name) {
   setName(name);
}

double SalariedEmployee::getPay() {
   return salary;
}

void SalariedEmployee::setSalary(double salary) {
   this->salary = salary;
}
