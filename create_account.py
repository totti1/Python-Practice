class Account:
    """
    Class that generates new instances of credentials.
    """
    credentials = []  # Empty contact list

    def __init__(self, username, password):

      # docstring removed for simplicity

        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        Account.credentials.append(self)
        print("Account Created Successfully")
        return False

    @classmethod
    def check_user(cls, user, passw):
        '''
        save_contact method saves contact objects into contact_list
        '''
        for cred in cls.credentials:
            if(cred.username == user, cred.password == passw):
                print("User succesfully logged in")
                return False
            else:
                print("User doesn't exist")
            # print(cred.password)

    @classmethod
    def Display(cls):
        for eve in Account.credentials:

            print("you have created "+eve.username +
                  " with the password of " + eve.password)
            print("\n")

    def Remove(self):
        Account.credentials.remove(self)
        print("Account with " + self.username + " was Successfully deleted")
        print("\n")
    # def delete_contact(self):

    #     '''
    #     delete_contact method deletes a saved contact from the contact_list
    #     '''

    #     Login.credentials.remove(self)
