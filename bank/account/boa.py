"""
Bank of America Account
"""

from .factory import AccountFactory

account = "BoA - Play Yourself"
arg = "boa"
payment_payees = ["Online payment from CHK"]
rename_columns = {
    "Posted Date": "posted date",
    "Payee": "merchant",
    "Amount": "cost"
}

class BankOfAmerica(AccountFactory):
    def __init__(self):
        super(BankOfAmerica, self).__init__(
            arg, account, payment_payees, rename_columns)
