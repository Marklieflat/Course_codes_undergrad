def isAnagram(s1,s2):
    ls1 = [a for a in s1]
    ls2 = [b for b in s2]
    ls1sort = sorted(ls1)
    ls2sort = sorted(ls2)
    if ls1sort == ls2sort:
        return True
    else:
        return False

firstword = input('Please enter the first word:')
secondword = input('Please enter the second word:')
if isAnagram(firstword,secondword) == True:
    print('is an anagram.')
else:
    print('is not an anagram.')