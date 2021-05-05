#register
#- first name, last name, password. email
#- generate user id 


#login
#- email and password


#bank operations

#initializing the system
import random 

database = {} #dictionary

def init():

    isValidOptionSelected = False
    print("Welcome to bankPHP")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have selected invalid option")


def login():

    print("Login to your account")

    isLoginSuccessful = False

    while isLoginSuccessful == False:

        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails(3) == password):
                    isLoginSuccessful = True

        print("Invalid account or password")
    bankOperation(userDetails)


def register():

    print("Register")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password \n")

    accountNumber = generatingAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account has been created")
    print("=======================")
    print("Your account umber is %d" % accountNumber)
    print("Make sure you keep it safe")
    print("=======================")

    login()

def bankOperation(user):

    print("Welcome %s %s" % (user[0], user[1]))
    
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout"))

    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):
            
        withdrawalOperation()
    elif(selectedOption == 3):
            
        login()
    elif(selectedOption == 4):
            
        exit()
    else:
        
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit Operations")

def generatingAccountNumber():

    return random.randrange(1111111111,9999999999)



#### ACTUAL BANKING SYSTEM ####

print(generatingAccountNumber())
# init()
