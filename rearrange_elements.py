# rearrange elements by sign alternatively:

nums = [5,10,-3,-1,-10,6]
n = len(nums)
result = [0]*n
def rearrange():
    pos_index = 0
    neg_index = 1
    for i in range(0,n):
        if nums[i]>0:
            result[pos_index] = nums[i]
            pos_index += 2
        else:
            result[neg_index] = nums[i]
            neg_index += 2
    return result

print(rearrange())