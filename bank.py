#####################################################################################
###       ______   __       __        _______    ______   __    __  __    __      ###
###      /      \ /  \     /  |      /       \  /      \ /  \  /  |/  |  /  |     ###
###     /$$$$$$  |$$  \   /$$ |      $$$$$$$  |/$$$$$$  |$$  \ $$ |$$ | /$$/      ###
###     $$ |__$$ |$$$  \ /$$$ |      $$ |__$$ |$$ |__$$ |$$$  \$$ |$$ |/$$/       ###
###     $$    $$ |$$$$  /$$$$ |      $$    $$< $$    $$ |$$$$  $$ |$$  $$<        ###
###     $$$$$$$$ |$$ $$ $$/$$ |      $$$$$$$  |$$$$$$$$ |$$ $$ $$ |$$$$$  \       ###
###     $$ |  $$ |$$ |$$$/ $$ |      $$ |__$$ |$$ |  $$ |$$ |$$$$ |$$ |$$  \      ###
###     $$ |  $$ |$$ | $/  $$ |      $$    $$/ $$ |  $$ |$$ | $$$ |$$ | $$  |     ###
###     $$/   $$/ $$/      $$/       $$$$$$$/  $$/   $$/ $$/   $$/ $$/   $$/      ###
###                                                                               ###
#####################################################################################
###                                                                               ###
###                                                                               ###
###                               Student Number                                  ###
###                                  C20402732                                    ###
###                                                                               ###
###                                                                               ###
###                                    Name                                       ###
###                              Aleksey Makarevich                               ###
###                                                                               ###
###                                                                               ###
#####################################################################################
#Importing all my necessary modules
import sys
import csv
from datetime import date, datetime

class Customer:

    #Intialising all necessary user information for the program to run
    def __init__(self, age, id):
        self.age = age
        self.id = id

    # A Login method which then also reads the users information into the class
    def Login(self, Username, Password):
        #opens the customers text file for reading
        file = open("customers.txt","r")
        found = False
         
        #Reading each line of the file
        for line in file:
            #Splitting each line of the file into an array
            details = line.split(",")
            fixed = []
            #Stripping the array of any new line instances
            #Cleans the information of any new line arguments
            for element in details:
                fixed.append(element.strip())
            #Checks each line to see if the information matches
            if Username == fixed[2] and Password == fixed[3]:
                #If a suitable login is found, updates the found variable
                found = True
                break #This will leave the for loop if a match is found
        #If a match is found it allow sthe user to login and continue
        if found == True:
            print("Login successful!")
            #Inserts all the necessary information into the classes
            user.id = fixed[4]
            user.age = int(fixed[5])
            account.id = fixed[4]
            account.Initialise()
            MainMenu()
        else:
            print("Login Failed")
            #Sending the user back to the welcome screen
            Welcome()

    #A method to display all users in the system, so users can choose who to send money to
    def DisplayUsers(self):
        #opens the customers text file for reading and writing
        file = open("customers.txt","r+")
        #prints out the top of the able
        print(f"|Firstname\t\t|Surname\t\t|ID")
        print("____________________________________________________")
        for line in file:
            details = line.split(",")
            fixed = []
            #Cleans the information of any new line arguments
            for element in details:
                fixed.append(element.strip())
            #Checks each line to see if the information matches
            #Prints the user information in a nice looking table
            print(f"|{fixed[0]}    \t\t|{fixed[1]}   \t\t|{fixed[4]}")
        Transfer()

    #def __str__(self):
    #    return f'ID = {self.id} Age = {self.age}'

