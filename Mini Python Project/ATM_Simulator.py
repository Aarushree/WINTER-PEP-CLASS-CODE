#ATM Simulator
file_name="atm_data.txt"
#balance is the a global variable that store money
balance=1000
#Pin is a global variablethat stores ATM pin 
pin="1234"
'''new code= 5678'''

#----------------------------------------------------Load data function------------------------------------------------------
def load_data():
    #global keyword allows us to modify outside variables
    global balance,pin
    try:
        #open a file  i read mode
        file=open(file_name,"r")
        #read all the lines from the file into a list
        lines=file.readlines()
        #close the file after reading
        file.close()
        #frist lines contains pin, strip removes \n
        pin=lines[0].strip()   #strip: it will remove the space from starting and ending 
        #second line contains balance
        balance=int(lines[1].strip())
    except:
        #if file does not exist or error occurs
        #pass mean 'Do Nothing'
        #program will use default balance and pin
        pass

#---------------------------------------------------------CHECK BALANCE------------------------------------------------------
def check_balance():
    print("your balance is :", balance)

#SAVE DATA
def save_data():
    #opening a file in write mode
    file=open(file_name,"w")
    #write a pin into the file and go to next line
    file.write(pin+"\n")
    #write Balance as string
    file.write(str(balance))
    #close the file
    file.close()

#--------------------------------------------------------DEPOSIT MONEY---------------------------------------------------------
def deposit_money():
    #global allows changing original balance 
    global balance
    try:
        amount=int(input("enter amount to desposit:"))
        balance=balance+amount
        #save updated balance yo the file
        save_data()
        print("money desposite successfully")
    except:
        print("please enter nnumber only")


#---------------------------------------------------------WITHDRAW Moeny------------------------------------------------------
def withdraw_money():
    global balance
    try:
        amount=int(input("enter amount  you want to withddraw: "))
        if(amount>balance):
            print("insufficient balance")
        else:
            balance=balance-amount
        save_data()
        print("please collect your cash")
    except:
        print("please enter nnumber only")

#------------------------------------------------------------CHANGE PIN---------------------------------------------------------
def change_pin():
    global pin
    #ask  user for old pin
    old_pin=input("enter thr old pin:")
    #check if old pin matches
    if old_pin==pin:
        #ask user for new pin
        new_pin=input("enter ur new pin")
        pin= new_pin
        save_data()
        print("pin change successfully")
    else:
        print("incorrect pin")

#---------------------------------------------------------Main Program-------------------------------------------------------
def main():
    #load data when program starts
    load_data()
    #now ask user to enter the pin
    user_pin=input("enter the pin:")
    #if pin is wrong stop the program
    if user_pin!=pin:
        print("Incorrect PIN")
        return
    while True:
        print("\n-------------------------------------ATM MENU---------------------------")
        print("1. Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Change pin")
        print("5.Exit")

        choice =input("enter ur choice")
        if choice =="1":
            check_balance()
        elif choice =="2":
            deposit_money()
        elif choice =="3":
            withdraw_money()
        elif choice=="4":
            change_pin()
        elif choice=="5":
            print("thank u for using ATM")
            break
        else:
            print("invalid choice")

main()



#========================================prject ends=========================================================================