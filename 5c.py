A = [[1,2,3],
    [4,5,6],
    [7,8,9]]
print("A = ")
for r in A:
   print(r)
B=[[10,11,12],[13,14,15],[16,17,18]]
C = [[0,0,0],[0,0,0],[0,0,0]]
print("B = ")
for r in B:
   print(r)
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j]+=(A[i][k]*B[k][j])
print("C = ")
for r in C:
   print(r)
