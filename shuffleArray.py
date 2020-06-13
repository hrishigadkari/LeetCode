nums = [1,2,3,4,4,3,2,1]
n = 4
arr = []
for i in range(0,n):           
    print(i)
    arr.append(nums[i])
    arr.append(nums[n+i])
    print(arr)
print(arr)