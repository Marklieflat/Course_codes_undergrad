#q2

# # a = input('Interger:')
# def reverse(numbers):
#     numbers = str(numbers)
#     list(numbers)
#     if numbers == numbers[::-1]:
#         return int(numbers)
#     else:
#         return
# # reverse(a)


from math import sqrt
def is_primenumber(numbers):
    for i in range(2, int(sqrt(numbers) + 1)):
        while (numbers % i == 0):
            return False
    return True


# def is_palindromicprime(numbers):
#     if is_primenumber(numbers) and reverse(numbers):
#         return True
#     else:
#         return False
    
# num = 2
# count = 0 
# while count < 100:
#     if is_palindromicprime(num):
#         print('%6d' % num , end = ' ')
#         count += 1
#         if count % 10 == 0:
#             print('',end = '\n') 
#     num += 1


# Q3

# from math import sqrt
# def isvalid(side1,side2,side3):
#     if side1 + side2 > side3:
#         return True
#     elif side1 + side3 > side2:
#         return True
#     elif side2 + side3 > side1:
#         return True
#     else:
#         return False

# def area (side1,side2,side3):
#     cosx = ((side1)**2 + (side2)**2 - (side3)**2)/(2*side1*side2)
#     sinx = sqrt(1-(cosx)**2)
#     area = 1/2 *side1*side2*sinx 
#     return area

# inputs = input('Enter 3 lengths of sides of a triangle: ')
# a,b,c = inputs.split(' ')
# a = eval(a)
# b = eval(b)
# c = eval(c)
# isvalid(a,b,c)
# a = area(a,b,c)
# print(a)

# Q4
def factorial(num):
    result = 1
    for i in range(1,num+1):
        result = result*i
    return result

def cb(k,n):
    result = (factorial(n))/(factorial(n-k)*factorial(k))
    return result

N = eval(input('Please input the number of lines for Young Triangle:'))
for line in range(N):
    print('%4s'%' '*(N-line),end='')
    for k in range(line+1):
        print('%4d' % cb(line,k),end='')
        print('%4s' % ' ',end='')
    print("",end='\n') 