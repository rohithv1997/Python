n=int(input("Enter a Number \t"))
a=0
b=n
sum=0
while n>0:
    a=n%10
    sum+=(a**3)
    n//=10

if(sum==b):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
