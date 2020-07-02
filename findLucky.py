class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a =[]
        for key,value in Counter(arr).items():
            print(key,value)
            if (key == value):
                a.append(key)
        if len(a) == 0:
            return -1
        return max(a)