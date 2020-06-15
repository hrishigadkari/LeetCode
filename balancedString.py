class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s = list(s)
        r,l,count = 0,0,0
        for i in range(0, len(s)):
            if s[i] == 'R':
                r += 1
            if s[i] == 'L':
                l += 1
            if r == l:
                count += 1
        return count