import statistics
A=[1,2,3,4,5,6,7,8,9,10]

print("A= ")
for r in A:
    print(r)
print("Mean= ")
print(statistics.mean(A))
print("Variance= ")
print(statistics.pvariance(A))
print("Standard Deviation= ")
print(statistics.pstdev(A))

