class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # init the nums_map
        nums_map = {}
        
        # loop through the numbers
        for number in nums:
            # if the number found in dictionary, return true
            if number in nums_map:
                return True
            
            # if not found append the number to the map
            nums_map[number] = True
        
        # if no number found twice, return False
        return False