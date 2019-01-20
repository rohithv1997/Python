class Employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount+=1
    def displaycount(self):
        print("No. of Employees= ",Employee.empcount)
    def displayEmployee(self):
        print("Name: ",self.name,"\tSalary: ",self.salary)

emp1=Employee("Zara",2000)
emp2=Employee("Mark",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("No. of Employees= ",Employee.empcount)
