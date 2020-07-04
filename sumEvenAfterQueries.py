class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        tot = sum([i for i in A if i % 2 == 0])
        a = []
        for v,i in queries:
            if (A[i] % 2 == 0):
                tot -= A[i]
            A[i] += v
            if (A[i] % 2 == 0):
                tot += A[i]
            a.append(tot)
        return a