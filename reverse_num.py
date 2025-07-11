num = 1234
i = 0
while num > 0:
    a = num % 10    # 1234 % 10 = 4
    i = i * 10 + a   # 0 * 10 + 4 = 4
    num = num // 10  # 1234 // 10 = 123

print(i)   # i = 4321


nums = [1,2,3,4,5,6]
left = 0
right = len(nums) - 1
while left < right:
    nums[left],nums[right] = nums[right],nums[left]
    left += 1
    right -= 1

print(nums)

