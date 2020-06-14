class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        mul = 1
        while (n > 0 ):
            digit = n % 10
            add = add + digit
            mul = mul * digit
            n = n // 10
        return mul - add
            