class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i,b,arr,arr1,c = 0,[],[],[],[]
        if not strs:
            return ""
        for a in strs:
            b.append(len(a))
        l = min(b)
        for i in range(0,l):
            for a in strs:
                arr.append(a[i])
            arr1.append(arr)
            arr=[]
        for i in arr1:
            if (len(set(i)) == 1):
                c.append(i[0])
            if not c:
                return ""
        return "".join(c)
        