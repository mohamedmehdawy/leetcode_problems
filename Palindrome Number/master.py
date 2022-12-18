class Solution:
    def reverse(self, number: int):
        """
            this function reverse number
            parameters:
                number: the number should be reverse
            return: reversed number
        """
        result = 0        
        while number > 0:
            result = (result * 10) + (number % 10)
            number //= 10
        return result
    
    def isPalindrome(self, x: int) -> bool:
        # handel negitave numbers
        if x < 0:
            return False
        
        
        reversed_number = self.reverse(x)
        
        try:
            
            if x / reversed_number == 1:
                return True
            else:
                return False
        except:
            return True
        

x = Solution()


print(x.isPalindrome(0))

