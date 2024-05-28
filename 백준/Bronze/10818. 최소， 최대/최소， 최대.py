n = int(input())
nums = list(map(int,input().split()))
max1 = -1000001
min1 = 1000001
for i in range(n):
    if min1 > nums[i]:
        min1 = nums[i]
    if max1 < nums[i]:
        max1 = nums[i]  
print(min1,max1)
    

