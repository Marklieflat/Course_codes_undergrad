# # Q2

# password = input('Enter your password:')
# def isValid():
#     if len(password) < 8:
#         return False

#     if password.isalnum() == False:
#         return False

#     count = 0
#     for i in password:
#         if i.isdigit():
#             count += 1
#     if count < 2:
#         return False
    
#     return True

# def ans():
#     if isValid():
#         print('Your password is valid')
#     else:
#         print('Your password is invalid')

# ans()

# Q3
# def prefix(s1,s2):
    
#     # the length of potential index, starts with 0
#     pref_count = 0
    
#     # iteratively test the charecters in the same position
#     for index in range(min(len(s1), len(s2))):
        
#         # determine if the charecters are the same 
#         if s1[index] == s2[index]:
#             pref_count += 1
        
#         # otherwise, stop the whole iteration
#         else:
#             break
    
#     # return the prefix using slicing operation
#     return s1[:pref_count]

# # sample test of Q3

# s1 = input("Enter the first string:")
# s2 = input("Enter the second string:")

# print("The longest prefix of the two strings is '%s'." % prefix(s1,s2))

