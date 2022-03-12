"""
Bank of America Account
"""

from .factory import AccountFactory

account = "BoA - Play Yourself"
arg = "boa"
payment_payees = ["Online payment from CHK", "MA Banking Center payment"]
interest_charges = ["INTEREST CHARGED ON PURCHASES"]
rename_columns = {
    "Posted Date": "posted date",
    "Payee": "merchant",
    "Amount": "cost"
}

class BankOfAmerica(AccountFactory):
    def __init__(self):
        super(BankOfAmerica, self).__init__(
            arg, account, payment_payees, interest_charges, rename_columns)
