"""
Bank of America Account
"""

from .factory import AccountFactory

account = "BoA - Play Yourself"
payment_payees = ["Online payment from CHK"]
rename_columns = {
    "Posted Date": "posted date",
    "Payee": "payee",
    "Amount": "cost"
}

class BankOfAmerica(AccountFactory):
    def __init__(self, cmd_option):
        super(BankOfAmerica, self).__init__(cmd_option, account, payment_payees,rename_columns)
