from mana_pizza.commons.mtg import ColorCombinations, LandSetMetaclass, LandTags


class ColoredFetchLands(metaclass=LandSetMetaclass):
    lands = {
        "Flooded Strand": ColorCombinations.AZORIUS,
        "Polluted Delta": ColorCombinations.DIMIR,
        "Bloodstained Mire": ColorCombinations.RAKDOS,
        "Wooded Foothills": ColorCombinations.GRUUL,
        "Windswept Heath": ColorCombinations.SELESNYA,
        "Marsh Flats": ColorCombinations.ORZHOV,
        "Scalding Tarn": ColorCombinations.IZZET,
        "Verdant Catacombs": ColorCombinations.GOLGARI,
        "Arid Mesa": ColorCombinations.BOROS,
        "Misty Rainforest": ColorCombinations.SIMIC,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class BasicFetchLands(metaclass=LandSetMetaclass):
    lands = {
        "Terramorphic Expanse": ColorCombinations.FIVE_COLOR,
        "Evolving Wilds": ColorCombinations.FIVE_COLOR
    }
    tags = {}


class OtherFechLands(metaclass=LandSetMetaclass):
    lands = {
        "Fabled Passage": ColorCombinations.FIVE_COLOR,
        "Prismatic Vista": ColorCombinations.FIVE_COLOR
    }
    tags = {LandTags.ENTERS_UNTAPPED}


PICK_PRIORITY = {
    1: OtherFechLands,
    10: BasicFetchLands
}
