# S = []
# for odd_nums in range(1,56):
#     if odd_nums % 2 ==1 :
#         S.append(odd_nums)
# print(S)

# s =[]
# for nums in range(27,160):
#     if nums % 4 ==0 and nums % 10 ==6:
#         s.append(nums)
# print(s)

# a = input('Please enter the first word:')
# b = input('please enter the second word:')
# list1 = list(a)
# list2 = list(b)
# list1.sort()
# list2.sort()
# if list1==list2:
#     print('Yes')
# else:
#     print('no')
    
# s=[]
# a = int(input('Please enter an integer n, n>2:'))
# for nums in range(2,a):
#     for num1 in range(3,a-1):
#         if nums % num1 == 0:
#             s.append(nums)
# s.sort()
# print(s)#youwenti

i = int(input('Please enter an integer n:'))
prime_list = []
for denominator in range(2,i):
    prime = True
    for i in range(2,int(denominator**0.5 + 1)):
        if denominator % i == 0:
            prime = False
            break
    if prime:
        prime_list.append(denominator)
print(prime_list)

# if (k % 7 == 0)
