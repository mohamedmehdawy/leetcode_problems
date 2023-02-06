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
    def isValid(self, s: str) -> bool: # O(n)
        if len(s) % 2 != 0:
            return False
        else:
            # create stack to store paranthese in it
            stack = []
            
            for char in s:
                if self.getPos(self.left, char): # if current char in left side append it to stack
                    stack.append(char)
                elif len(stack) and self.getPos(self.right, char) == self.getPos(self.left, stack[-1]): # if current char in right side and the last element in stack is the open of it remove last element from stack and the stack not empty
                    stack.pop()
                else:
                    return False
            # return true if stack is empty
            if not len(stack):
                return True
            else:
                return False
        
obj = Solution()

# print(obj.isValid('()'))
print(obj.isValid('}{'))
print(obj.isValid('[{}{}{}{}{}(([[]]))]'))