class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        J,S = list(J), list(S)
        for i in S:
            if i in J:
                count += 1
        return count