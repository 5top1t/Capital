"""
Bank of America Account
"""

from .factory import AccountFactory

account = "Apple Card"
arg = "apple"
payment_payees = ["Online payment from CHK", "ACH DEPOSIT"]
interest_charges = ["DAILY CASH ADJUSTMENT"]
rename_columns = {
    "Transaction Date": "posted date",
    "Description": "merchant",
    "Amount (USD)": "cost"
}

class Apple(AccountFactory):
    def __init__(self):
        super(Apple, self).__init__(
            arg, account, payment_payees, interest_charges, rename_columns)
