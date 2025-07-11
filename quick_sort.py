class Solution:

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i <= high and arr[i] <= pivot:
                i += 1
            while j >= low and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSort(self, arr, low, high):
        if low < high:
            p_index = self.partition(arr, low, high)
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)

arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]
sol = Solution()
sol.quickSort(arr, 0, len(arr) - 1)
print(f"Sorted array = {arr}")




