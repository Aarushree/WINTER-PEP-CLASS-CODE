# class Address:
#     def __init__(self,city):
#         self.city=city
#     def show_address(self):
#         print("city:",self.city)

# #student class
# class Student:
#     def __init__(self,name,city):
#         self.name=name
#         #composition:
#         #creating object of address class inside student class
#         self.address= Address(city)
#     def show_student(self):
#         print("Name:",self.name)
#         #using object of another class
#         self.address.show_address()
# s=Student("karan","delhi")
# s.show_student()



class Engine:
    def start(self):
        print("engine started!")
class Car:
    def __init__(self):
        self.engine=Engine()
    def drive(self):
        self.engine.start()
        print("car is moving")
obj=Car()
obj.drive()


#create a teacher and subject classes where teacher HAS-A subject
#HAS-A relationship is a composition
#Design a console based "Employee Payroll system" using oops python
#the ssystem should calculate salary for different type of employess using all oops concepts
#employee - Abstract class
#full time employee - child class
#part time employee - child class
#salary - encapsulated Data 
#payroll system- controller(HAS-A)
#OUTPUT-
#employee Created
#salary:50000
#employee Created
#salary:4000


