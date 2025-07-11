# nums = [9,8,7,6,5,4,3,2,1]
# n = len(nums)
# for i in range(1,n):
#     key = nums[i]
#     j = i - 1
#     while j>=0 and nums[j]>key:
#         nums[j + 1] = nums[j]
#         j -= 1
#     nums [j + 1] = key

# print(nums)






num = [5,3,2,6,7,9,1]
n = len(num)
for i in range(1,n):
    key = num[i]
    j = i-1
    while j >= 0 and num[j] > key:
        num[j+1] = num[j]
        j -= 1
    num[j+1] = key

print(num)