#  Rotate an array k times (without slicing):

nums = [1,2,3,4,5,6,7,8,9,10]
def reverse(nums,left,right):
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1

k = int(input("Enter the number of times rotation required: "))
n = len(nums)
reverse(nums,n - k,n - 1)
reverse(nums,0,n - k - 1)
reverse(nums,0,n-1)
print(nums)


#  With the help of slicing:
nums2 = [1,2,3,4,5,6,7,8,9,10]
nums2[:] = nums2[n - k:n ] + nums2[0:n - k]
print(nums2)