from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        tot = 0
        cnt = Counter(chars)
        for word in words:
            w = Counter(word)
            a = True
            for letter in w:
                if (letter not in cnt or cnt[letter] < w[letter]):
                    a = False
                    break
            if a:
                tot += len(word)
        return tot