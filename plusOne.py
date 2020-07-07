class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(0,n):
            if(digits[n-1-i] == 9):
                digits[n-1-i] = 0
                carry = 1
            else:
                digits[n-1-i] = digits[n-1-i] + 1
                return digits
            if (carry == 1):
            digits.append(carry)
            return digits[::-1]
    