A = [[1,2,3],[4,5,6],[7,8,9]]
print("A= ")
for r in A:
   print(r)
B = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print("A' = ")
for r in B:
   print(r)
