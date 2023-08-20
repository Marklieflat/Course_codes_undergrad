# working_hours = int(input('Enter your working hours:'))
# hourly_rate = float(input('Enter your hourly rate:'))
# if working_hours > 40:
#     Salary = 40*hourly_rate + (working_hours-40)*1.5*hourly_rate
#     print('your salary is:',Salary)
# else:
#     Salary=working_hours*hourly_rate
#     print('your salary is:',Salary)


# month = int(input('Enter a month (1-12):'))
# day = int(input('Enter a day (1-31);'))
# days_in_month = (31,28,31,30,31,30,31,31,30,31,30,31)
# if day<days_in_month[month-1]:
#     print(month,day+1)
# else:
#     month = month%12 +1
#     print(month,1)


set = [1,2,3,4,5,6]
total = 0
print('Before',total)
for numbers in set:
    total = total + numbers
print('After',total)