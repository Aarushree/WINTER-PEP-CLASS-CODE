'''===================================ABSTRACTION====================================================='''

#abrstract class:
# class Parent:
#     def work(self):
#         pass

# class child(Parent):
#     def work(self):
#         print("i am working")

# class Payment:
#     def pay(self,amount):
#         pass
# class UPI(Payment):
#     def pay(self, amount):
#         print("Paid using UPI:",amount)

# class Card(Payment):
#     def pay(self, amount):
#         print("Paid using card:",amount)

# class Cash(Payment):
#     def pay(self, amount):
#         print("Paid using cash:",amount)

# obj=UPI()
# obj=Card()
# odj=Cash()
# obj.pay(12)


# class Shape():
#     def tell(self,konsa):
#         pass
# class Circle(Shape):
#     def tell(self,konsa):
#         print("this a circle!",konsa)

# class Rectangle(Shape):
#     def tell(self,konsa):
#         print("this is a rectangle!",konsa)
# ohj=Circle()
# ohj=Rectangle()
# ohj.tell("you got it")


# class Payment:
#     def start(self):
#         print("payment started")
#         def work(self):
#             pass
        
# class UPI(Payment):
#     def pay(self, amount):
#         print("Paid using UPI:",amount)

# class Card(Payment):
#     def pay(self, amount):
#         print("Paid using card:",amount)

# obj1=UPI()
# obj1.start()
# obj1.pay(100)


# obj1=Card()
# obj1.start()
# obj1.pay(150)


class Course:
    def cousre_info(self):
      print("this is a programming subject")
      
    def duration(self):
        pass

class ExamInterface:
    def exam_type(self):
        pass

class Python(Course,ExamInterface):
    def duration(self):
        print("course duration is 3 months")
    def exam_type(self):
        print("this is a practical based")
c=Python()
c.cousre_info()
c.duration()
c.exam_type()


