"""
Prepare data for analysis
"""

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

        for i in range(len(self.rows)):
            if self.rows[i][self.payee_key] in self.recurring_payee_translations:
                recurring_indices.append(i)

        for i in range(len(recurring_indices)):
            self.rows.pop(recurring_indices[i] - i)


class ScrubTransform(RenameHeaderTransform, PurgeHeaderTransform, PurgePaymentsTransform):
    def scrub(self):
        self._rename_columns_transform()
        self._delete_non_header_columns_transform()
        self._delete_payment_transactions_transform()


class CleanseTransform(TranslationsTransform, PurgeReccurringChargesTransform, AccountTransform):
    def cleanse(self):
        self._translations_transform()
        self._delete_reccuring_transactions_transform()
        self._add_account_column_transform()

class StandardTransform(ScrubTransform, CleanseTransform):
    def process(self):
        self.scrub()
        self.cleanse()
