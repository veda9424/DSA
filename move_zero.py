nums = [1,0,2,0,3,0,4,0]

def move():
    n = len(nums)
    if n <= 1:     #  means the arr is like this [1]
        return

    i = 0
    while i < n:
        if nums[i] == 0:     # the starting of arr is with 0 or the position where the i is 0 [0,1,1,2,0,4]
            break
        i += 1  

    if i == n:      # means there is no zero in arr [12345]
        return

    j = i + 1
    while j < n:
        if nums[j] != 0:     # arr = [1,0,2,0]   i = 1 and j = 0  then after one more loop i = 0 and j = 2
            nums[i],nums[j] = nums[j],nums[i]    # after swapping arr = [1,2,0,0]
            i += 1      
        j += 1

move()
print(nums)



