# a,b,c = eval(input('Enter coefficient a,b and c in the equation:'))
# if b**2-4*a*c >0 :
#     X1=((-b+sqrt(b**2-4*a*c))/(2*a))
#     X2=((-b-sqrt(b**2-4*a*c)))/(2*a)
#     print('The two roots of the equation are ',X1 and X2)
# elif b**2-4*a*c == 0 :
#     X=((-b/(2*a)))
#     print('There is only one root',X)
# else :
#     print('The equation has no real roots')


# inputs = input('Enter the month and year number:')
# month, year =inputs.split(',')
# month = int(month)
# year = int(year)
# if month in (1,3,5,7,8,10,12):
#     days=31
#     print(days)
# elif month in (4,6,9,11):
#     days=30
#     print(days)
# elif month == 2:
#     if year%4 ==0:
#         days=29
#         print(days)
#     else:
#         days=28
#         print(days)
# else:
#     print('invalid error')


# a = int(input('Enter an integer:'))
# for i in range(1,a+1):
#     print("  "*((a-i)*2),end='  ')
#     for j in range(i,1,-1):
#         print(j, end = '  ')
#     for j in range(1,i):
#         print(j, end = '  ')
#     print(i)

# a = int(input('input:'))
# str1 = ' 1'
# for i in range(1,a+1):
#     print(str1.center(50))
#     x = str(i+1)
#     str1 = '%2s %2s %2s' % (x,str1,x)