class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        current_magazine = magazine
        for char in ransomNote:
            current_index = current_magazine.find(char)
            if(current_index == -1):
                return False
            else:
                current_magazine = current_magazine[:current_index] + current_magazine[current_index+1:]
        return True

