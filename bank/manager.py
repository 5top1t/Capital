""""
Select a bank account to parse
"""
from .account.boa import BankOfAmerica
from .account.capital_one import CapitalOne

class BankManager(object):
    def __init__(self):
        self.boa = BankOfAmerica()
        self.capone = CapitalOne()

    def run(self, args):
        if args.bank == self.boa.arg:
            self.boa.run(args.file, args.date)
        if args.bank == self.capone.arg:
            self.capone.run(args.file, args.date)
