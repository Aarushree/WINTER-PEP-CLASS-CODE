#file=open("data.txt","mode->r,w,a")
# file=open("student.txt","w")
# file.write("Name:Rahul\n")
# file.write("Course: Python \n")
# file.close()

# file=open("student.txt","r")
# data=file.read()
# print(data)
# file.close()
'''second way of reading a file
 with open("student.txt","r")as file:
    data = file.read()
    print(data)'''

# file=open("student.txt","a")
# file.write("marks:90\n")
# file.close()
# file=open("student.txt","r")
# data=file.readline()
# print(data)
# data2=file.readlines()
# print(data2)




# file=open("data.txt","w")
# file.write("Name:Arushree\n")
# file.close()
file=open("data.txt","a")
file.write("color:red\n")
file.close()


