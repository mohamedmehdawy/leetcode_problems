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
    def isValid(self, s: str) -> bool: # O(2^n)
        size = len(s)
        # length of s is odd return false
        if size % 2 != 0:
            return False
        
        else:
            i = 0
            expected = size // 2 # the expected number of paranthes
            while i <= size - 2:
                open_pos = self.getPos(self.left, s[i])
                if open_pos:
                    
                    if self.getPos(self.left, s[i]) == self.getPos(self.right, s[i+1]):
                        i = i + 2
                        expected -= 1

                    else:
                        count = 1
                        is_valid = False
                        scope = {
                        "start": -1,
                        "end": -1
                    }
                        for j in range(i+1, size): # check if paranthe is valid
                            if s[i] == s[j]:
                                count += 1
                            elif self.getPos(self.left, s[i]) == self.getPos(self.right, s[j]):
                                if count == 1:
                                    is_valid = True
                                    expected -= 1
                                    scope['start'] = i
                                    scope['end'] = j
                                    break
                                else:
                                    count -= 1
                        if is_valid:
                            status = self.isValid(s[scope['start']+1:scope['end']])
                            if status:
                                i = scope['end'] + 1
                            else:
                                return False
                        else:
                            return False
                    
                    # check if expected number of paranthes end
                    if expected == 0:
                        return True
                else: 
                    return False
            return True
        
obj = Solution()

# print(obj.isValid('()'))
print(obj.isValid('}{'))
print(obj.isValid('[{}{}{}{}{}(([[]]))]'))