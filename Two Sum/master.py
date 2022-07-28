class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        results = [0, 0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    results[0] = i
                    results[1] = j
                    return results
        return results        


test = Solution()

print(test.twoSum([2,7,11,15], 9))