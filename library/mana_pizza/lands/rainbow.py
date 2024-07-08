from mana_pizza.commons.mtg import ColorCombinations, Land, LandTags


class RainbowLands:
    _loaded = False

    _command_tower = None
    _exotic_orchard = None
    _mana_confluence = None
    _city_of_brass = None
    _generic_rainbow_land = Land("Rainbow Land", ColorCombinations.FIVE_COLOR, tags=set(), is_generic=True)

    @classmethod
    def _get(cls, attr) -> Land:
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
    def command_tower(cls) -> Land:
        return cls._get("_command_tower")

    @classmethod
    def exotic_orchard(cls) -> Land:
        return cls._get("_exotic_orchard")

    @classmethod
    def mana_confluence(cls) -> Land:
        return cls._get("_mana_confluence")

    @classmethod
    def city_of_brass(cls) -> Land:
        return cls._get("_city_of_brass")
    
    @classmethod
    def generic_rainbow_land(cls) -> Land:
        return cls._get("_generic_rainbow_land")
