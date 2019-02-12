from create_account import Account

# def Create_User():
print("Welcome to Password Locker")
print("\n")
print("Please create an account")
print("\n")
print("Enter username")
username = input()
print("Do you want us to generate a password for you ? y-Yes, n-No")
confirm = input().lower()
if(confirm == 'y'):
    password = "1234567890"
    print("Your Paasword is "+password)
else:
    print("Now create your own password")
    password = input().lower()

myAccount = Account(username, password)
myAccount.save_account()
print(f"Log in details for {username}  have been saved")


def Sign_in():
    '''
        Sign_in method helps to retrieve data from the user and pass it into Account class to perform the sign in action
    '''
    print("Welcome to Login Interface")
    print("Fill in the required details")
    print("Please enter a username")
    usernameLog = input()
    print("Please add a password")
    passwordLog = input().lower()
    Account.check_user(usernameLog, passwordLog)


def Add_user():
    '''
        add_user method creates unlimited amount of account that the user will want to create
    '''

    print("Add an Account")
    print("\n")
    print("Enter username")
    username = input()
    print("Do you want us to generate a password for you ? y-Yes, n-No")
    confirm = input().lower()
    if(confirm == 'y'):
        password = "1234567890"
        print("Your Paasword is "+password)
    else:
        password = input().lower()

    myAccount = Account(username, password)
    myAccount.save_account()
    print(f"Log in details for {username}  have been saved")


def main():
    '''
        main function that make everything happen
    '''
    # print("Welcome!")
    # Create_User()

    while True:
        print("Please use these short codes to navigate:ac -create a new account, dc -display credentials, log -if you already have an account and ex to exit the application, de -delete your credentials, ex -exit the application")
        short_code = input().lower()

        if short_code == 'ac':
            Add_user()

        elif short_code == 'dc':
            Account.Display()

        elif short_code == 'log':
            Sign_in()

        elif short_code == 'de':
            # print("Nothing was deleted")
            Account.Remove(myAccount)
            # Sign_in()

        elif short_code == 'ex':
            print("See you soon ! :)")
            break

        else:
            print("User does not exist please create an account first")
            break


main()
