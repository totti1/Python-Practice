import unittest
from create_account import Account


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Account("aris","1234567890")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case runs
        """
        Account.credentials=[]

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"aris")
        self.assertEqual(self.new_user.password,"1234567890")

    def test_save_user(self):
        """
        test case to see if the user name is saved into the user usernames
        """
        self.new_user.save_account()
        self.assertEqual(len(Account.credentials),1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple usernames to our user_names
        """
        self.new_user.save_account()
        test_user = Account("aris","1234567890")
        test_user.save_account()
        self.assertEqual(len(Account.credentials),2)

    def test_check_user(self):
        """
        test to check if we can return a Boolean if we cannot find the users
        """
        self.new_user.save_account()
        test_user=Account("aris","1234567890")
        test_user.save_account()

        user_exists = Account.check_user("aris","1234567890")
        self.assertTrue(user_exists)

    def test_Remove(self):
        '''
        test_Remove to test if we can remove a user credentials from our credentials array
        '''
        self.new_user.save_account()
        test_contact = Account("aris","1234567890") # new contact
        test_contact.save_account()

        self.new_user.Remove()# Deleting a contact object
        self.assertEqual(len(Account.credentials),1)

if __name__ == '__main__':
    unittest.main()
