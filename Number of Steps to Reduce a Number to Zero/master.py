class Solution:
    def numberOfSteps(self, num: int) -> int:
        setps = 0
        while(num != 0):
            if(num % 2 == 0): num = num / 2
            else: num -= 1
            setps += 1
        return setps


test = Solution()

print(test.numberOfSteps(123))