class Account(Customer):

    #Method for initiating the class variables
    def __init__(self, age, id, check, save, checkbal, savebal):
            self.check = check
            self.save = save
            self.checkbal = checkbal
            self.savebal = savebal
            super().__init__(age, id)

    #This method loads in all the necessary information into the account class
    def Initialise(self):
        print("\nAccount initialised.\n")
        file = open("accounts.txt","r+")
        
        for line in file:
            details = line.split(",")
            fixed = []
            #Cleans the information of any new line arguments
            for element in details:
                fixed.append(element.strip())
            #Checks each line to see if the information matches
            if self.id == fixed[0]:
                self.check = int(fixed[1])
                self.save = int(fixed[2])
                self.checkbal = int(fixed[3])
                self.savebal = int(fixed[4])
                self.lastdate = fixed[5]
                print(self.lastdate)
                break #This will leave the for loop if a match is found

    #This method creates a new Checking account
    def CreateCheck(self):
        #If checking account is set to 1, then they already have an account and wont be able to open a new one
        if self.check == 1:
            print("\nYou already have a Checking Account.")
        #Since you have to be over 18 to open a checking account, their age is stored in case they are too young
        elif user.age < 18:
            print("You are too young to create a checking account.")
        #If both are successful, self.check is set to 1 which will update the accounts page to say they have an account
        else:
            self.check = 1
            print("\nAccount made!")
            
    #This method creates a new Savings account
    def CreateSave(self):
        #If savings account is set to 1, then they already have an account and wont be able to open a new one
        if self.save == 1:
            print("\nYou already have a Savings Account.")

        
        else:
            #Sets save to 1, meaning the user now has a savings account
            self.save = 1
            print("\nAccount made!")

    #This method deletes a checking account
    def DeleteCheck(self):
        #If checking account is set to 0, then they dont have an account and wont be able to delete it
        if self.check == 0:
            print("\nYou do not have a checking account.")
            Delete()
        
        #Checks if the checking account has any money, or in debt, balance must be at 0 in order to delete
        elif self.checkbal != 0:
            print("\nYour checking account must be empty before deleting it.")
            Delete()

        #Sets check to 0, meaning they no longer have a checking account   
        else:
            self.check = 0
            print("\nAccount deleted!")
            Delete()

    #This method deletes a checking account
    def DeleteSave(self):
        #If checking account is set to 0, then they dont have an account and wont be able to delete it
        if self.save == 0:
            print("\nYou do not have a savings account.")
            Delete()
        
        #If the savings account is not empty, they cannot delete it
        elif self.savebal != 0:
            print("\nYour savings account must be empty before deleting it.")
            Delete()

        #Sets save to 0, meaning they no longer have a savings account
        else:
            self.save = 0
            print("\nAccount deleted!")
            Delete()
    
    #This method exports the new updated info to the accounts text file
    def Export(self, date):
        #Saves all lines of the old file
        with open("accounts.txt","r") as myfile:
            lines = myfile.readlines()

            #Prints all lines to a new accounts file, without the line including the id of the current user
            with open("accounts.txt","w") as myfile:
                for line in lines:
                    if line.find(self.id) == -1:
                        myfile.write(line)
        
        #Writes out the users new information, as a new line at the bottom of the file
        with open("accounts.txt","a",newline="") as myfile:
                writer = csv.writer(myfile)
                writer.writerow([self.id, self.check, self.save, self.checkbal, self.savebal, date])
                myfile.close()

    #This method is used to view the transactions of the current user set in a nice table
    def ViewTrans(self):
        file = open("accountTransactions.txt","r+")
        print(f"|Account \t\t|Amount\t\t|Total\t\t|Date")
        print("__________________________________________________________________")
        for line in file:
            details = line.split(",")
            fixed = []
            #Cleans the information of any new line arguments
            for element in details:
                fixed.append(element.strip())
            #Checks each line to see if the information matches
            if self.id == fixed[0]:
                print(f"|{fixed[1]}\t\t|{fixed[2]}\t\t|{fixed[3]}\t\t|{fixed[4]}")
        TransBal()

    #The string method will allow the balance of the user to print out and is used in the balance section of the menu
    def __str__(self):
        return f'You have {account.savebal} Euro saved up and {account.checkbal} in your checking account.'

class SavingAccount(Account):

    #Method for initiating the class variables
    def __init__(self, amount):
        self.amount = amount

    #Method to deposit money in savings account
    def Deposit(self, amount):
        #Checks if the user is attemping to deposit a negative value
        if amount <= 0:
            print("You can only deposit a positive value")
            Deposit()
        
        #If its a valid input, the balance is updated and sent to transactions
        else:
            int(amount)
            account.savebal = account.savebal + amount
            print("Money Successfully lodged into account.")
            saving.Transactions(account.id, "Savings ", amount)
            Deposit()

    #Method to withdraw money from savings account
    def Withdraw(self, amount):
        #Checks if they are trying to withdraw a postive amount
        if amount <= 0:
            print("You can only withdraw a positive value")
            Withdraw()

        #Checks if they are trying to withdraw more than their balance
        elif amount > account.savebal:
            print("You cannot withdraw more money than there is in your account.")
            Withdraw()

        #If successful, withdraws the money from their account
        else:
            int(amount)
            account.savebal = account.savebal - amount
            print("Money Withdrawn from account.")
            saving.Transactions(account.id, "Savings ", -amount)
            account.lastdate = str(date.today())
            Withdraw()
            
    #Method to write to transactions with any information needed for that transactions
    def Transactions(self, id, type, amount):
        with open('accountTransactions.txt', 'r') as f:
            last_line = f.readlines()[-1]
        details = last_line.split(",")
        register = []
        for element in details:
            register.append(element.strip())
        register[5] = int(register[5])
        NewID = register[5] + 1

        with open("accountTransactions.txt","a",newline="") as myfile:
                writer = csv.writer(myfile)
                writer.writerow([id, type, amount, account.savebal ,date.today(), NewID])
                myfile.close()


