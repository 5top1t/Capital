""""
Select a bank account to parse
"""
from .account.apple import Apple
from .account.boa import BankOfAmerica
from .account.capital_one import CapitalOne

class BankManager(object):
    def __init__(self):
        self.apple = Apple()
        self.boa = BankOfAmerica()
        self.capone = CapitalOne()

    def run(self, args):
        if args.bank == self.apple.arg:
            self.apple.run(args)
        elif args.bank == self.boa.arg:
            self.boa.run(args)
        elif args.bank == self.capone.arg:
            self.capone.run(args)
        else:
            raise Exception("Unknown bank arg={}".format(args.bank))
