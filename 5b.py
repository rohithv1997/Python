A = [[200,190,180],
    [170,160,150],
    [140,130,120]]
B = [[1,2,3],
    [4,5,6],
    [7,8,9]]

print("A = ")
for r in A:
   print(r)
print("B = ")
for r in B:
   print(r)
C = [[A[i][j] - B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
print("Difference= ")
for r in C:
   print(r)
