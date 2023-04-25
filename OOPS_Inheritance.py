# OOPS Inheritance concepts

#Inheritance is a method where once class(child class) uses attritbues and methods of another class(Parent Class). 

class Employee:   #parent class. Child can inh

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):  #This is parent or base method
        print(f"{self.name} is working.")
    

class SoftwareEngineer(Employee):  #child class. It will use some attributes of Employee parent class
    def __init__(self, name, age, level, salary):
        super().__init__(name, age)     #we dont need to call self.name again here as it is present in our parent class. super() means super class or parent class
        self.level = level
        self.salary = salary


class Designer(Employee):
    pass


se = SoftwareEngineer("Max", 25)
se.work()   #example of inheritance where the child class inherited the parent class methods

d = Designer("Philip", 27)