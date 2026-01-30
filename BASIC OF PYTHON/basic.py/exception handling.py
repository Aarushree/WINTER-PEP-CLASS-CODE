# try:
#     c=int(input("enter the number:"))
#     print(10/c)
# except ZeroDivisionError:
#     print("you cannot divide by zero")
# except ValueError:
#     print("enter the only number")

# try:
#     c=int(input("enter the number:"))
#     print(10/c)
# except:
#     print("error occured")
# else:
#     print("no error, program run successfully")
     
#finally
# try:
#     f=open("movies.txt")
# except:
#     print("the file not found error")
# finally:
#     print("program finished")

# age=int(input("enter the age:"))
# if age<18:
#     raise ValueError("age must be 18 or above for vote")
# print("you can vote")

#CUSTOM ERROR

# class LowBalanceError(Exception):
#     #This line create a custom exception named LowBalanceError
#     #pass is used because class cannnot br empty in python
#     #we dont need to add anylogic inside the class right now
#     pass

# balance = 500
# withdraw = int(input("enter amount:"))
# if withdraw>balance:
#     raise LowBalanceError("Insufficient balance")
# print("withdraw successfull")


'''===================================================================================================================================='''

# try:
#     num=int(input("enter a number:"))
#     print(100/num)
# except:
#     print("error")

# try:
#     try:
#         print(1/0)
#     finally:
#         print("inner finally")
# except ZeroDivisionError:
#     print("outer exception")
# finally:
#     print("order finally")


# def test():
#     try:
#         return 10
#     finally:
#         return 20
# print(test())

# try:
#     try:
#         x=int("abc")
#     except ValueError:
#         print("inner handled")
#         raise
# except Exception:
#     print("outer handled")

# def test():
#     try:
#         return 10
#     except:
#         return 20
#     else:
#         return 30
# print(test())

# age=int(input("enter ur age:"))
# if age<18:
#     raise ValueError("age must be 18 or more")
# print("you are eligible")

'''take number input from user'''
num=int(input("enter ur number:"))
#id  number is negative, we manually raise an error
#python does npt automatically treat negative number aas wrong 
if num<0:
    raise ValueError("number must be positive")
#this will runs if no exception occur
print('you entered:',num)