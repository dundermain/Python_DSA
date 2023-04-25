#OOPS concept in Python

class SoftwareEngineer:
    #created a clase

    alias = "Keyboard Magician"  #  This is a class attritbute. It can be accessed by both class and instance

    def __init__(self, name, age, level, salary):  #for every method in an instanse the first argument has to be self. This is initialisation
        self.name =  name
        self.age = age
        self.level = level 
        self.salary = salary   #all these are instance attributes and can only be accssed by instance not by class

    def code(self): #This is an instance method. A method is a function inside thre class and attribute is variable inside class
        print(f"{self.name} is writing a code")

    def code_in_language(self, langauge): #we can pass arguments in methods as well
        print(f"{self.name} is writing a code in {langauge}")


#some dunder methods available in Python

    def __str__(self):
        information = f"The name of the SE is {self.name}, age is {self.age}. {self.name} is working at level {self.level}"
        return information


se1 = SoftwareEngineer("Max", 20, "Junior", 5000)  #created an instance with their respecitve attributes as arguments



print(se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)
se1.code()
#print(SoftwareEngineer.age)  #this will give error "AttributeError: type object 'SoftwareEngineer' has no attribute 'age'"

print(se1) #This will call the __str__method and will print the information present there
