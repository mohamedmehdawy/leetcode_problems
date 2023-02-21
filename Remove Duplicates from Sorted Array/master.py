class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        # area of valid numbers
        valid_area = len(nums) - 1
        
        # set i and j
        i = 0
        j = i + 1
        
        while i <= valid_area:
            j = i + 1
            while j <= valid_area:
                # if current element found in another place replace, swap another place in the end of valid area and decrace valid area by 1
                if nums[i] == nums[j]:
                    nums[j], nums[valid_area] = nums[valid_area], nums[j]
                    valid_area -= 1
                else:
                    j += 1
            i += 1
        
        # sort valid area
        slice_area = nums[:valid_area+1]
        slice_area.sort()
        
        for i in range(valid_area+1):
            nums[i] = slice_area[i]
        
        return valid_area + 1
        
obj = Solution()
print(obj.removeDuplicates([1,1,1]))