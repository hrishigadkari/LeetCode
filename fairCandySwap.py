A = [21,89,90,88,54,45,67,41,57,7]
B = [55,57,22,19,44,91,100,71,33,33]
diff = (sum(A) - sum(B))/2
print(diff)
for i in A:
    for j in B:
        #print(i,j)
        if i-j == diff or j-i == diff:
            print(i,j)
            print(i-j, j-1)