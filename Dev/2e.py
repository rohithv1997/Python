n=int(input("Enter the Limit \t"))
a=-1
b=1
c=0
print("Fibonacci Series = ")
while c<=n:
    c=a+b
    print(c," ")
    a=b
    b=c
    
