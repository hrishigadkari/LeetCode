class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            a = int(str(x)[::-1])
#print (a) 
        if x <= 0:
            a = -1 * int(str(x*(-1))[::-1])
#print (a)
        if a >= 2**31 -1 and a <= 2**31:
            return 0
        else:
            return a