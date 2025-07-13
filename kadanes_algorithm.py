#  Find the maximum subarray using kadanes algorithm:

nums = [-2,1,-3,4,-1,2,1,-5,4]
n =len(nums)
def max_subarray():
    maxi = float('-inf')
    total = 0
    for i in range(0,n):
        total = total + nums[i]     # 0 + (-2)= -2
        maxi = max(maxi,total)      # comparison -inf < -2
        if total < 0:    # if total is -2 it will reset it to 0
            total = 0        
    return maxi

print(max_subarray())