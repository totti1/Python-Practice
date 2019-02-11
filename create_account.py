class Account:
    """
    Class that generates new instances of credentials.
    """
    credentials = []  # Empty contact list

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into credentials
        '''
        Account.credentials.append(self)
        print("Account Created Successfully")
        return False

    @classmethod
    def check_user(cls, user, passw):
        '''
        check user method is the one that is checking user credentials in order to login
        '''
        for cred in cls.credentials:
            if(cred.username == user and cred.password == passw):
                print("User succesfully logged in")
                return True
            else:
                print("User doesn't exist")
            # print(cred.password)

    @classmethod
    def Display(cls):
        '''
        Display method displays every account created
        '''
        for eve in Account.credentials:

            print("you have created "+eve.username +
                  " with the password of " + eve.password)
            print("\n")

    def Remove(self):
        '''
        Remove method deletes one of the accounts created before
        '''
        Account.credentials.remove(self)
        print("Account with " + self.username + " was Successfully deleted")
        print("\n")
