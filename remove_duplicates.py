#  Remove duplicate elements in the array after sorting it and return the num of duplicate elements:

nums = [1,1,1,2,3,4,4,5,6,8,7,8,9,10,10,11]
n =len(nums)
if n == 1:
    print(1)
i = 0
j = i + 1
while j < n:
    if nums[j] != nums[i]:
        i += 1
        nums[i],nums[j]=nums[j],nums[i]
    j += 1

print(i)
print(nums)