class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        while i < len(s):
            doubleStatue = False
            if i+1 < len(s):
                if s[i] == "I":
                    if s[i+1] == "V" or s[i+1] == "X":
                        doubleStatue = True

                elif s[i] == "X":
                    if s[i+1] == "L" or s[i+1] == "C":
                        doubleStatue = True

                elif s[i] == "C":
                    if s[i+1] == "D" or s[i+1] == "M":
                        doubleStatue = True
            if doubleStatue:
                result += symbols[s[i+1]] - symbols[s[i]] 
                i += 2
            else:
                result += symbols[s[i]]
                i += 1
        return result