class CheckingAccount(Account):

	#Method for initiating the class variables
    def __init__(self, amount):
        self.amount = amount

    #Method to deposit money in checking account
    def Deposit(self, amount):

        #Checks if the user is attemping to deposit a negative value
        if amount <= 0:
            print("You can only deposit a positive value")
            Deposit()

        #If its a valid input, the balance is updated and sent to transactions
        else:
            account.checkbal = account.checkbal + amount
            checking.Transactions(account.id, "Checking", amount, account.checkbal)
            print("Money Successfully lodged into account.")
            Deposit()

    #Method to withdraw money from checking account
    def Withdraw(self, amount, location):
        #Checks if they are trying to withdraw a postive amount
        if amount <= 0:
            print("You can only withdraw a positive value")

            #If statement incase they are withdrawing from the transactions method
            if location == 0:
                Withdraw()
            else:
                Transfer()

        #Checks if they are trying to withdraw more than their credit allowance
        elif (account.checkbal - amount) < -500:
            print("You cannot be more than 500 euro in debt.")
            #If statement incase they are withdrawing from the transactions method
            if location == 0:
                Withdraw()
            else:
                Transfer()

        #If successful, withdraws the money from their account
        else:
            account.checkbal = account.checkbal - amount
            print("Money Withdrawn from account.")
            checking.Transactions(account.id, "Checking", -amount, account.checkbal)
            if location == 0:
                Withdraw()

    #Method to transfer money between accounts
    def Transfer(self, id, amount, type):
        #Reading the accounts text file to see if the person they are sending money to actually has that type of account.
        file = open("accounts.txt","r")
        found = False
        
        for line in file:
            details = line.split(",")
            fixed = []
            #Cleans the information of any new line arguments
            for element in details:
                fixed.append(element.strip())
            if type == "0":
                if id == fixed[0]:
                    if fixed[2] == "1":
                        found = True
                        break #This will leave the for loop if a match is found
                    else:
                        print("User does not have the specified account type.")
                        Transfer()
            else:
                if id == fixed[0]:
                    if fixed[1] == "1":
                        found = True
                        break #This will leave the for loop if a match is found
                    else:
                        print("User does not have the specified account type.")
                        Transfer()
        #This only runs if the target has that account
        if found == True:
            #Withdraws the ammount of money, and if the withdrawl fails it sends them back to the trasnfer screen
            checking.Withdraw(amount, 1)

            print("Transfer Successful")

            #This if tree is used to print out to transactions
            if type == "0":
                uptamount = int(fixed[4]) + amount
                checking.Transactions(id, "Savings", amount, uptamount)
            else:
                uptamount = int(fixed[3]) + amount
                checking.Transactions(id, "Checking", amount, uptamount)

            #Opens accounts file in order to write out the new updates trasnferred money
            with open("accounts.txt","r") as myfile:
                lines = myfile.readlines()

            with open("accounts.txt","w") as myfile:
                for line in lines:
                    if line.find(fixed[0]) == -1:
                        myfile.write(line)
        

            with open("accounts.txt","a",newline="") as myfile:
                    writer = csv.writer(myfile)
                    if type == "0":
                        writer.writerow([fixed[0], fixed[1], fixed[2], fixed[3], uptamount, fixed[5]])
                    else:
                        writer.writerow([fixed[0], fixed[1], fixed[2], uptamount, fixed[4], fixed[5]])
                        myfile.close()
            Transfer()
        else:
            #If they enter an invalid user ID
            print("User ID does not exist")
            Transfer()

    #Method to write to transactions with any information needed for that transactions
    def Transactions(self, id, type, amount, balance):

        with open('accountTransactions.txt', 'r') as f:
            last_line = f.readlines()[-1]
        details = last_line.split(",")
        register = []
        for element in details:
            register.append(element.strip())
        register[5] = int(register[5])
        NewID = register[5] + 1

        with open("accountTransactions.txt","a",newline="") as myfile:
                writer = csv.writer(myfile)
                writer.writerow([id, type, amount, balance, date.today(), NewID])
                myfile.close()
	

