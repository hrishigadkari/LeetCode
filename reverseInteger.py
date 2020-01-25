class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            a = int(str(x)[::-1])
#print (a) 
        if x <= 0:
            a = -1 * int(str(x*(-1))[::-1])
#print (a)
        r = range(-2**31-1, 2**31)    
        if a in r:
            return a
        else:
            return 0