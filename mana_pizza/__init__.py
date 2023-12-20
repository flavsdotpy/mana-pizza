from mana_pizza.commons.mtg import ManaColors
from mana_pizza.commons.scryfall import scryfall_client
from mana_pizza.lands.basic import BasicLands
from mana_pizza.lands.dual import PICK_PRIORITY as DUAL_PICK_PRIORITY
from mana_pizza.lands.fetch import PICK_PRIORITY as FETCH_PICK_PRIORITY
from mana_pizza.lands.rainbow import RainbowLands
from mana_pizza.lands.tri import PICK_PRIORITY as TRI_PICK_PRIORITY



class ManaSmootherConf:
    BASIC_LANDS_RATIO = {
        2: 22/35,
        3: 14/35,
        4: 9/35,
        5: 9/35
    }


class ManaPizzaLandSmoother:

    __loaded = False
    __mana_symbols = None

    def __init__(self, commander: str):
        self.commander = commander
        self.__load()

    def __load(self):
        if not self.__loaded:
            self.__load_mana_symbols()
            self.__load_lands()
            self.__load_commander_info()

    def __load_mana_symbols(self):
        print("Setting up mana symbols...")
        self.__mana_symbols = {
            ManaColors.WHITE: [],
            ManaColors.RED: [],
            ManaColors.GREEN: [],
            ManaColors.BLACK: [],
            ManaColors.BLUE: [],
        }
        all_mtg_symbols = scryfall_client.list_symbology()
        mana_symbols = [
            s for s in all_mtg_symbols
            if s["represents_mana"]
        ]
        for symbol in mana_symbols:
            for color in symbol["colors"]:
                self.__mana_symbols[color].append({
                    "symbol": symbol["symbol"],
                    "pip_value": symbol["cmc"] / len(symbol["colors"])
                })

    def __load_commander_info(self):
        print(f"Loading info. Commander: {self.commander}")
        card = scryfall_client.get_card_by_name(self.commander)
        self.color_identity = card["color_identity"]


    def __load_lands(self):
        BasicLands.plains()
        RainbowLands.command_tower()
        for fetch_cls in FETCH_PICK_PRIORITY.values():
            fetch_cls.get()
        for dual_cls in DUAL_PICK_PRIORITY.values():
            dual_cls.get()
        for tri_cls in TRI_PICK_PRIORITY.values():
            tri_cls.get()


    def __get_pip_count_for_card(self, card):
        print("Calculating cards list mana statistics...")
        card_pip_count = {
            ManaColors.WHITE: 0,
            ManaColors.RED: 0,
            ManaColors.GREEN: 0,
            ManaColors.BLACK: 0,
            ManaColors.BLUE: 0,
        }
        for color in card_pip_count:
            for symbol in self.__mana_symbols[color]:
                pips = card["mana_cost"].count(symbol["symbol"])
                card_pip_count[color] += symbol["pip_value"] * pips
        return card_pip_count

    def __calc_mana_stats(self):
        print("Calculating cards list mana statistics...")
        self.pip_count = {}
        self.total_cmc = 0
        for card_name in self.card_list:
            card = scryfall_client.get_card_by_name(card_name)
            self.total_cmc += card["cmc"]
            card_pips = self.__get_pip_count_for_card(card)
            self.pip_count = {
                k: self.pip_count.get(k, 0) + card_pips.get(k, 0)
                for k in set(self.pip_count) | set(card_pips)
            }
        print(f"Total CMC: {self.total_cmc}")
        print(f"CMC average with lands: {self.total_cmc/100}")
        print(f"CMC average w/o lands: {self.total_cmc/len(self.card_list)}")
        print(f"Pip count:")
        for c, count in self.pip_count.items():
            print(f"{c}: {count}")

    def __get_basic_lands(self):
        print("Selecting basic lands for the deck...")
        total_pips = sum(self.pip_count.values())
        for color in self.color_identity:
            color_percentage = self.pip_count[color] / total_pips
            color_land_percentage = color_percentage * ManaSmootherConf.BASIC_LANDS_RATIO[len(self.color_identity)]
            if color_land_percentage:
                basic_land = BasicLands.get_by_color(color)
                self.selected_lands.extend([
                    basic_land.name for _ in range(int(round(color_land_percentage * self.lands_count)))
                ])

    def smooth_mana(self, card_list: list[str]):
        self.card_list = card_list
        self.lands_count = 99 - len(card_list)
        self.selected_lands = list()
        self.__calc_mana_stats()
        self.__get_basic_lands()
        print()
