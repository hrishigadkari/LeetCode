class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = Counter(s)
        for i in range(0,len(s)):
            if (m[s[i]] == 1):
                return i
        return -1