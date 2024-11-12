/*
 * File: calendar.cpp
 * ------------------
 * This file implements the calendar.h interface
 */

#include "calendar.h"
// TODO
#include <string>
#include"strlib.h"
#include<iostream>
#include"error.h"
using namespace std;

/*******************Problem 1, part 1******************/

string monthToString(Month month){
    switch (month){
        case JANUARY : return "JANUARY";
        case FEBRUARY : return "FEBRUARY";
        case MARCH : return "MARCH";
        case APRIL : return "APRIL";
        case MAY : return "MAY";
        case JUNE : return "JUNE";
        case JULY : return "JULY";
        case AUGUST : return "AUGUST";
        case SEPTEMBER : return "SEPTEMBER";
        case OCTOBER : return "OCTOBER";
        case NOVEMBER : return "NOVEMBER";
        case DECEMBER : return "DECEMBER";
        default : return "???" ;
    }
}

bool isLeapYear(int year){
    if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)){
        return true;
    }
    else{
        return false;
    }
}

int daysInMonth(Month month, int year){
    switch (month){
        case JANUARY :
        case MARCH :
        case MAY :
        case JULY :
        case AUGUST :
        case OCTOBER :
        case DECEMBER :
            return 31;
        case FEBRUARY :
            return (isLeapYear(year)) ? 29 : 28;
        default : return 30;
    }
}

Month operator++(Month & month, int){
    Month ans = month;
    month = Month(month + 1);
    return ans;
}

/*******************Problem 1, part 2******************/

void Date::initDate(int dd, Month mm, int yyyy){
    if (dd < 1 || dd > daysInMonth(mm, yyyy)){
        error("Cannot find such date in the calender.");
    }
    day = dd;
    month = mm;
    year = yyyy;
    dayInYear = dd;
    for (Month i = JANUARY; i < month; i++){
        dayInYear += daysInMonth(i,yyyy);
    }
}


Date::Date(){
    initDate(1, JANUARY, 1900);
}

Date::Date(int day, Month month, int year){
    initDate(day, month, year);
}

Date::Date(Month month, int day, int year){
    initDate(day, month, year);
}

int Date::getDay(){
    return day;
}

Month Date::getMonth(){
    return month;
}

int Date::getYear(){
    return year;
}

string Date::toString(){
    return integerToString(day) + "-" + capitalize(monthToString(month)) + "-" + integerToString(year);
}

string Date::capitalize(string str){
    return toUpperCase(str.substr(0,1)) + toLowerCase(str.substr(1,2));
}

/*******************Problem 1, part 3******************/

std::ostream & operator<<(std::ostream & os, Date date){
    return os << date.toString();
}

Date operator+(Date date, int delta){
    int day1 = date.dayInYear;
    int year1 = date.getYear();
    Month month1 = JANUARY;
    int day2 = day1 + delta;
    while (day2 > 365 + isLeapYear(year1)){
        day2 -= (365 + isLeapYear(year1));
        year1 ++;
    }
    while (day2 < 0){
        day2 += (365 + isLeapYear(year1));
        year1 --;
    }
    while (day2 > daysInMonth(month1, year1)){
        day2 -= daysInMonth(month1, year1);
        month1 ++;
    }
    return Date(day2, month1, year1);
}

Date operator-(Date date, int delta){
    return date + (-delta);
}

int operator-(Date d1, Date d2){
    int dayinyear1 = d1.dayInYear;
    int dayinyear2 = d2.dayInYear;
    int year1 = d1.getYear();
    int year2 = d2.getYear();
    if (year1 < year2){
        for (int i = year1; i < year2; i++){
            dayinyear2 += (365 + isLeapYear(i));
        }
        return dayinyear2 - dayinyear1;
    }
    else if (year1 == year2) return abs(dayinyear1 - dayinyear2);
    else{
        for (int i = year2; i < year1; i++){
            dayinyear1 += (365 + isLeapYear(i));
        }
        return dayinyear1 - dayinyear2;
    }
}

Date & operator+=(Date & date, int delta){
    date = date + delta;
    return date;
}

Date & operator-=(Date & date, int delta){
    date = date - delta;
    return date;
}

Date operator++(Date & date){
    return date + 1;
}

Date operator++(Date & date, int){
    Date old = date;
    date = date + 1;
    return old;
}

Date operator--(Date & date){
    return date - 1;
}

Date operator--(Date & date, int){
    Date old = date;
    date = date - 1;
    return old;
}

bool operator==(Date d1, Date d2){
    return d1 - d2 == 0;
}

bool operator!=(Date d1, Date d2){
    return d1 - d2 != 0;
}

bool operator<(Date d1, Date d2){
    if (d1.getYear() < d2.getYear()) return 1;
    else if(d1.getYear() > d2.getYear()) return 0;
    else {
        if (d1.getMonth() <  d2.getMonth()) return 1;
        else if (d1.getMonth() >  d2.getMonth()) return 0;
        else {
            if (d1.getDay() < d2.getDay()) return 1;
            else {
                return 0;
            }
        }
    }
}

bool operator<=(Date d1, Date d2){
    return (d1 < d2) || (d1 == d2);
}

bool operator>(Date d1, Date d2){
    return (d1 < d2) ? 0 : 1;
}

bool operator>=(Date d1, Date d2){
    return (d1 > d2) || (d1 == d2);
}


