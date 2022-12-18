class Solution:
    def rotate_right(self, nums):
        current = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            nums[i + 1] = nums[i]
        nums[0] = current
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k % len(nums)):
            self.rotate_right(nums)
