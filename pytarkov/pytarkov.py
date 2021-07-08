import requests


class PyTarkov:
    def __init__(self, api_key):
        self.api_key = api_key

    class InvalidItem(Exception):
        def __init__(self, message="Invalid Item"):
            self.message = message
            super().__init__(self.message)

    class InvalidAPIKey(Exception):
        def __init__(self, message="Invalid API Key"):
            self.message = message
            super().__init__(self.message)

    def __get_data(self, url):
        response = requests.get(url).json()
        if not response:
            raise self.InvalidItem
        elif "Access denied" in str(response):
            raise self.InvalidAPIKey
        else:
            return response

    def get_item_by_name(self, item_name):
        return Item(self.__get_data(f"https://tarkov-market.com/api/v1/item?q={item_name}&x-api-key={self.api_key}"))

    def get_item_by_uid(self, uid):
        return Item(self.__get_data(f"https://tarkov-market.com/api/v1/item?uid={uid}&x-api-key={self.api_key}"))

    def get_all_items(self):
        return self.__get_data(f"https://tarkov-market.com/api/v1/items/all?x-api-key={self.api_key}")

    def get_bsg_raw(self):
        return self.__get_data(f"https://tarkov-market.com/api/v1/bsg/items/all?x-api-key={self.api_key}")


class Item:
    def __init__(self, data):
        self.__data = data[0]
        self.uid = data["uid"]
        self.name = data["name"]
        self.short_name = data["shortName"]
        self.price = data["price"]
        self.base_price = data["basePrice"]
        self.avg_24h_price = data["avg24hPrice"]
        self.avg_7d_price = data["avg7daysPrice"]
        self.trader_name = data["traderName"]
        self.trader_price = data["traderPrice"]
        self.trader_price_currency = data["traderPriceCur"]
        self.updated = data["updated"]
        self.slots = data["slots"]
        self.diff_24h = data["diff24h"]
        self.diff_7d = data["diff7days"]
        self.icon = data["icon"]
        self.link = data["link"]
        self.wiki_link = data["wikiLink"]
        self.img = data["img"]
        self.img_big = data["imgBig"]
        self.bsg_id = data["bsgId"]
        self.is_functional = data["isFunctional"]
        self.reference = data["reference"]
