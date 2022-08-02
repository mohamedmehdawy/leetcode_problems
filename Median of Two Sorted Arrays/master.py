import math
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        lenght = len(arr)
        mid = math.floor(lenght / 2)
        if(lenght % 2 == 0):
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return arr[mid]
        
t = Solution()
print(t.findMedianSortedArrays([1,2], [3,4]))