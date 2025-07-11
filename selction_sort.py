nums = [5, 7, 8, 6, 3, 2, 4, 1, 9]

# ASCENDING ORDER

def selection_sort_ascending(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums [min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums

x = selection_sort_ascending(nums)
print(x)

# DESCENDING ORDER

def selection_sort_descending(nums):
    n = len(nums)
    for i in range(0,n):
        max_index = i
        for j in range(i + 1, n):
            if nums[j] > nums [max_index]:
                max_index = j
        nums[i],nums[max_index] = nums[max_index],nums[i]
    return nums

y = selection_sort_descending(nums)
print(y)