#Initiating the classes to be able to use them globally
user = Customer(0, 0)
account = Account(0, 0, 0, 0, 0, 0)
checking = CheckingAccount(0)
saving = SavingAccount(0)

#Welcome screen for user to login, register or exit program
def Welcome():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\tWelcome to the AM Bank, please select one of the following options.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. Login.\n\
            \r2. Register.\n\
            \r3. End Program.\n')

    
    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        Login()
    elif choice == "2":
        Register()
    elif choice == "3":
        print("\nGoodbye")
        #sys.exit calls to end the program
        sys.exit
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        #Sending the user back to the welcome screen
        Welcome()

def Login():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\t\tPlease Enter your user details.\n\
            \r------------------------------------------------------------------------------------\n')
    #Username and password input which is sent to login method
    Username = input("Enter Username:")
    Password = input("Enter Password:")
    user.Login(Username, Password)
    
def MainMenu():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\tWelcome to the main menu, please select one of the following options.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. Create a new account.\n\
            \r2. Account transactions and Balance.\n\
            \r3. Deposit/Withdraw or Transfer Money.\n\
            \r4. Delete an account.\n\
            \r5. Log out.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        Create()
    elif choice == "2":
        TransBal()
    elif choice == "3":
        DepTran()
    elif choice == "4":
        Delete()
    elif choice == "5":
        print("\nGoodbye")
        #Sending the user back to the welcome screen
        Welcome()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        MainMenu()

def Create():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\tPlease select type of account you would like to open.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. Checking Account.\n\
            \r2. Savings Account.\n\
            \r3. Back.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        account.CreateCheck()
        Create()
    elif choice == "2":
        account.CreateSave()
        Create()
    elif choice == "3":
        account.Export(account.lastdate)
        MainMenu()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        Create()

def TransBal():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\t\tPlease select what you would like to do.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. View Transactions.\n\
            \r2. View Balance.\n\
            \r3. Back.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        account.ViewTrans()
    elif choice == "2":
        #The __str__ in the class accounts returns the users balance for both accounts
        print(account)
        TransBal()
    elif choice == "3":
        MainMenu()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        TransBal()

def DepTran():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\t\tPlease select what you would like to do.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. Deposit Money.\n\
            \r2. Withdraw Money.\n\
            \r3. Transfer Money.\n\
            \r4. Back.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        Deposit()
    elif choice == "2":
        Withdraw()
    elif choice == "3":
        Transfer()
    elif choice == "4":
        MainMenu()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        DepTran()

def Deposit():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\t\tPlease select which account you would like to deposit to.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. Checking Account\n\
            \r2. Savings Account\n\
            \r3. Back.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        #Check to see if the user have a checking account to deposit to
        if account.check != 1:
            print("You do not have a Checking acount.")
            Deposit()
        else:
            #Takes amount input and sends it to the deposit method
            amount = input("Please Enter amount you would like to deposit: \n")
            amount = int(amount)
            checking.Deposit(amount)
    elif choice == "2":
        #Check to see if the user have a savings account to deposit to
        if account.save != 1:
            print("You do not have a Savings acount.")
            Deposit()
        else:
            #takes amount input and sens it to the deposit method
            amount = input("Please Enter amount you would like to deposit: \n")
            amount = int(amount)
            saving.Deposit(amount)
    elif choice == "3":
        #Export the new account information to the text file
        account.Export(account.lastdate)
        DepTran()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        Deposit()

def Withdraw():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\t\tPlease select which account you would like to Withdraw from.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. Checking Account\n\
            \r2. Savings Account\n\
            \r3. Back.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        if account.check != 1:
            print("You do not have a Checking acount.")
            Withdraw()
        else:
            amount = input("Please Enter amount you would like to withdraw: \n")
            amount = int(amount)
            checking.Withdraw(amount, 0)
    elif choice == "2":
        #Setting the date format so it can be read from the file properly
        date_format = "%Y-%m-%d"
        a = datetime.strptime(account.lastdate, date_format)
        b = datetime.strptime(str(date.today()), date_format)
        #Taking the last withdrawal date from the current date to get days since withdrawal
        delta = b - a

        #Checking to see if the user actually has a saving account
        if account.save != 1:
            
            print("You do not have a Savings acount.")
            Withdraw()
        #If withdrawn less than 30 days ago, stop the user from withdrawing
        elif delta.days < 30:
            print("You mean only withdraw once every 30 days.")
            daysleft = 30 - delta.days
            print(f'You may withdraw in {daysleft} days')
            Withdraw()
        
        #If both are unsuccessful, program allows user to withdraw
        else:
            amount = input("Please Enter amount you would like to withdraw: \n")
            amount = int(amount)
            saving.Withdraw(amount)
    elif choice == "3":
        #Export the new account information to the text file
        account.Export(account.lastdate)
        DepTran()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        Withdraw()

