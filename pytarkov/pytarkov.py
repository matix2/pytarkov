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
        self.data = data[0]

    def uid(self):
        return self.data["uid"]

    def name(self):
        return self.data["name"]

    def short_name(self):
        return self.data["shortName"]

    def price(self):
        return self.data["price"]

    def base_price(self):
        return self.data["basePrice"]

    def avg_24h_price(self):
        return self.data["avg24hPrice"]

    def avg_7d_price(self):
        return self.data["avg7daysPrice"]

    def trader_name(self):
        return self.data["traderName"]

    def trader_price(self):
        return self.data["traderPrice"]

    def trader_price_currency(self):
        return self.data["traderPriceCur"]

    def updated(self):
        return self.data["updated"]

    def slots(self):
        return self.data["slots"]

    def diff_24h(self):
        return self.data["diff24h"]

    def diff_7d(self):
        return self.data["diff7days"]

    def icon(self):
        return self.data["icon"]

    def link(self):
        return self.data["link"]

    def wiki_link(self):
        return self.data["wikiLink"]

    def img(self):
        return self.data["img"]

    def img_big(self):
        return self.data["imgBig"]

    def bsg_id(self):
        return self.data["bsgId"]

    def is_functional(self):
        return self.data["isFunctional"]

    def reference(self):
        return self.data["reference"]
