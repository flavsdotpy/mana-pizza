from collections import Counter
from math import ceil, inf

from mana_pizza.commons.db import local_db
from mana_pizza.commons.log import get_logger
from mana_pizza.commons.mtg import Land, ManaColors
from mana_pizza.commons.scryfall import scryfall_client
from mana_pizza.lands.basic import BasicLands
from mana_pizza.lands.dual import PICK_PRIORITY as DUAL_PICK_PRIORITY
from mana_pizza.lands.fetch import PICK_PRIORITY as FETCH_PICK_PRIORITY, ColoredFetchLands
from mana_pizza.lands.rainbow import RainbowLands
from mana_pizza.lands.tri import PICK_PRIORITY as TRI_PICK_PRIORITY



class ManaSmootherConf:
    TRI_LAND_SLOTS = {
        3: 2,
        4: 2,
        5: 3
    }
    FETCH_LANDS_SLOTS = {
        2: 1,
        3: 2,
        4: 2,
        5: 3
    }
    BASIC_LANDS_SLOTS = {
        2: 20,
        3: 13,
        4: 8,
        5: 8
    }


class ManaSmootherHelper:
    __loaded = False
    __mana_symbols = None

    @classmethod
    def load(cls):
        if not cls.__loaded:
            get_logger().info("Loading smoother resources...")
            local_db.load()
            cls.__load_lands()
            cls.__load_mana_symbols()
            cls.__loaded = True

    @classmethod
    def __load_lands(self):
        get_logger().info("Setting up land base...")
        BasicLands.plains()
        RainbowLands.command_tower()
        for fetch_cls in FETCH_PICK_PRIORITY.values():
            fetch_cls.get()
        for dual_cls in DUAL_PICK_PRIORITY.values():
            dual_cls.get()
        for tri_cls in TRI_PICK_PRIORITY.values():
            tri_cls.get()

    @classmethod
    def __load_mana_symbols(self):
        get_logger().info("Setting up mana symbols...")
        self.__mana_symbols = {
            ManaColors.WHITE: [],
            ManaColors.RED: [],
            ManaColors.GREEN: [],
            ManaColors.BLACK: [],
            ManaColors.BLUE: [],
        }
        all_mtg_symbols = scryfall_client.fetch_symbology()
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

    @classmethod
    def mana_symbols(cls) -> dict:
        return cls.__mana_symbols


