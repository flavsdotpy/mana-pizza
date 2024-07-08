from mana_pizza.commons.mtg import ColorCombinations, LandSetMetaclass, LandTags


class GenericTripleLands(metaclass=LandSetMetaclass):
    lands = {
        "Mardu Tri-land": ColorCombinations.MARDU,
        "Abzan Tri-land": ColorCombinations.ABZAN,
        "Sultai Tri-land": ColorCombinations.SULTAI,
        "Temur Tri-land": ColorCombinations.TEMUR,
        "Jeskai Tri-land": ColorCombinations.JESKAI,
        "Bant Tri-land": ColorCombinations.BANT,
        "Esper Tri-land": ColorCombinations.ESPER,
        "Grixis Tri-land": ColorCombinations.GRIXIS,
        "Jund Tri-land": ColorCombinations.JUND,
        "Naya Tri-land": ColorCombinations.NAYA,
    }
    generic = True


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
