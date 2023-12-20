from mana_pizza.commons.mtg import ColorCombinations, Land, LandTags


class RainbowLands:
    _loaded = False

    _command_tower = None
    _exotic_orchard = None
    _mana_confluence = None
    _city_of_brass = None

    @classmethod
    def _get(cls, attr):
        if not cls._loaded:
            cls._load()
        return getattr(cls, attr)

    @classmethod
    def _load(cls):
        cls._command_tower = Land(
            name="Command Tower", colors=ColorCombinations.FIVE_COLOR, tags={LandTags.ENTERS_UNTAPPED})
        cls._exotic_orchard = Land(
            name="Exotic Orchard", colors=ColorCombinations.FIVE_COLOR, tags={LandTags.ENTERS_UNTAPPED})
        cls._mana_confluence = Land(
            name="Mana Confluence", colors=ColorCombinations.FIVE_COLOR, tags={LandTags.ENTERS_UNTAPPED})
        cls._city_of_brass = Land(
            name="City of Brass", colors=ColorCombinations.FIVE_COLOR, tags={LandTags.ENTERS_UNTAPPED})
        cls._loaded = True

    @classmethod
    def command_tower(cls):
        return cls._get("_command_tower")

    @classmethod
    def exotic_orchard(cls):
        return cls._get("_exotic_orchard")

    @classmethod
    def mana_confluence(cls):
        return cls._get("_mana_confluence")

    @classmethod
    def city_of_brass(cls):
        return cls._get("_city_of_brass")
