"""
Name of charge issuer
"""

class MerchantTranslation:
    column = "merchant"
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

AMAZON = MerchantTranslation("Amazon Marketplace", ["AMZN Mktp", "AMZNAMZN.COM/BILLWA"])
AMAZON_WEB_SERVICES = MerchantTranslation(
    "Amazon Web Services", ["Amazon web services"])
JET_BLUE = MerchantTranslation("JetBlue", ["JETBLUE"])
EXPEDIA = MerchantTranslation("Expedia", ["EXPEDIA"])
STAPLES = MerchantTranslation("Staples", ["STAPLES"])
PRICERITE = MerchantTranslation("PriceRite", ["PRICERITE"])
WALMART = MerchantTranslation("Walmart", ["WAL-MART", "WM SUPERCENTER"])
UBER = MerchantTranslation("Uber", ["UBER TRIP"])
COMMUTER_RAIL = MerchantTranslation("Commuter Rail", ["COMMUTER RAIL SOUTH"])
ICON_CLUB = MerchantTranslation("Icon Club", ["ICON BOSTON MA"])
BIJOU_CLUB = MerchantTranslation("Bijou Club", ["THE BIJOU BOSTON"])
HAVANA_CLUB = MerchantTranslation("Havana Club", ["HAVANA CLUB"])
GAS = MerchantTranslation("Gas", ["SHELL OIL", "A.L. PRIME", "EXXONMOBIL"])
MACYS = MerchantTranslation("Macy's", ["MACYS  NORTHSHORE"])
TACO_BELL = MerchantTranslation("Taco Bell", ["TACO BELL"])
BUENA_VIDA = MerchantTranslation("Buena Vida ATL", ["BUENA VIDA ATLANTA"])
BAR_VEGAN = MerchantTranslation("Bar Vegan ATL", ["BAR VEGAN ATLANTA"])
CRAZY_GOOD_KITCHEN = MerchantTranslation(
    "Crazy Good Kitchen", ["CRAZY GOOD KITCHEN"])
TASTY_BURGER = MerchantTranslation("Tasty Burger", ["TASTY BURGER"])
PANDA_EXPRESS = MerchantTranslation("Panda Express", ["PANDA EXPRESS"])
CHIPOTLE = MerchantTranslation("Chipotle", ["CHIPOTLE"])
HARVARD_BUSSINESS_REVIEW = MerchantTranslation("Harvard Business Review", ["HARVBUSREV"])
COACHING = MerchantTranslation("Personal coach", ["PAYPAL *MARIALIZARR", "MARIALIZARR"])
EASTERN_MARKET = MerchantTranslation("Eastern Market", ["EASTERN MARKET"])
DOLLAR_TREE = MerchantTranslation("Dollar Tree", ["DOLLAR TREE"])
USPS = MerchantTranslation("USPS", ["USPS"])
YMCA = MerchantTranslation("YMCA", ["YMCA METRO NORTH"])
APPLE = MerchantTranslation("Apple", ["APPLE.COM/BILL"])
WAFFLE_HOUSE = MerchantTranslation("Waffle House", ["WAFFLE HOUSE"])
PARKING = MerchantTranslation("Parking", ["PARKING", "PAS*PASSPT"])
BOSTON_GLOBE = MerchantTranslation("Boston Globe", ["BOSTON GLOBE"])
AMERICAN_DELI = MerchantTranslation("American Deli", ["AMERICAN DELI"])
EAST_POLE_COFFEE = MerchantTranslation("East Poole Coffee", ["EASTPOLECOFFEECO"])
SUSTAINABLE_HOME = MerchantTranslation("Sustainable Home", ["SUSTAINABLE HOME"])
THE_PRINT_SHOP = MerchantTranslation("The Print Shop", ["THE PRINT SHOP"])
COMCAST = MerchantTranslation("Comcast", ["COMCAST"])
INTEREST_CHARGED = MerchantTranslation("Interest Charged", ["INTEREST CHARGED"])
CNBC = MerchantTranslation("CNBC ATL", ["CNBC ATLANTA"])
THE_VILLAGE_SMOKEHOUSE = MerchantTranslation("The Village SmokeHouse Bar", ["THE VILLAGE SMOKEHOUSE"])
FIVE_GUYS = MerchantTranslation("5 Guys", ["5GUYS"])
EL_JEFE = MerchantTranslation("El Jefe Taqueria", ["EL JEFE'S TAQUERIA"])
CVS_PHARMACY = MerchantTranslation("CVS", ["CVS/PHARMACY"])
HOME_DEPOT = MerchantTranslation("Home Depot", ["THE HOME DEPOT"])
NOTION = MerchantTranslation("Notion", ["NOTION LABS"])
WHOLE_FOODS = MerchantTranslation("Whole Foods Market", ["WHOLEFDS"])
CAR_WASH = MerchantTranslation("Car Wash", ["CAR WASH", "SIMONIZ CAR WASH"])
LIQUOR = MerchantTranslation("Liquor", ["LYNNWAY LIQUORS"])
NBA_LEAGUE_PASS = MerchantTranslation("NBA League Pass", ["NBA LEAGUE"])
PIZZERIA = MerchantTranslation("Pizzeria", ["PIZZERIA"])
ESTEFANIS = MerchantTranslation("Estefani's", ["ESTEFANI"])
CITY_BAR = MerchantTranslation("City Bay Back Bay", ["CITY BAR"])
LAUNDRY = MerchantTranslation("Laundry", ["SALEM LAUNDRY COMPANY"])
AFRO_NATION_TICKETS = MerchantTranslation(
    "Afro Nation Tickets", ["FT* FESTICKET"])
URBAN_OUTFITTERS = MerchantTranslation("Urban Outfitters", ["URBAN-OUTFITTERS "])
CHAMPION = MerchantTranslation("Champion", ["NEWBURY CHAMPION"])


ALL_MERCHANT_TRANSLATIONS = [
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
    NOTION,
    WHOLE_FOODS,
    CAR_WASH,
    LIQUOR,
    NBA_LEAGUE_PASS,
    PIZZERIA,
    ESTEFANIS,
    CITY_BAR,
    LAUNDRY,
    AFRO_NATION_TICKETS,
    URBAN_OUTFITTERS,
    CHAMPION
]
RECURRING_MERCHANT_TRANSLATIONS = [
    HARVARD_BUSSINESS_REVIEW, COACHING, AMAZON_WEB_SERVICES, YMCA, BOSTON_GLOBE, COMCAST, AMAZON_WEB_SERVICES]
