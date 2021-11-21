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
AMAZON_WEB_SERVICES = PayeeTranslation(
    "Amazon Web Services", ["Amazon web services"])
JET_BLUE = PayeeTranslation("JetBlue", ["JETBLUE"])
EXPEDIA = PayeeTranslation("Expedia", ["EXPEDIA"])
STAPLES = PayeeTranslation("Staples", ["STAPLES"])
PRICERITE = PayeeTranslation("PriceRite", ["PRICERITE"])
WALMART = PayeeTranslation("Walmart", ["WAL-MART", "WM SUPERCENTER"])
UBER = PayeeTranslation("Uber", ["UBER TRIP"])
COMMUTER_RAIL = PayeeTranslation("Commuter Rail", ["COMMUTER RAIL SOUTH"])
ICON_CLUB = PayeeTranslation("Icon Club", ["ICON BOSTON MA"])
BIJOU_CLUB = PayeeTranslation("Bijou Club", ["THE BIJOU BOSTON"])
HAVANA_CLUB = PayeeTranslation("Havana Club", ["HAVANA CLUB"])
GAS = PayeeTranslation("Gas", ["SHELL OIL", "A.L. PRIME", "EXXONMOBIL"])
MACYS = PayeeTranslation("Macy's", ["MACYS  NORTHSHORE"])
TACO_BELL = PayeeTranslation("Taco Bell", ["TACO BELL"])
BUENA_VIDA = PayeeTranslation("Buena Vida ATL", ["BUENA VIDA ATLANTA"])
BAR_VEGAN = PayeeTranslation("Bar Vegan ATL", ["BAR VEGAN ATLANTA"])
CRAZY_GOOD_KITCHEN = PayeeTranslation(
    "Crazy Good Kitchen", ["CRAZY GOOD KITCHEN"])
TASTY_BURGER = PayeeTranslation("Tasty Burger", ["TASTY BURGER"])
PANDA_EXPRESS = PayeeTranslation("Panda Express", ["PANDA EXPRESS"])
CHIPOTLE = PayeeTranslation("Chipotle", ["CHIPOTLE"])
HARVARD_BUSSINESS_REVIEW = PayeeTranslation("Harvard Business Review", ["HARVBUSREV"])
COACHING = PayeeTranslation("Personal coach", ["PAYPAL *MARIALIZARR", "MARIALIZARR"])
EASTERN_MARKET = PayeeTranslation("Eastern Market", ["EASTERN MARKET"])
DOLLAR_TREE = PayeeTranslation("Dollar Tree", ["DOLLAR TREE"])
USPS = PayeeTranslation("USPS", ["USPS"])
YMCA = PayeeTranslation("YMCA", ["YMCA METRO NORTH"])
APPLE = PayeeTranslation("Apple", ["APPLE.COM/BILL"])
WAFFLE_HOUSE = PayeeTranslation("Waffle House", ["WAFFLE HOUSE"])
PARKING = PayeeTranslation("Parking", ["PARKING", "PAS*PASSPT"])
BOSTON_GLOBE = PayeeTranslation("Boston Globe", ["BOSTON GLOBE"])
AMERICAN_DELI = PayeeTranslation("American Deli", ["AMERICAN DELI"])
EAST_POLE_COFFEE = PayeeTranslation("East Poole Coffee", ["EASTPOLECOFFEECO"])
SUSTAINABLE_HOME = PayeeTranslation("Sustainable Home", ["SUSTAINABLE HOME"])
THE_PRINT_SHOP = PayeeTranslation("The Print Shop", ["THE PRINT SHOP"])
COMCAST = PayeeTranslation("Comcast", ["COMCAST"])
INTEREST_CHARGED = PayeeTranslation("Interest Charged", ["INTEREST CHARGED"])
CNBC = PayeeTranslation("CNBC ATL", ["CNBC ATLANTA"])
THE_VILLAGE_SMOKEHOUSE = PayeeTranslation("The Village SmokeHouse Bar", ["THE VILLAGE SMOKEHOUSE"])
FIVE_GUYS = PayeeTranslation("5 Guys", ["5GUYS"])
EL_JEFE = PayeeTranslation("El Jefe Taqueria", ["EL JEFE'S TAQUERIA"])
CVS_PHARMACY = PayeeTranslation("CVS", ["CVS/PHARMACY"])
HOME_DEPOT = PayeeTranslation("Home Depot", ["THE HOME DEPOT"])
NOTION = PayeeTranslation("Notion", ["NOTION LABS"])


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
    USPS,
    YMCA,
    APPLE,
    WAFFLE_HOUSE,
    PARKING,
    BOSTON_GLOBE,
    AMERICAN_DELI ,
    EAST_POLE_COFFEE,
    SUSTAINABLE_HOME,
    THE_PRINT_SHOP,
    COMCAST,
    HAVANA_CLUB,
    INTEREST_CHARGED,
    BUENA_VIDA,
    BAR_VEGAN,
    CRAZY_GOOD_KITCHEN,
    AMAZON_WEB_SERVICES,
    CNBC,
    THE_VILLAGE_SMOKEHOUSE,
    FIVE_GUYS,
    EL_JEFE,
    CVS_PHARMACY,
    HOME_DEPOT,
    NOTION
]

RECURRING_PAYEE_TRANSLATIONS = [
    HARVARD_BUSSINESS_REVIEW, COACHING, AMAZON_WEB_SERVICES, YMCA, BOSTON_GLOBE, COMCAST, AMAZON_WEB_SERVICES]
