from mana_pizza.commons.mtg import ColorCombinations, Land, LandTags, ManaColors


class BasicLands:
    _loaded = False

    _forest = None
    _plains = None
    _swamp = None
    _island = None
    _mountain = None

    @classmethod
    def _get(cls, attr):
        if not cls._loaded:
            cls._load()
        return getattr(cls, attr)

    @classmethod
    def _load(cls):
        cls._forest = Land(
            "Forest", colors=ColorCombinations.MONO_GREEN, tags={LandTags.ENTERS_UNTAPPED, LandTags.FETCHABLE})
        cls._plains = Land(
            "Plains", colors=ColorCombinations.MONO_WHITE, tags={LandTags.ENTERS_UNTAPPED, LandTags.FETCHABLE})
        cls._swamp = Land(
            "Swamp", colors=ColorCombinations.MONO_BLACK, tags={LandTags.ENTERS_UNTAPPED, LandTags.FETCHABLE})
        cls._island = Land(
            "Island", colors=ColorCombinations.MONO_BLUE, tags={LandTags.ENTERS_UNTAPPED, LandTags.FETCHABLE})
        cls._mountain = Land(
            "Mountain", colors=ColorCombinations.MONO_RED, tags={LandTags.ENTERS_UNTAPPED, LandTags.FETCHABLE})
        cls._loaded = True

    @classmethod
    def get_by_color(cls, color):
        return {
            ManaColors.WHITE: cls.plains,
            ManaColors.BLUE: cls.island,
            ManaColors.GREEN: cls.forest,
            ManaColors.BLACK: cls.swamp,
            ManaColors.RED: cls.mountain,
        }[color]()

    @classmethod
    def forest(cls):
        return cls._get("_forest")

    @classmethod
    def plains(cls):
        return cls._get("_plains")

    @classmethod
    def swamp(cls):
        return cls._get("_swamp")

    @classmethod
    def island(cls):
        return cls._get("_island")

    @classmethod
    def mountain(cls):
        return cls._get("_mountain")

