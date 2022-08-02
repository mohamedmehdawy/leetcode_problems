class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        current = ""
        for i in range(len(s)):
            current = s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in current:
                    current += s[j]
                else:
                    break
            if len(current) > max:
                max = len(current)           
        return max
        
        
obj = Solution()
print(obj.lengthOfLongestSubstring("dvdf"))