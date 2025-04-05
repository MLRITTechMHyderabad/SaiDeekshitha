class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        
        :param amount: Amount to withdraw
        :return: Remaining balance or error message
        """
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("amount must be a number")
            elif amount<0:
                raise ValueError("No Negative amount")
            elif amount>self.balance:
                raise InsufficientFundsError("Insufficient Funds")
            self.balance-=amount
            return "Remaining balance: ₹{self.balance}"
        
        except ValueError as e:
            return e
        except InsufficientFundsError as e:
            return e
        except Exception as e:
            return e

# Example Usage:
account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
