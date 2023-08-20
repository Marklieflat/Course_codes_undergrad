# num = [1,5,3,6,8]
# num.sort(reverse=True)
# print(num)

# numlist = list()
# while True:
#     inp = input('Enter a number:')
#     if inp == 'done':
#         break
#     inp = float(inp)
#     numlist.append(inp)
# a = sum(numlist)/len(numlist)
# print(a)

# header = 'From professor.xman@uct.edu Sat Jan 5 09:14:16 2008'
# words = header.split()
# address = words[1].split('@')
# print('The domain:',address[1])
# print('The month is :',words[3])

worddict = dict()
while True:
    word = input('Enter a word:')
    if word in worddict:
        worddict[word] = worddict[word]+1
    elif word == 'done':
        break
    else:
        worddict = 1
print(worddict)