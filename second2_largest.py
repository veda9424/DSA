arr = [1,2,3,4,5,6,7,8,9]
largest = float('-inf')
s_largest = float('-inf')
n = len(arr)
for i in range(0,n):
    largest = max(largest,arr[i])
for i in range(0,n):
    if arr[i] > s_largest and arr[i] != largest:
        s_largest = arr[i]

print(largest)
print(s_largest)