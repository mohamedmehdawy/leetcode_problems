class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = -1

        for row in accounts:
            counter = 0
            for value in row:
                counter += value
            
            if counter > max_wealth: max_wealth = counter
        return max_wealth