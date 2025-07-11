nums = [1,2,3,4,5,7,8,9]
freq = {}
n = len(nums)
for i in range(0,n + 1):
    freq[i] = 0
for j in nums:
    freq[j] = 1

for k,v in freq.items():
    if v == 0:
        print(k)