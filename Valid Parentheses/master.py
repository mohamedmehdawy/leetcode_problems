class Solution:
    def __init__(self):
        self.left = ['(', '{', '[']
        self.right = [')', '}', ']']
    def getPos(self, side, value): # O(n)
        """
            this function return position of target in side
            -- why not return index?
            - because 0 work as False so we need return position not index
            parametrs:
                side: left or right
                value: should be search
            return: boolean value
        """
        try:
            return side.index(value) + 1
        except:
            return False
    def isValid(self, s: str) -> bool: # O(n^2)
        size = len(s)
        # length of s is odd return false
        if size % 2 != 0:
            return False
        
        else:
            i = 0
            last_index = None # last index for controle range
            while i <= size - 2:
                open_pos = self.getPos(self.left, s[i])
                if open_pos:
                    if self.getPos(self.left, s[i]) == self.getPos(self.right, s[i+1]):
                        if i + 2 == last_index:
                            i += 3
                        else:
                            i += 2
                    elif self.getPos(self.left, s[i]) == self.getPos(self.right, s[size - 1 - i]):
                        i += 1
                    elif i != 0:
                        count = 1
                        is_valid = False
                        for j in range(i+1, size): # check if paranthe is valid
                            if s[i] == s[j]:
                                count += 1
                            elif self.getPos(self.left, s[i]) == self.getPos(self.right, s[j]):
                                if count == 1:
                                    is_valid = True
                                    last_index = j
                                    break
                                else:
                                    count -= 1
                        if is_valid:
                            i += 1
                        else:
                            return False
                    else:
                        return False
                else: 
                    return False
            return True
        
obj = Solution()

# print(obj.isValid('()'))
# print(obj.isValid('}{'))
print(obj.isValid('[{()}]'))