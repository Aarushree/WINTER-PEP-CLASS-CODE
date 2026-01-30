# Ques1:
# take input print its type and then print double of it(DataType)
'''num=int(input("enter the value"))
print(type(num))
num=int(num)
print(num*2)'''

# Ques2:
#     Take input salary as string then convert it to the integer amd add bonus 5000 and print(Type Conversion)
'''salary = input("Enter your salary: ")
salary_int = int(salary)
total_salary = salary_int + 5000
print("Salary after adding bonus:", total_salary)'''

# Ques3:
#       print Hot if temp>=30(if-else)
#       normal temp>=15 else cold
'''temp=int(input("enter the temp:"))
if(temp>=30):
    print("The temp is Hot")
elif(temp>=15):
    print("The temp is Normal")
else:
    print("The temp is cold")'''

# Ques4:
#     print table of 7 and also count how many number are printed(for loop)
#num=int(input("enter the num:"))
'''count=0
print("the table of 7 is :")
for i in range(1,11):
        print(7*i)
        count += 1
print("Total numbers printed:", count)'''

# Ques5:
#     Take a number and reverse it(while loop)
'''n=int(input("enter the no: "))
rev=0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print(rev)'''
# Ques6:
#     check even odd using functions
'''n=int(input("enter the num:"))
if(n%2==0):
    print("the num is even")
else:
    print("the num is odd")'''


# Ques7:
#     create a lambda function to return a cube of a number'''

n=int(input("enter the num:"))
cube = lambda x: x ** 3
print(cube(n))