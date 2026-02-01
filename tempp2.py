'''try:
    #risky code
except:
    #error handling code'''

#basic code 
'''try:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    print(a/b)
except:
    print("error occurred!!!!!!!!!!!!!!!!!!!")'''

try:
    file=open("movies.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file not found")
finally:
    print("program ends")
