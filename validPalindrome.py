class Solution:
    def isPalindrome(self, s: str) -> bool:
        pOne = 0
        pTwo = len(s)- 1
        while pOne < pTwo:
            while pOne < pTwo and not s[pOne].isalnum():
                pOne += 1
            while pOne < pTwo and not s[pTwo].isalnum():
                pTwo -= 1
            while s[pOne].lower() != s[pTwo].lower():
                return False
            pOne += 1
            pTwo -= 1
        return True