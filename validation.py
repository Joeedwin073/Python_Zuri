import os

    # Account Number validation
def account_number_validation(accountNumber):
    
    # check if there is an account number

    if accountNumber:

        # check if the account number is up to 10 digits

        if len(str(accountNumber)) == 10:

            # check if the account number can be converted to an integer and catch the errors
            try:
                int(accountNumber)
                return True

            except ValueError:
                print("Invalid account number, account should be an integer ")
                return False
            except TypeError:
                print('invalid account')
                return False
            
        else:
            print('Account number must be 10 digits! ')
            return False

    else:
        print('account number is not valid')
        return False


# Password validaion

def password_validation(password):
    # Check if there is a password
    # Check if the password is more than 8 digits
    # Ensure the password is neither the person's name, username or email
    # Ensure the password contains a number, letter and a special character

    
    if password:

        if len(password) >= 8:
            print('password is greater than 8. ')
            return True

            # for loop to iterate over the password to check for numbers

        else:
            print('Password must be greater than or equal to 8 digits! ')
            return False
            
    else:
        print('Please you have to input a password! ')
        return False


def useremail_validation(useremail):
    
    is_useremail_verified = False

    if useremail:
    
        if useremail.endswith('.com'):
            return True
        else:
            print('Useremail must end with ".com" pls try again')
            return is_useremail_verified
    else: 
        print('This field is compulsory! ')


# Validation of the login function
def login_validation(accountNumber):

    if os.path.exists('./data/user_record/' + str(accountNumber) + '.txt'):

        return True
    else:
        print('It doesnt exist')
        return False



password_validation('dshddd4dis')