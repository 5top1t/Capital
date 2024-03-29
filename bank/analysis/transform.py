"""
Prepare data for analysis
"""

from datetime import datetime
from ..transaction.history import History

INTEREST_CHARGE_MERCHANT = "Interest charge"

class TranslationsTransform(History):
    def _translations_transform(self):
        for row in self.rows:
            is_translated = False
            for translation in self.all_merchant_translations:
                if is_translated is True:
                    break

                for synonym in translation.synonyms:
                    if synonym in row[self.merchant_key]:
                        row[self.merchant_key] = translation.name
                        is_translated = True
                        break

class InterestTransform(History):
    def _interests_charge_transform(self):
        for row in self.rows:
            if row[self.merchant_key] in self.interest_charges:
                row[self.merchant_key] = INTEREST_CHARGE_MERCHANT
                break 

class AccountTransform(History):
    def _add_account_column_transform(self):
        if self.account:
            for i in range(len(self.rows)):
                self.rows[i][self.account_key] = self.account
                
class NegateChargedAmountTransform(History):
    def _abs_value_cost_transform(self):
        for i in range(len(self.rows)):
            self.rows[i][self.cost_key] = -1 * abs(float(self.rows[i][self.cost_key]))


class RenameHeaderTransform(History):
    def _rename_columns_transform(self):
        for row in self.rows:
            for column, rename in self.rename_columns.items():
                if column in row:
                    row[rename] = row.pop(column)


class PurgeHeaderTransform(History):
    def _delete_non_header_columns_transform(self):
        for row in self.rows:
            for cell in row.copy():
                if not cell in self.header:
                    row.pop(cell)


class PurgePaymentsTransform(History):
    def _delete_payment_transactions_transform(self):
        payment_indices = []

        for i in range(len(self.rows)):
            for payee in self.payment_payees:
                if payee in self.rows[i][self.merchant_key]:
                    payment_indices.append(i)
                    
        for i in range(len(payment_indices)):
            self.rows.pop(payment_indices[i] - i)
            

class PurgeEmptyTransactionsTransform(History):
    # These transaction may be credits
    
    def _delete_empty_transactions_transform(self):
        payment_indices = []

        for i in range(len(self.rows)):
            if self.rows[i][self.cost_key] == '':
                payment_indices.append(i)

        for i in range(len(payment_indices)):
            self.rows.pop(payment_indices[i] - i)

class PurgeReccurringChargesTransform(History):
    def _delete_reccuring_transactions_transform(self):
        recurring_indices = []
        recurring_payees = [t.name for t in self.recurring_merchant_translations]

        for i in range(len(self.rows)):
            if self.rows[i][self.merchant_key] in recurring_payees:
                recurring_indices.append(i)

        for i in range(len(recurring_indices)):
            self.rows.pop(recurring_indices[i] - i)
            
class PurgeStarteDateTransform(History):
    def _delete_start_date_transform(self, start_date):
        date_filter_indices = []

        for i in range(len(self.rows)):
            transaction_date = datetime.strptime(self.rows[i][self.posted_date_key], self.date_format)
            if start_date > transaction_date:
                date_filter_indices.append(i)

        for i in range(len(date_filter_indices)):
            self.rows.pop(date_filter_indices[i] - i)
        

class PurgeMonthFilterTransform(History):
    def _delete_month_transform(self, month):
        month_filter_indices = []

        for i in range(len(self.rows)):
            transaction_date = datetime.strptime(
                self.rows[i][self.posted_date_key], self.date_format)
            if transaction_date.month != month:
                month_filter_indices.append(i)


        for i in range(len(month_filter_indices)):
            self.rows.pop(month_filter_indices[i] - i)

class ScrubTransform(RenameHeaderTransform, PurgeHeaderTransform, PurgePaymentsTransform, PurgeEmptyTransactionsTransform):
    def scrub(self):
        self._rename_columns_transform()
        self._delete_non_header_columns_transform()
        self._delete_payment_transactions_transform()
        self._delete_empty_transactions_transform()


class CleanseTransform(
        TranslationsTransform,
        InterestTransform,
        PurgeReccurringChargesTransform,
        AccountTransform,
        NegateChargedAmountTransform,
        PurgeStarteDateTransform,
        PurgeMonthFilterTransform):
    def cleanse(self, args):
        if args.date:
            self._delete_start_date_transform(args.date)
        if args.month:
            self._delete_month_transform(int(args.month))
        self._translations_transform()
        self._interests_charge_transform()
        self._delete_reccuring_transactions_transform()
        self._add_account_column_transform()
        self._abs_value_cost_transform()
    
class StandardTransform(ScrubTransform, CleanseTransform):
    
    def process(self, args):
        self.scrub()
        self.cleanse(args)
