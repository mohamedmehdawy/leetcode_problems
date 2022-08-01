class Solution:
    def __init__(self):
        self.max_sub = {
            "sub": "",
            "length": 0
        }
        self.current = ""
    def setMaxSub(self) -> None:
        self.max_sub["sub"] = self.current
        self.max_sub["length"] = len(self.current)
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            self.current = s[i]
            if len(self.current) > self.max_sub["length"]:
                self.setMaxSub()
            for j in range(i + 1, len(s)):
                if s[j] not in self.current:
                    self.current += s[j]
                    
                else:
                    if len(self.current) > self.max_sub["length"]:
                        self.setMaxSub()
                    break
                if len(self.current) > self.max_sub["length"]:
                    self.setMaxSub()


        return self.max_sub["length"]
        
        
obj = Solution()
print(obj.lengthOfLongestSubstring("dvdf"))