"""
Name of charge issuer
"""

class PayeeTranslation:
    column = "payee"
    name = ""
    synonyms = []

    def __init__(self, name, synonyms):
        self.name = name
        self.synonyms = synonyms

    def __eq__(self, other):
        try:
            self.name == other.name
        except AttributeError:
            self.name == other

    def __lt__(self, other):
        try:
            self.name == other.name
        except AttributeError:
            self.name == other

    def __le__(self, other):
        try:
            self.name <= other.name
        except AttributeError:
            self.name <= other

    def __gt__(self, other):
        try:
            self.name > other.name
        except AttributeError:
            self.name > other

    def __ge__(self, other):
        try:
            self.name >= other.name
        except AttributeError:
            self.name >= other

AMAZON = PayeeTranslation("Amazon Marketplace", ["AMZN Mktp", "AMZNAMZN.COM/BILLWA"])
JET_BLUE = PayeeTranslation("JetBlue", ["JETBLUE"])
EXPEDIA = PayeeTranslation("Expedia", ["EXPEDIA"])
STAPLES = PayeeTranslation("Staples", ["STAPLES"])
PRICERITE = PayeeTranslation("PriceRite", ["PRICERITE"])
WALMART = PayeeTranslation("Walmart", ["WAL-MART"])
UBER = PayeeTranslation("Uber", ["UBER TRIP"])
COMMUTER_RAIL = PayeeTranslation("Commuter Rail", ["COMMUTER RAIL SOUTH"])
ICON_CLUB = PayeeTranslation("Icon Club", ["ICON BOSTON MA"])
BIJOU_CLUB = PayeeTranslation("Bijou Club", ["THE BIJOU BOSTON"])
GAS = PayeeTranslation("Gas", ["SHELL OIL", "A.L. PRIME"])
MACYS = PayeeTranslation("Macy's", ["MACYS  NORTHSHORE"])
TACO_BELL = PayeeTranslation("Taco Bell", ["TACO BELL"])
TASTY_BURGER = PayeeTranslation("Tasty Burger", ["TASTY BURGER"])
PANDA_EXPRESS = PayeeTranslation("Panda Express", ["PANDA EXPRESS"])
CHIPOTLE = PayeeTranslation("Chipotle", ["CHIPOTLE"])
HARVARD_BUSSINESS_REVIEW = PayeeTranslation("Harvard Business Review", ["HARVBUSREV"])
COACHING = PayeeTranslation("Personal coach", ["PAYPAL *MARIALIZARR", "MARIALIZARR"])
EASTERN_MARKET = PayeeTranslation("Eastern Market", ["EASTERN MARKET"])
DOLLAR_TREE = PayeeTranslation("Dollar Tree", ["DOLLAR TREE"])
USPS = PayeeTranslation("USPS", ["USPS"])

ALL_PAYEE_TRANSLATIONS = [
    AMAZON,
    JET_BLUE,
    EXPEDIA,
    STAPLES,
    PRICERITE,
    WALMART,
    UBER,
    COMMUTER_RAIL,
    ICON_CLUB,
    BIJOU_CLUB,
    GAS,
    MACYS,
    TACO_BELL,
    TASTY_BURGER,
    PANDA_EXPRESS,
    CHIPOTLE,
    HARVARD_BUSSINESS_REVIEW,
    COACHING,
    EASTERN_MARKET,
    DOLLAR_TREE,
    USPS
]

RECURRING_PAYEE_TRANSLATIONS = [HARVARD_BUSSINESS_REVIEW, COACHING]
