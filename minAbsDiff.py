class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        a = []
        mindiff = max(arr)
        for i in range(0,len(arr)-1):
            if ((arr[i+1] - arr[i]) < mindiff):
                mindiff = arr[i+1] - arr[i]
                a.clear()
                a.append([arr[i],arr[i+1]])
            elif ((arr[i+1] - arr[i]) == mindiff):
                a.append([arr[i],arr[i+1]])
        return a