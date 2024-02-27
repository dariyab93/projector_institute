import unittest

class TestBankMethods(unittest.TestCase):

    def test_open_account(self):
        bank = Bank()

        savings_account = SavingsAccount(2001, 10000, 0.05)
        bank.open_account(savings_account)

        self.assertIn(savings_account, bank.accounts)
        self.assertEqual(savings_account.balance, 10000)
        self.assertTrue(hasattr(savings_account, 'account_number'))

    def test_update_accounts(self):
        # Arrange
        bank = Bank()
        savings_account = SavingsAccount(2001, 10000, 0.05)
        current_account = CurrentAccount(3001, -500, 1500)
        bank.add_account(savings_account)
        bank.add_account(current_account)

        # Act
        bank.update_accounts()

        # Check if the interest was added to the savings account
        self.assertEqual(savings_account.balance, 10500)  

        # Check if the overdraft letter was sent for the current account
        self.assertTrue(current_account.balance < 0)  # Current account is in overdraft

if __name__ == '__main__':
    unittest.main()
