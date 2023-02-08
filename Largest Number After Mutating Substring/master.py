class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str: # O(n)
        """
            this function return the largest number insted of change list
            parameters:
                num: which represents a large integer
                chnage: 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit
            return: Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num. 
        """
        numbers = list(num) # convert numbers from string to list to can replace each item
        start_change = False # to detect substring
        for index in range(len(numbers)): 
            number = int(numbers[index]) # convert current number from str to int
            # if change[number] is greater than or equal current number change current number in numbers
            if change[number] > number:
                numbers[index] = str(change[number])

                # set start change to true
                if not start_change:
                    start_change = True
            # if change[number] is equal current number skip current iterate
            elif change[number] == number:
                continue
            # if start change of sequence true and current number is greater than change[number] leave iteration because this break our substring contiguous sequence
            elif start_change:
                break
        return "".join(numbers)

obj = Solution()
print(obj.maximumNumber("214010", [6,7,9,7,4,0,3,4,4,7]))