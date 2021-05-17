#To design an ATM mock up project

# Initialize page

import random
import validation
import database
import os
import funds

def init ():
    print('Welcome to bank PHP')
    
    haveAccount = int(input("""
    Do you have an account?
    1 for yes 
    2 for no
    """))

    if haveAccount == 1:
        print('**********Login**********')
        print('Welcome to the login page \n')
        login ()
    elif haveAccount == 2:
        print('Welcome to the registration page \n')
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
    
    
    useremail = input('What is your email? \n')
    email_validation = validation.useremail_validation(useremail)

    if email_validation:
        firstName = input('What is your first name? \n')

        lastName = input('What is your last name? \n')

        userPassword = input('What is your password \n')

        # Validate the user input for password
        is_valid_password = validation.password_validation(userPassword)
        
        if is_valid_password:
            username = firstName + lastName

            accountNumber = accountNumberGenerator()

            available_amount = funds.create_available_amount(accountNumber)

            database.create_user(accountNumber, str([firstName , lastName, useremail, userPassword, username]))

            funds.create_user_funds(accountNumber, available_amount)

            print(available_amount)

            print('Your account has been created... ')

            print("Here's your username " + username)
            print("Here's your account number %d make sure to keep it safe" % accountNumber )

            login ()
        else:
            register()
    else:
        register()



# login function
def login (): 
    userAccountNumber = input("What is your account number? \n")

    is_account_valid = validation.account_number_validation(userAccountNumber)

    if is_account_valid:
        
        is_login_valid = validation.login_validation(userAccountNumber)

        if is_login_valid: 
            user_password = input("What is your password? ")   
            is_password_valid = validation.password_validation(user_password)
            if is_password_valid:
                bankOperations2()
            else:
                login()
        else:
            login()
    else:
        print('Account Number is not valid')
        login()

    

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

# def check_balance():
    #account_number = input('What is your account number? ')
    #account_balance = funds.read_available_amount(account_number)
    #print(account_balance)






init()


