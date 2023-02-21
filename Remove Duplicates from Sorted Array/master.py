class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # set valid area to 1 beacause we have at least 1 valid number
        valid_area = 1
        for i in range(1, len(nums)):
            # if we found number not eqaul last number in valid area, put this number in the last of our valid area and increase it by one
            if nums[valid_area - 1] != nums[i]:
                nums[valid_area] = nums[i]
                valid_area += 1
        return valid_area        
obj = Solution()
print(obj.removeDuplicates([1,1,1, 2, 2, 2, 3, 4,4]))