class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = Counter(t) - Counter(s)
        for key in a.keys():
            return key