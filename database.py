import os

# CRUD operations 
# Create a user
# Read a users details
# Update the user details
# Delete the user details

user_file_path = "data/user_record/"

def create_user(account_number, user_details):
# create a list that contains the necessary details for the user
# create a file that would help to store the details for the user

    is_create_user_succesful = False

    try:

        f = open(user_file_path + str(account_number) + ".txt", "w")

        f.write( user_details)
    
    except FileExistsError:

        if os.path.exists(user_file_path + str(account_number) + ".txt"):
            print('user already exist')
            return is_create_user_succesful
        f.close()


def read_user(account_number):
# read through a user details
    print('Reading through user detials... ')
    f = open(user_file_path + str(account_number) + ".txt", "r")
    print(f.read())

def update_user(user_details):
    print('ddd')


def delete_user(user_details):
# delete a user details
    print("User details has been deleted! ")


#read_user('8665327580')