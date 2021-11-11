import argparse
from bank import (BankManager, BANK_ARGS)

manager = BankManager()

parser = argparse.ArgumentParser(description="Financial runner argument parser")
parser.add_argument(
    '-bank', choices=BANK_ARGS, help='Transaction processor')
parser.add_argument(
    '-file', help='Transaction file path')
parser.add_argument(
    '-date', help='Filter transaction on or after this date')
args = parser.parse_args()

manager.run(args)
