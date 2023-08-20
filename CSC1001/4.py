a=1
b=2
c=a**b
while a<=5:
    print('%-8d%-8d%-8d'%(a,b,c))
    a+=1
    b+=1
    c=a**b