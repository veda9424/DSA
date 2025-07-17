nums = [1,2,3,99,100,98,97,5,101]
n = len(nums)
my_set = set()
def longest_sequence():
    for i in range(0,n):
        my_set.add(nums[i])
    longest = 0
    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            while x + 1 in my_set:
                count += 1
                x += 1
            longest = max(longest,count)
    return longest

print(longest_sequence())


