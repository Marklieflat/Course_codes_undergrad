name = input('<请输入文件名>')
fname = open("C:\\Users\\Mark\Desktop\\新建文件夹\\%s"% name, 'r',encoding="utf-8")
f = fname.readlines()
zM = []
zF = []
for line in f:
    inputs = line.split('\t')
    for i in inputs:
        if inputs.index(i) % 6 == 1:
            if i == 'M':
                zM.append(inputs[inputs.index(i)-1:inputs.index(i)+4])
            if i == 'F':
                zF.append(inputs[inputs.index(i)-1:inputs.index(i)+4])
                
mannumber = len(zM)
womannumber = len(zF)
sum_of_manrbc = 0
sum_of_womanrbc = 0
for i in range(len(zM)-1):
    sum_of_manrbc += eval(zM[i][2])
    
manrbc = sum_of_manrbc/len(zM)

for j in range(len(zF)-1):
    sum_of_womanrbc += eval(zF[j][2])

womanrbc = sum_of_womanrbc/len(zF)
print(mannumber)
print(womannumber)
print(manrbc)
print(womanrbc)

fname.close()