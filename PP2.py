#To design an ATM mock up project

# Initialize page

import random

database = {} #dictionary


def init ():
    print('Welcome to bank PHP')
    
    haveAccount = int(input("""
    Do you have an account?
    1 for yes 
    2 for no
    """))

    if haveAccount == 1:
        print()
        login ()
    elif haveAccount == 2:
        print()
        register()

# banking operations
def bankOperations (username):
    print('Welcome %s' % username)

    bankOperations2 ()

def bankOperations2 ():

    userOptionSelected = int(input('''
    Pls what would you like to do
    1 for deposit
    2 for withdrawal
    3 for Account Balance Check
    4 for logout
    5 to exit
    '''))
    if userOptionSelected == 1:
        deposit ()
    elif userOptionSelected == 2:
        withdrawal ()
    elif userOptionSelected == 3:
        accountBalanceCheck ()
    elif userOptionSelected == 4:
        login ()
    elif userOptionSelected == 5:
        exit ()
    else:
        bankOperations2 ()

#Bank Operations3
def bankOperations3 ():
    userOption = int(input('''
    What else woould you like to do?
    select 
    1 for deposit
    2 for withdrawal
    3 to check account balance
    4 to logout
    5 to exit
    '''))
    
    if userOption == 1:
        deposit()
    elif userOption == 2:
        withdrawal()
    elif userOption == 3:
        accountBalanceCheck()
    elif userOption == 4:
        login()
    elif userOption == 5:
        exit ()
    else: 
        print('You have not selceted a valid option! ')
        bankOperations3()

# register function
def register ():
    print('Welcome to the registration page \n')

    useremail = input('What is your email? \n')

    firstName = input('What is your first name? \n')

    lastName = input('What is your last name? \n')

    username = firstName + lastName

    userPassword = input('What is your password \n')

    accountNumber = accountNumberGenerator ()

    database[accountNumber] = [firstName, lastName, useremail, userPassword, username]
    print(database)

    print('Your account has been created... ')

    print("Here's your username " + username)
    print("Here's your account number %d make sure to keep it safe" % accountNumber )

    login ()


# login function
def login (): 
    print('**********Login**********')

    userAccountNumber = int(input("What is your account number? \n"))

    for accountNumber,userDetails in database.items():
        if accountNumber == userAccountNumber:
            userPassword = input('What is your password? \n')
            if userPassword == userDetails[3]:
                bankOperations(userDetails[4])
            else:
                print('User password not correct!!!')
                login ()
        else:
            print('User account number not correct!!!')
            login ()



# Account number generator
def accountNumberGenerator ():
    num = random.randrange(1111111111,9999999999)
    return num

# Account Balance Check
def accountBalanceCheck():
    print('You have %d in your account. ' % availableAmount)
    bankOperations3()

# deposit
def deposit ():
    global availableAmount
    depositAmount = int(input("How much would you like to deposit? \n"))
    print('Current balance: %d' % depositAmount)
    availableAmount =+ depositAmount
    print('You have %s in your account' % availableAmount)
     
    bankOperations3 ()


# withdrawal 
def withdrawal ():
    withdrawalAmount = int(input('How much would like to withdraw? \n'))
    print('You have withdrawn %d' % withdrawalAmount)
    print('Amount remaining: %d' % availableAmount - withdrawalAmount)





init()

#   num = random.randrange(1111111111,9999999999)
#   print(num)

