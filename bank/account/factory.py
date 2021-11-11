"""
Bank transaction factory
"""

"""
Manage a new account
"""

import os
import csv
from datetime import datetime

from ..analysis.transform import StandardTransform


DEFAULT_DIR = "/Users/jarry/Downloads"

class AccountFactory(StandardTransform):
    arg = ""

    def __init__(self, arg, account, payment_payees, rename_columns):
        self.arg = arg
        self.account = account
        self.payment_payees = payment_payees
        self.rename_columns = rename_columns

    def run(self, filename, date):
        self._read_activity_history(filename)
        self.process(date)
        self._write_activity_history()

    def _read_activity_history(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                self.rows.append(row)

    def _write_activity_history(self):
        now = datetime.now()
        dest_path = os.path.join(DEFAULT_DIR, "{}-{}.csv".format(
                                 self.arg, now.strftime("%Y-%m-%d-%f")))
        
        with open(dest_path, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.header)
            writer.writeheader()
            writer.writerows(self.rows)
