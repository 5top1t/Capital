"""
Bank statement history
"""

from ..transaction.payee import (
    ALL_PAYEE_TRANSLATIONS, RECURRING_PAYEE_TRANSLATIONS)

class History(object): 
    all_payee_translations = ALL_PAYEE_TRANSLATIONS
    recurring_payee_translations = RECURRING_PAYEE_TRANSLATIONS
    account_key = "account"
    posted_date_key = "posted date"
    payee_key = "payee"
    cost_key = "cost"
    header = [account_key, posted_date_key, payee_key, cost_key]

    account = ""
    deposits = []
    translate_columns = dict()
    rows = []
