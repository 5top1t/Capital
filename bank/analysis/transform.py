"""
Prepare data for analysis
"""

from datetime import datetime
from ..transaction.history import History

class TranslationsTransform(History):
    def _translations_transform(self):
        for row in self.rows:
            is_translated = False
            for translation in self.all_payee_translations:
                if is_translated is True:
                    break

                for synonym in translation.synonyms:
                    if synonym in row[self.payee_key]:
                        row[self.payee_key] = translation.name
                        is_translated = True
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
                if payee in self.rows[i][self.payee_key]:
                    payment_indices.append(i)

        for i in range(len(payment_indices)):
            self.rows.pop(payment_indices[i] - i)


class PurgeReccurringChargesTransform(History):
    def _delete_reccuring_transactions_transform(self):
        recurring_indices = []
        recurring_payees = [t.name for t in self.recurring_payee_translations]

        for i in range(len(self.rows)):
            if self.rows[i][self.payee_key] in recurring_payees:
                recurring_indices.append(i)

        for i in range(len(recurring_indices)):
            self.rows.pop(recurring_indices[i] - i)
            
class PurgeStarteDateTransform(History):
    def _delete_start_date_transform(self, date):
        date_filter_indices = []
        date_format = '%m/%d/%Y'
        start_date = datetime.strptime(date, date_format)

        for i in range(len(self.rows)):
            transaction_date = datetime.strptime(self.rows[i][self.posted_date_key], date_format)
            if start_date > transaction_date:
                date_filter_indices.append(i)

        for i in range(len(date_filter_indices)):
            self.rows.pop(date_filter_indices[i] - i)
        

class PurgeMonthFilterTransform(History):
    def _delete_month_transform(self, month):
        month_filter_indices = []
        date_format = '%m/%d/%Y'

        for i in range(len(self.rows)):
            transaction_date = datetime.strptime(
                self.rows[i][self.posted_date_key], date_format)
            if transaction_date.month != month:
                month_filter_indices.append(i)


        print(len(month_filter_indices))
        for i in range(len(month_filter_indices)):
            self.rows.pop(month_filter_indices[i] - i)
            
        print(len(self.rows))


class ScrubTransform(RenameHeaderTransform, PurgeHeaderTransform, PurgePaymentsTransform):
    def scrub(self):
        self._rename_columns_transform()
        self._delete_non_header_columns_transform()
        self._delete_payment_transactions_transform()


class CleanseTransform(
        TranslationsTransform,
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
        self._delete_reccuring_transactions_transform()
        self._add_account_column_transform()
        self._abs_value_cost_transform()
    
class StandardTransform(ScrubTransform, CleanseTransform):
    
    def process(self, args):
        self.scrub()
        self.cleanse(args)