class ManaPizzaLandSmoother:

    def __init__(self, commander: str, parameters: dict = {}):
        self.errors = list()
        self.commander = commander
        self.card_price_limit = parameters.get("card_price_limit", inf)
        self.__load_commander_info()

    def __load_commander_info(self):
        get_logger().debug(f"Loading info. Commander: {self.commander}")
        try:
            card = local_db.get_card_by_name(self.commander)
            self.deck_color_identity = set(card["color_identity"])
        except:
            self.errors.append("Commander not found!")

    def __get_pip_count_for_card(self, card_obj: dict):
        get_logger().debug(f"Calculating mana statistics for: {card_obj['name']}")
        card_pip_count = {
            ManaColors.WHITE: 0,
            ManaColors.RED: 0,
            ManaColors.GREEN: 0,
            ManaColors.BLACK: 0,
            ManaColors.BLUE: 0,
        }
        for color in card_pip_count:
            for symbol in ManaSmootherHelper.mana_symbols()[color]:
                pips = card_obj["mana_cost"].count(symbol["symbol"])
                card_pip_count[color] += symbol["pip_value"] * pips
        return card_pip_count

    def __calc_mana_stats(self):
        get_logger().debug("Calculating cards list mana statistics...")
        self.pip_count = {}
        self.total_cmc = 0
        for card_name in self.card_list:
            try:
                card_obj = local_db.get_card_by_name(card_name)
            except:
                self.errors.append(f"Card {card_name} not found!")
                continue
            self.total_cmc += card_obj["cmc"]
            card_pips = self.__get_pip_count_for_card(card_obj)
            self.pip_count = {
                k: self.pip_count.get(k, 0) + card_pips.get(k, 0)
                for k in set(self.pip_count) | set(card_pips)
            }
        self.total_pips = sum(self.pip_count.values())
        self.color_proportions = dict(sorted(
            {
                color: round(color_pips / self.total_pips, 2)
                for color, color_pips in self.pip_count.items()
            }.items(), key=lambda item: item[1], reverse=True
        ))
        get_logger().debug(f"Total CMC: {self.total_cmc}")
        get_logger().debug(f"CMC average with lands: {self.total_cmc/100}")
        get_logger().debug(f"CMC average w/o lands: {self.total_cmc/len(self.card_list)}")
        get_logger().debug(f"Pip count:")
        for c, count in self.pip_count.items():
            get_logger().debug(f"{c}: {count}")

    def __select_land(self, land: Land):
        if not land:
            return False
        if land.price > self.card_price_limit:
            return False
        self.selected_lands.append(land)
        get_logger().debug(f"Selected {land.name}")
        return True

    def __get_basic_lands(self):
        get_logger().debug("Selecting basic lands...")
        before = len(self.selected_lands)
        total_pips = sum(self.pip_count.values())
        for color in self.deck_color_identity:
            color_percentage = self.pip_count[color] / total_pips
            color_land_count = color_percentage * ManaSmootherConf.BASIC_LANDS_SLOTS[len(self.deck_color_identity)]
            if color_land_count:
                basic_land = BasicLands.get_by_color(color)
                for _ in range(int(round(color_land_count))):
                    self.__select_land(basic_land)
        get_logger().debug(f"Selected {len(self.selected_lands) - before} basic lands!")

    def __calc_dual_land_pairs(
        self, color_proportions: dict, num_lands: int, pairs: list[set] = None, has_major_color: bool = False
    ) -> list[list]:
        pairs = [set() for _ in range(num_lands)] if not pairs else pairs

        num_colors = 2 * num_lands
        color_proportions = dict(sorted(color_proportions.items(), key=lambda item: item[1], reverse=True))
        sum_proportions = sum(color_proportions.values())

        if len(self.deck_color_identity) == 2:
            return [tuple(self.deck_color_identity) for _ in range(num_lands)]
        if not(sum_proportions):
            return pairs

        cur_color = list(color_proportions.keys())[0]
        cur_color_proportion = color_proportions.pop(cur_color)
        cur_color_lands = ceil(cur_color_proportion / sum_proportions * num_lands) \
                        if has_major_color \
                        else ceil(cur_color_proportion * num_colors)

        count = 0
        if any(not pair for pair in pairs):
            for pair in pairs:
                if len(pair) < 1:
                    pair.add(cur_color)
                    count += 1
                if count >= cur_color_lands:
                    break
        for pair in pairs:
            if len(pair) < 2 and cur_color not in pair:
                pair.add(cur_color)
                count += 1
            if count >= cur_color_lands:
                break

        if not color_proportions:
            return pairs

        if not has_major_color and cur_color_proportion >= .5:
            has_major_color = True

        return self.__calc_dual_land_pairs(color_proportions, num_lands, pairs, has_major_color)

    def __get_dual_lands(self):
        get_logger().debug("Selecting dual lands...")
        before = len(self.selected_lands)
        num_dual_lands = self.lands_count - len(self.selected_lands)
        color_proportions = self.color_proportions.copy()
        dual_land_pairs = self.__calc_dual_land_pairs(color_proportions, num_dual_lands)
        pairs_count = dict(Counter([tuple(pair) for pair in dual_land_pairs]))
        for dual_land_class in DUAL_PICK_PRIORITY.values():
            for color_pair in pairs_count:
                if not pairs_count[color_pair]:
                    continue
                land = dual_land_class.get_for_combination(color_pair)
                if self.__select_land(land):
                    pairs_count[color_pair] -= 1
            if not sum(pairs_count.values()):
                break
        get_logger().debug(f"Selected {len(self.selected_lands) - before} dual lands!")


    def __get_tri_lands(self):
        get_logger().debug("Selecting tri lands...")
        if len(self.deck_color_identity) < 3:
            get_logger().debug("Skipping tri lands for decks with 2 or less colors...")
            return

        before = len(self.selected_lands)
        slots = ManaSmootherConf.TRI_LAND_SLOTS[len(self.deck_color_identity)]
        if len(self.deck_color_identity) == 3:
            trio_color_combinations = [self.deck_color_identity]
        elif len(self.deck_color_identity) == 4:
            colors = list(self.color_proportions.keys())
            trio_color_combinations = [
                (colors[0], colors[1], colors[2]), (colors[0], colors[1], colors[3])
            ]
        elif len(self.deck_color_identity) == 5:
            colors = list(self.color_proportions.keys())
            trio_color_combinations = [
                (colors[0], colors[1], colors[2]),
                (colors[0], colors[1], colors[3]),
                (colors[0], colors[1], colors[4])
            ]
        for tri_land_class in TRI_PICK_PRIORITY.values():
            for color_trio in trio_color_combinations:
                if not slots:
                    break
                land = tri_land_class.get_for_combination(color_trio)
                if self.__select_land(land):
                    slots -= 1
        get_logger().debug(f"Selected {len(self.selected_lands) - before} tri lands!")

    def __get_fetch_lands(self):
        get_logger().debug("Selecting fetch lands...")
        before = len(self.selected_lands)
        slots = ManaSmootherConf.FETCH_LANDS_SLOTS[len(self.deck_color_identity)]
        if len(self.deck_color_identity) == 2:
            dual_color_pairs = [self.deck_color_identity]
        elif len(self.deck_color_identity) == 3:
            colors = list(self.color_proportions.keys())
            dual_color_pairs = [(colors[0], colors[1]), (colors[0], colors[2])]
        elif len(self.deck_color_identity) in [4, 5]:
            colors = list(self.color_proportions.keys())
            dual_color_pairs = [
                (colors[0], colors[1]), (colors[0], colors[2]), (colors[0], colors[3])
            ]
        for color_pair in dual_color_pairs:
            if not slots:
                break
            land = ColoredFetchLands.get_for_combination(color_pair)
            if self.__select_land(land):
                slots -= 1
        for fetch_land_class in FETCH_PICK_PRIORITY.values():
            for land in fetch_land_class.get():
                if not slots:
                    break
                if self.__select_land(land):
                    slots -= 1
        get_logger().debug(f"Selected {len(self.selected_lands) - before} fetch lands!")

    def __get_rainbow_lands(self):
        get_logger().debug("Selecting rainbow lands...")
        before = len(self.selected_lands)
        self.__select_land(RainbowLands.command_tower())
        if len(self.deck_color_identity) > 2:
            self.__select_land(RainbowLands.exotic_orchard())
        if len(self.deck_color_identity) > 3:
            self.__select_land(RainbowLands.city_of_brass())
        if len(self.deck_color_identity) > 3:
            self.__select_land(RainbowLands.mana_confluence())
        get_logger().debug(f"Selected {len(self.selected_lands) - before} rainbow lands!")

    def smooth_mana(self, card_list: list[str]):
        if len(self.deck_color_identity) < 2:
            self.errors.append("Mana pizza does not work for mono-color decks!")

        self.card_list = [c for c in card_list if c]
        self.lands_count = 99 - len(card_list)
        self.selected_lands = list()
        self.__calc_mana_stats()

        if self.errors:
            return list()

        self.__get_basic_lands()
        self.__get_rainbow_lands()
        self.__get_fetch_lands()
        self.__get_tri_lands()
        self.__get_dual_lands()
        return self.selected_lands
