from time import sleep

import requests
import urllib.parse

from mana_pizza.commons.log import get_logger


class ScryfallEndpoints:
    SEARCH_CARD    = "cards/search"
    LIST_SYMBOLOGY = "symbology"


class ScryfallClient:

    __SCRYFALL_API_HOST = "https://api.scryfall.com"

    def __request_scryfall_api(self, endpoint, body=None, params=None):
        sleep(.1)
        res = requests.get(f"{self.__SCRYFALL_API_HOST}/{endpoint}", json=body or {}, params=params or {})
        if res.status_code > 299:
            get_logger().error(f"Something happened when requesting scryfall API: {res.content}")
            get_logger().error(f"Endpoint: {endpoint}. Status code: {res.status_code}")
            return None
        return res.json()

    def __encode_q_param(self, value):
        return urllib.parse.quote(value, safe='"!, /\: \'')

    def fetch_symbology(self):
        return self.__request_scryfall_api(ScryfallEndpoints.LIST_SYMBOLOGY)["data"]

    def fetch_card_by_name(self, card_name, edition=None):
        get_logger().debug(f"Fetching card {card_name} from scryfall...")
        query = f"!\"{card_name}\""
        if edition:
            query += f" set:{edition}"
        res = self.__request_scryfall_api(ScryfallEndpoints.SEARCH_CARD, params={"q": self.__encode_q_param(query)})
        if not res:
            return None
        if res["total_cards"] > 1:
            get_logger().error("Duplicated cards found!")
            return None
        return res["data"][0]


scryfall_client = ScryfallClient()
