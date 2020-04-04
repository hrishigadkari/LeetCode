class Solution:
    def isHappy(self, n: int) -> bool:
        add = 0
        num = [int(x) for x in str(n)]
        #print(num)
        n = len(num)
        for i in range(0,n):
            add = add + num[i]**2
        #print(add)
        if add == 1 or add == 7:
            return True
        if add < 10:
            return False
        if add != 1:
            return self.isHappy(add)
        