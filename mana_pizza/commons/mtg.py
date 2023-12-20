from mana_pizza.commons.scryfall import scryfall_client


class ManaColors:
    WHITE = "W"
    BLUE = "U"
    BLACK = "B"
    RED = "R"
    GREEN = "G"


class Land:

    def __init__(self, name, colors,  tags, specific_edition=None):
        self.name = name
        self.colors = colors
        self.tags = tags
        self.specific_edition = specific_edition
        self._load_price()

    def _load_price(self):
        card = scryfall_client.get_card_by_name(self.name, self.specific_edition)
        self.price = card["prices"]["usd"]

    def can_be_fetched(self) -> bool:
        return LandTags.FETCHABLE in self.tags

    def can_etb_untapped(self) -> bool:
        return LandTags.ENTERS_UNTAPPED in self.tags

    def is_artifact(self) -> bool:
        return LandTags.ARTIFACT in self.tags

    def is_guildgate(self) -> bool:
        return LandTags.GATE in self.tags

    def is_snow(self) -> bool:
        return LandTags.SNOW in self.tags

    def does_become_creature(self) -> bool:
        return LandTags.BECOMES_CREATURE in self.tags

    def does_bounce(self) -> bool:
        return LandTags.BOUNCE in self.tags

    def does_gain_life(self) -> bool:
        return LandTags.LIFEGAIN in self.tags

    def does_scry(self) -> bool:
        return LandTags.SCRY in self.tags

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name} | Colors: {''.join(self.colors)} | Priority: {self.priority} | Tags: {','.join(self.tags)}"


class LandTags:
    # Features
    FETCHABLE = "fetchable"
    ENTERS_UNTAPPED = "enters_untapped"
    # Types
    ARTIFACT = "artifact"
    GATE = "gate"
    SNOW = "snow"
    # Abilities
    BECOMES_CREATURE = "manland"
    BOUNCE = "bounce"
    LIFEGAIN = "lifegain"
    SCRY = "scry"
    MANA_SINK = "mana_sink_ability"


class Editions:
    THIRD_EDITION = "3ed"


class ColorCombinations:
    FIVE_COLOR = {ManaColors.WHITE, ManaColors.BLUE, ManaColors.BLACK, ManaColors.RED, ManaColors.GREEN}
    SANS_RED = {ManaColors.WHITE, ManaColors.BLUE, ManaColors.BLACK, ManaColors.GREEN}
    SANS_GREEN = {ManaColors.WHITE, ManaColors.BLUE, ManaColors.BLACK, ManaColors.RED}
    SANS_BLUE = {ManaColors.WHITE, ManaColors.BLACK, ManaColors.RED, ManaColors.GREEN}
    SANS_BLACK = {ManaColors.WHITE, ManaColors.BLUE, ManaColors.RED, ManaColors.GREEN}
    SANS_WHITE = {ManaColors.BLUE, ManaColors.BLACK, ManaColors.RED, ManaColors.GREEN}
    BANT = {ManaColors.WHITE, ManaColors.BLUE, ManaColors.GREEN}
    ESPER = {ManaColors.WHITE, ManaColors.BLUE, ManaColors.BLACK}
    GRIXIS = {ManaColors.BLUE, ManaColors.BLACK, ManaColors.RED}
    JUND = {ManaColors.BLACK, ManaColors.RED, ManaColors.GREEN}
    NAYA = {ManaColors.RED, ManaColors.GREEN, ManaColors.WHITE}
    ABZAN = {ManaColors.WHITE, ManaColors.BLACK, ManaColors.GREEN}
    JESKAI = {ManaColors.WHITE, ManaColors.BLUE, ManaColors.RED}
    SULTAI = {ManaColors.BLUE, ManaColors.BLACK, ManaColors.GREEN}
    MARDU = {ManaColors.WHITE, ManaColors.BLACK, ManaColors.RED}
    TEMUR = {ManaColors.BLUE, ManaColors.RED, ManaColors.GREEN}
    AZORIUS = {ManaColors.WHITE, ManaColors.BLUE}
    ORZHOV = {ManaColors.WHITE, ManaColors.BLACK}
    BOROS = {ManaColors.RED, ManaColors.WHITE}
    SELESNYA = {ManaColors.WHITE, ManaColors.GREEN}
    DIMIR = {ManaColors.BLUE, ManaColors.BLACK}
    IZZET = {ManaColors.BLUE, ManaColors.RED}
    RAKDOS = {ManaColors.BLACK, ManaColors.RED}
    GOLGARI = {ManaColors.BLACK, ManaColors.GREEN}
    GRUUL = {ManaColors.RED, ManaColors.GREEN}
    SIMIC = {ManaColors.BLUE, ManaColors.GREEN}
    MONO_WHITE = {ManaColors.WHITE}
    MONO_BLUE = {ManaColors.BLUE}
    MONO_GREEN = {ManaColors.BLACK}
    MONO_RED = {ManaColors.RED}
    MONO_BLACK = {ManaColors.GREEN}
    COLORLESS = {}


class LandSetMetaclass(type):

    def get(cls):
        if not hasattr(cls, '_initialized'):
            cls._initialized = True
            cls._lands = []
            cls._load_lands()
        return cls._lands

    def get_for_combination(cls, combination: set):
        all = cls.get()
        return [l for l in all if combination.issubset(l.colors)]

    def _load_lands(cls):
        _REQUIRED_ATTRS = {"lands", "tags"}
        for attr in _REQUIRED_ATTRS:
            if not hasattr(cls, attr):
                raise Exception(f"Please define `{attr}` class atribute")
        for land, colors in cls.__getattribute__(cls, "lands").items():
            cls._lands.append(Land(
                name=land,
                colors=colors,
                tags=getattr(cls, "tags"),
                specific_edition=getattr(cls, "specific_edition", None),
            ))