def Transfer():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\t\tPlease select what you would like to do.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. List Users.\n\
            \r2. Transfer Money.\n\
            \r3. Back.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        #Displays a table of users with their ID's so the current user knows who they're sending money to
        user.DisplayUsers()
    elif choice == "2":
        #Asks the user whom they would like to send money to
        id = input("Enter Id to who you are transferring: \n")
        #User enters amount they would like to transfer
        amount = input("Enter amount you would like to transfer: \n")
        amount = int(amount)
        #User chooses which account they would like to send money to
        print("Enter acount type you would like to transfer to")
        type = input("Enter 1 for Checking and 0 for Savings:\n")
        #Sending the inputted information to the method
        checking.Transfer(id, amount, type)
    elif choice == "3":
        DepTran()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        DepTran()

def Delete():
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\tPlease select which account you would like to delete.\n\
            \r------------------------------------------------------------------------------------\n\
            \r1. Current Account.\n\
            \r2. Savings Account.\n\
            \r3. Back.\n')

    #If ladder in order to process users menu option
    choice = input("Enter Option: \n")
    if choice == "1":
        #Run method
        account.DeleteCheck()
        return
    elif choice == "2":
        #Run method
        account.DeleteSave()
        return
    elif choice == "3":
        #Export the new account information to the text file
        account.Export(account.lastdate)
        MainMenu()
    else:
        #Validation incase the user accidently inputs the wrong menu option
        print("\n\nIncorrect input, please try again.")
        Delete()

def Register(): #Allows the user to Register if they do not have an account.
    #Printing Menu
    print('------------------------------------------------------------------------------------\n\
                \r\t\tPlease enter the details you wish you register with.\n\
            \r------------------------------------------------------------------------------------\n')
    #First name input
    FirstName = input("Enter Firstname: ") 
    #Surname input
    SurName = input("Enter Surname: ") 
    #Users own choice of username
    Username = input("Enter Username: ") 
    #Checks for the length of the users username
    userlength = len(Username) 


    #If statement used as validation
    if userlength < 4:
        print("\nError: Username must be longer than 5 letters")
        #Sending the user back to the welcome screen
        Welcome()
    else:
        #Allows the user to choose a password
        Password = input("\nEnter Password: ")
        #Checks the user password length
        passlength = len(Password)

        #if statement for password validation
        if passlength > 20 or passlength < 6:
            print("\nError: Password must be 5-20 characters long") #
            #Sending the user back to the welcome screen
            Welcome()
        else:
            #Input for users age, used for checking account opening
            Age = input("\nEnter Age: ")
            #Converting the age input to int
            Age = int(Age)
            #Age validation
            if Age < 14:
                print("\nError: You are too young to open a bank account")
                #Sending the user back to the welcome screen
                Welcome()
            else:
                #If all validation is passed, the information is written to the customers file,
                #while also creating the skeleton for accounts.txt

                #Opening up the last line of customers.txt in order to increment the unique id of every user
                with open('Customers.txt', 'r') as f:
                   last_line = f.readlines()[-1]
                #Splits the line at every "," in order to be bale to access information
                details = last_line.split(",")
                #register is used in order to strip the information of any new line calls
                register = []
                for element in details:
                    register.append(element.strip())
                #Sets the id portion of register to int to allow addition
                register[4] = int(register[4])
                #Incrementing the unique id for the new registration
                NewID = register[4] + 1

                #Writing in the information into the customers file to allow for login.
                with open("customers.txt","a",newline="") as myfile:
                    writer = csv.writer(myfile)
                    writer.writerow([FirstName, SurName, Username,Password,NewID,Age])
                    myfile.close()
                
                #Writing empty skeleton to accounts, to allow them to create accounts later
                with open("accounts.txt","a",newline="") as myfile:
                    writer = csv.writer(myfile)
                    writer.writerow([NewID, 0, 0, 0, 0, 2000-10-10]) #Date is set to2000, to allow user to withdraw from a savings account if they make one
                    myfile.close()
                print("Registration successful, you may now login.")
                
                #Sending the user back to the welcome screen
                Welcome()


#Run Code here
Welcome()
