"""
Bank statement history
"""

from ..transaction.merchant import (
    ALL_MERCHANT_TRANSLATIONS, RECURRING_MERCHANT_TRANSLATIONS)

class History(object): 
    all_merchant_translations = ALL_MERCHANT_TRANSLATIONS
    recurring_merchant_translations = RECURRING_MERCHANT_TRANSLATIONS
    account_key = "account"
    posted_date_key = "posted date"
    merchant_key = "merchant"
    cost_key = "cost"
    header = [account_key, posted_date_key, merchant_key, cost_key]

    account = ""
    deposits = []
    translate_columns = dict()
    rows = []
