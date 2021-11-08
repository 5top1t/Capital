import argparse
from bank import (BankOfAmerica, CapitalOne)
from options import (BOA_ARG, CAPONE_ARG)

boa = BankOfAmerica(BOA_ARG)
capone = CapitalOne(CAPONE_ARG)

parser = argparse.ArgumentParser(description="Financial runner argument parser")
parser.add_argument(
    '-bank', choices=[BOA_ARG, CAPONE_ARG], help='Transaction processor')
parser.add_argument(
    '-fp', help='Transaction file path')
args = parser.parse_args()

if args.bank == BOA_ARG:
    boa.run(args.fp)
if args.bank == CAPONE_ARG:
    capone.run(args.fp)
