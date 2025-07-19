from typing import List

class Solution:
    def threesum(self,num:List[int])->List[List[int]]:
        ans = []
        n = len(nums)
        num.sort()
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
        
            # moving towards two pointer
            j = i + 1
            k = n - 1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1

                    # skip the dupplicates of j and k if occurred:
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans

nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
sol = Solution()
print(sol.threesum(nums))
