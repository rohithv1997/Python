class student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print("Name: ",self.name,"\tAge: ",self.age,"\tGender: ",self.gender)

emp1=student("Zara",12,"Female")
emp1.display()
emp2=student("Mark",8,"Male")
emp2.display()
