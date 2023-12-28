from mana_pizza.commons.mtg import ColorCombinations, Land, LandTags


class ColorlessUtilityLands:
    _loaded = False

    _reliquary_tower = None
    _rogues_passage = None

    def _get(cls, attr) -> Land:
        if not cls._loaded:
            cls._load()
        return getattr(cls, attr)

    def _load(cls):
        cls._reliquary_tower = Land(
            "Reliquary Tower", colors=ColorCombinations.COLORLESS, tags={LandTags.ENTERS_UNTAPPED})
        cls._rogues_passage = Land(
            "Rogue's Passage", colors=ColorCombinations.COLORLESS, tags={LandTags.ENTERS_UNTAPPED})
        cls._loaded = True

    @classmethod
    def reliquary_tower(cls) -> Land:
        return cls._get("_reliquary_tower")

    @classmethod
    def rogues_passage(cls) -> Land:
        return cls._get("_rogues_passage")

