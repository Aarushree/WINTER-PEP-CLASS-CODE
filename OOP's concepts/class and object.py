# class Student:
#       #constructor is created
#     def __init__(self):
#         print("hi my constructor is created")
#         self.name="ARUSHREE"
# #    print("hii i am arushree")
    
# s1=Student()
# print(s1.name)

#syntax for paramater construstor
# class Student:
#    # name="neha"
#     def __init__(self, fullname, marks):
#         self.name = fullname  ''
#         '' #self.name and like these are attributes
#         self.score = marks

# s1 = Student("Arushree", 99)

# print(s1.name)
# print(s1.score)

#car model and color no in class
# class Car:
    
#     def __init__(self, model, color):
#         self.m=model
#         self.c=color
# s2=Car("HONDA-CITY","black")
# print(s2.m)
# print(s2.c)

# class Student:
   
#     college_name="LPU"
#     def __init__(self, fullname, marks):
#         self.name = fullname  #self.name and like these are attributes
#         self.score = marks

# s1 = Student("Arushree", 99)
# s2 = Student("Neha", 100)

# #these are object attribute
# print(s1.name)
# print(s2.name)
# #these are class attributessssssss
# print(s1.college_name)
# print(s2.college_name)

# print(Student.college_name)


#class car class attribute is car showroom and object attributes will be modelname and carprice

# class Car:
#     showroom_name="XYZ Cars"
#     def __init__(self, modelname, carprice):
#         self.name=modelname
#         self.price=carprice
# s1=Car("ALTO-800","200000")
# s2=Car("HONDA-CITY","500000")
# print(s1.name)
# print(s2.name)


# class Employee:
#     company_name="Infosys"
#     def __init__(self,emp_name,emp_salary)
        
#make a class student where totl_student a class attribute and after everycount the count is increasing
# class Student:
#     total_student=0
#     def __init__(self,name):
#         self.name=name
#         Student.total_student += 1
# s1=Student()
# s2=Student()


# class Student:
#     def __init__(self,name):
#            self.n=name
#     def hello(self):
#           print("welcome",self.n)
#           #static methods are only for class
#     @staticmethod
#     def college_name():
#           print("This is lpu")
          
# s1=Student("Arushree")
# s1.hello()
# s1.college_name()

#create a class student in which object attribute name and marks it has a normal method "display()" it has to print
#display()
# #it will print=(name,marks)
# class Student:
#       def __init__(self,name,marks):
#             self.n=name
#             self.m=marks
#       def display(self):
#             print("HII",self.n,"YOUR MARKS ARE:",self.m)
# s1=Student("Arushree",99)
# s1.display()

 
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def college_name():
        print("lpu")
s1 = Student("Arushree", 99)
print(s1.name)
print(s1.marks)
s1.college_name()


    
