"""
Capitol One Account
"""

from .factory import AccountFactory

account = "Capital One"
payment_payees = ["CAPITAL ONE MOBILE PYMT", "CAPITAL ONE AUTOPAY PYMT"]
rename_columns = {
    "Transaction Date": "posted date",
    "Description": "payee",
    "Debit": "cost"
}

class CapitalOne(AccountFactory):
    def __init__(self, cmd_option):
        super(CapitalOne, self).__init__(cmd_option, account, payment_payees, rename_columns)
