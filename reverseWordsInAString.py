class Solution:
    def reverseWords(self, s: str) -> str:
        b = ' '.join(reversed(s.split()))
        return b

        