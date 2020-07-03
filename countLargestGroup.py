class Solution:
    def sum_of_digit(self,a): 
        if a == 0:
            return 0
        return (a % 10 + self.sum_of_digit(int(a / 10)))
    
    def countLargestGroup(self, n: int) -> int:
        a,dic,v = [],{},{}      
        for i in range(1,n+1):
            a.append(self.sum_of_digit(i))
            dic[i] = a[i-1]
        for key, value in sorted(dic.items()):
            v.setdefault(value, []).append(key)
        print(v)
        maxi = 0
        for i in v.values():
            maxi = max(maxi,len(i))
        return len([i for i in v.values() if len(i)==maxi])
        