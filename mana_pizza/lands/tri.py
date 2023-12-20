from mana_pizza.commons.mtg import ColorCombinations, LandSetMetaclass, LandTags


class TripleLands(metaclass=LandSetMetaclass):
    lands = {
        "Seaside Citadel": ColorCombinations.BANT,
        "Arcane Sanctum": ColorCombinations.ESPER,
        "Crumbling Necropolis": ColorCombinations.GRIXIS,
        "Savage Lands": ColorCombinations.JUND,
        "Jungle Shrine": ColorCombinations.NAYA,
        "Nomad Outpost": ColorCombinations.MARDU,
        "Sandsteppe Citadel": ColorCombinations.ABZAN,
        "Opulent Palace": ColorCombinations.SULTAI,
        "Frontier Bivouac": ColorCombinations.TEMUR,
        "Mystic Monastery": ColorCombinations.JESKAI,
    }
    tags = {}


class Triomes(metaclass=LandSetMetaclass):
    lands = {
        "Savai Triome": ColorCombinations.MARDU,
        "Indatha Triome": ColorCombinations.ABZAN,
        "Zagoth Triome": ColorCombinations.SULTAI,
        "Ketria Triome": ColorCombinations.TEMUR,
        "Raugrin Triome": ColorCombinations.JESKAI,
        "Spara's Headquarters": ColorCombinations.BANT,
        "Raffine's Tower": ColorCombinations.ESPER,
        "Xander's Lounge": ColorCombinations.GRIXIS,
        "Ziatora's Proving Ground": ColorCombinations.JUND,
        "Jetmir's Garden": ColorCombinations.NAYA,
    }
    tags = {LandTags.FETCHABLE, LandTags.MANA_SINK}

PICK_PRIORITY = {
    0: Triomes,
    10: TripleLands,
}
