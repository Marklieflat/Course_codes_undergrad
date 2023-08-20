inputs = input('<排序数字序列> ')
nums = inputs.split(' ')
m = len(nums)-1
while m > 0:
    for i in range(len(nums)-1):
        if float(nums[i]) > float(nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            continue
    
    x = ' '
    seq = x.join(nums)
    print(seq)
    m = m-1
    if nums == sorted(nums):
        break

sum = 0
for i in nums:
    sum += float(i)
average =  float(sum/len(nums))
r_average = round(average,2)
print('<平均值>', r_average)
