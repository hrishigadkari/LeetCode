class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2)
        cnt = 0 
        for i in arr1:
            count = 0
            for j in arr2:
                if (abs(i-j) <= d):
                    count += 1
                    break
            print(count)        
            if (count > 0):
                cnt += 1
        return len(arr1)- cnt