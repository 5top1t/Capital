"""
Capitol One Account
"""

from .factory import AccountFactory

account = "Capital One"
arg = "capone"
payment_payees = ["CAPITAL ONE MOBILE PYMT", "CAPITAL ONE AUTOPAY PYMT"]
rename_columns = {
    "Transaction Date": "posted date",
    "Description": "merchant",
    "Debit": "cost"
}

class CapitalOne(AccountFactory):
    def __init__(self):
        super(CapitalOne, self).__init__(
            arg, account, payment_payees, rename_columns)
