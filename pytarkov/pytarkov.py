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
        self.data = data

    def uid(self):
        return self.data[0]["uid"]

    def name(self):
        return self.data[0]["name"]

    def short_name(self):
        return self.data[0]["shortName"]

    def price(self):
        return self.data[0]["price"]

    def base_price(self):
        return self.data[0]["basePrice"]

    def avg_24h_price(self):
        return self.data[0]["avg24hPrice"]

    def avg_7d_price(self):
        return self.data[0]["avg7daysPrice"]

    def trader_name(self):
        return self.data[0]["traderName"]

    def trader_price(self):
        return self.data[0]["traderPrice"]

    def trader_price_currency(self):
        return self.data[0]["traderPriceCur"]

    def updated(self):
        return self.data[0]["updated"]

    def slots(self):
        return self.data[0]["slots"]

    def diff_24h(self):
        return self.data[0]["diff24h"]

    def diff_7d(self):
        return self.data[0]["diff7days"]

    def icon(self):
        return self.data[0]["icon"]

    def link(self):
        return self.data[0]["link"]

    def wiki_link(self):
        return self.data[0]["wikiLink"]

    def img(self):
        return self.data[0]["img"]

    def img_big(self):
        return self.data[0]["imgBig"]

    def bsg_id(self):
        return self.data[0]["bsgId"]

    def is_functional(self):
        return self.data[0]["isFunctional"]

    def reference(self):
        return self.data[0]["reference"]
