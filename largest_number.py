# Method 1:

arr = [222,123,955,69,-98,-64]
largest = arr[0]
n = len(arr)
for i in range(0,n - 1):
    largest = max(largest,arr[i])
    
print(largest)


