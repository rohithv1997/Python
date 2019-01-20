def add(x,y):
     return x+y
def diff(x,y):
      return x-y
def pro(x,y):
     return x*y
def div(x,y):
     return x/y
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
ch=input("Enter choice ")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if ch=='1':
   print("Sum= ",add(a,b))
elif ch=='2':
   print("Difference= ",diff(a,b))
elif ch=='3':
   print("Product= ",pro(a,b))
elif ch=='4':
   print("Quotient= ",div(a,b))
else:
   print("Error")
