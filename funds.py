import os
import ast

# Create an available amount index the user details
# allow for an update of funds in the user details
# allow for a reduction of funds in the user details

user_file_path = "data/user_funds/"


def create_user_funds(account_number, available_amount):
# create a list that contains the necessary details for the user

    is_create_user_succesful = False

    user_id = {"account_number" : available_amount}

    try:

        f = open(user_file_path + str(account_number) + ".txt", "a")

        f.write(str(user_id))
    
    except FileExistsError:

        if os.path.exists(user_file_path + str(account_number) + ".txt"):
            print('user already exist')
            return is_create_user_succesful
        f.close()






def create_available_amount(account_number):
    available_amount = 0
    return available_amount

def read_available_amount(account_number):
    # This function is used to check the account balance.
    with open(user_file_path + str(account_number) + ".txt", "r") as data:

        user_dict = ast.literal_eval(data.read())
        # the code above is used to convert the string in the file to a dictionary so that it can be acessed.

        return user_dict['account_number']


def update_available_amount(account_number, amount_deposited):

    with open(user_file_path + str(account_number) + ".txt", "r") as data:

        user_dict = ast.literal_eval(data.read()) 
        print(user_dict)
        updated_amount = user_dict['account_number'] + amount_deposited
        # user_dict['account_number'] = updated_amount
        user_dict.update({'account_number': updated_amount})
        print(user_dict)

        print(user_dict['account_number'])

    print('available amount updated')

update_available_amount(9343447748, 2000)