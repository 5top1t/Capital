import argparse
import datetime
from bank import (BankManager, BANK_ARGS)

manager = BankManager()
month_choices = [str(m) for m in range(1,13)]

parser = argparse.ArgumentParser(description="Financial runner argument parser")
parser.add_argument(
    '-bank', choices=BANK_ARGS, help='Bank to be processed', required=True)
parser.add_argument(
    '-file', help='Transaction export file path', required=True)
parser.add_argument(
    '-month', choices=month_choices, help='Filter transactions for the given month')
parser.add_argument(
    '-date',
    type=lambda s: datetime.datetime.strptime(s, '%m/%d/%Y'), help='Filter transactions after a given date (inclusive)')

args = parser.parse_args()

manager.run(args)
