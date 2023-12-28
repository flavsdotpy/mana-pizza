from mana_pizza.commons.mtg import ColorCombinations, Editions, LandSetMetaclass, LandTags


class BicycleLands(metaclass=LandSetMetaclass):
    lands = {
        "Canyon Slough": ColorCombinations.RAKDOS,
        "Fetid Pools": ColorCombinations.DIMIR,
        "Irrigated Farmland": ColorCombinations.AZORIUS,
        "Scattered Groves": ColorCombinations.SELESNYA,
        "Sheltered Thicket": ColorCombinations.GRUUL,
    }
    tags = {LandTags.FETCHABLE, LandTags.MANA_SINK}


class BounceLands(metaclass=LandSetMetaclass):
    lands = {
        "Azorius Chancery": ColorCombinations.AZORIUS,
        "Boros Garrison": ColorCombinations.BOROS,
        "Dimir Aqueduct": ColorCombinations.DIMIR,
        "Golgari Rot Farm": ColorCombinations.GOLGARI,
        "Gruul Turf": ColorCombinations.GRUUL,
        "Izzet Boilerworks": ColorCombinations.IZZET,
        "Orzhov Basilica": ColorCombinations.ORZHOV,
        "Rakdos Carnarium": ColorCombinations.RAKDOS,
        "Selesnya Sanctuary": ColorCombinations.SELESNYA,
        "Simic Growth Chamber": ColorCombinations.SIMIC,
    }
    tags = {LandTags.BOUNCE}


class BoundLands(metaclass=LandSetMetaclass):
    lands = {
        "Bountiful Promenade": ColorCombinations.SELESNYA,
        "Luxury Suite": ColorCombinations.RAKDOS,
        "Morphic Pool": ColorCombinations.DIMIR,
        "Rejuvenating Springs": ColorCombinations.SIMIC,
        "Sea of Clouds": ColorCombinations.AZORIUS,
        "Spectator Seating": ColorCombinations.BOROS,
        "Spire Garden": ColorCombinations.GRUUL,
        "Training Center": ColorCombinations.IZZET,
        "Undergrowth Stadium": ColorCombinations.GOLGARI,
        "Vault of Champions": ColorCombinations.ORZHOV,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class CheckLands(metaclass=LandSetMetaclass):
    lands = {
        "Clifftop Retreat": ColorCombinations.BOROS,
        "Dragonskull Summit": ColorCombinations.RAKDOS,
        "Drowned Catacomb": ColorCombinations.DIMIR,
        "Glacial Fortress": ColorCombinations.AZORIUS,
        "Hinterland Harbor": ColorCombinations.SIMIC,
        "Isolated Chapel": ColorCombinations.ORZHOV,
        "Rootbound Crag": ColorCombinations.GRUUL,
        "Sulfur Falls": ColorCombinations.IZZET,
        "Sunpetal Grove": ColorCombinations.SELESNYA,
        "Woodland Cemetery": ColorCombinations.GOLGARI,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class FilterLands(metaclass=LandSetMetaclass):
    lands = {
        "Flooded Grove": ColorCombinations.SIMIC,
        "Fire-Lit Thicket": ColorCombinations.GRUUL,
        "Graven Cairns": ColorCombinations.RAKDOS,
        "Sunken Ruins": ColorCombinations.DIMIR,
        "Wooded Bastion": ColorCombinations.SELESNYA,
        "Fetid Heath": ColorCombinations.ORZHOV,
        "Mystic Gate": ColorCombinations.AZORIUS,
        "Cascade Bluffs": ColorCombinations.IZZET,
        "Rugged Prairie": ColorCombinations.BOROS,
        "Twilight Mire": ColorCombinations.GOLGARI,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class OldFilterLands(metaclass=LandSetMetaclass):
    lands = {
        "Skycloud Expanse": ColorCombinations.AZORIUS,
        "Darkwater Catacombs": ColorCombinations.DIMIR,
        "Shadowblood Ridge": ColorCombinations.RAKDOS,
        "Mossfire Valley": ColorCombinations.GRUUL,
        "Sungrass Prairie": ColorCombinations.SELESNYA,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class GainLands(metaclass=LandSetMetaclass):
    lands = {
        "Blossoming Sands": ColorCombinations.SELESNYA,
        "Bloodfell Caves": ColorCombinations.RAKDOS,
        "Dismal Backwater": ColorCombinations.DIMIR,
        "Jungle Hollow": ColorCombinations.GOLGARI,
        "Rugged Highlands": ColorCombinations.GRUUL,
        "Scoured Barrens": ColorCombinations.ORZHOV,
        "Swiftwater Cliffs": ColorCombinations.IZZET,
        "Thornwood Falls": ColorCombinations.SIMIC,
        "Tranquil Cove": ColorCombinations.AZORIUS,
        "Wind-Scarred Crag": ColorCombinations.BOROS,
    }
    tags = {LandTags.LIFEGAIN}


class GainLandsOld(metaclass=LandSetMetaclass):
    lands = {
        "Akoum Refuge": ColorCombinations.RAKDOS,
        "Graypelt Refuge": ColorCombinations.SELESNYA,
        "Jwar Isle Refuge": ColorCombinations.DIMIR,
        "Kazandu Refuge": ColorCombinations.GRUUL,
        "Sejiri Refuge": ColorCombinations.AZORIUS,
    }
    tags = {LandTags.LIFEGAIN}


class GuildGates(metaclass=LandSetMetaclass):
    lands = {
        "Azorius Guildgate": ColorCombinations.AZORIUS,
        "Boros Guildgate": ColorCombinations.BOROS,
        "Dimir Guildgate": ColorCombinations.DIMIR,
        "Golgari Guildgate": ColorCombinations.GOLGARI,
        "Gruul Guildgate": ColorCombinations.GRUUL,
        "Izzet Guildgate": ColorCombinations.IZZET,
        "Orzhov Guildgate": ColorCombinations.ORZHOV,
        "Rakdos Guildgate": ColorCombinations.RAKDOS,
        "Selesnya Guildgate": ColorCombinations.SELESNYA,
        "Simic Guildgate": ColorCombinations.SIMIC,
    }
    tags = {LandTags.GATE}


class HorizonLands(metaclass=LandSetMetaclass):
    lands = {
        "Horizon Canopy": ColorCombinations.SELESNYA,
        "Silent Clearing": ColorCombinations.ORZHOV,
        "Fiery Islet": ColorCombinations.IZZET,
        "Nurturing Peatland": ColorCombinations.GOLGARI,
        "Sunbaked Canyon": ColorCombinations.BOROS,
        "Waterlogged Grove": ColorCombinations.SIMIC,
    }
    tags = {LandTags.ENTERS_UNTAPPED, LandTags.MANA_SINK}


class OGDuals(metaclass=LandSetMetaclass):
    lands = {
        "Bayou": ColorCombinations.GOLGARI,
        "Badlands": ColorCombinations.RAKDOS,
        "Underground Sea": ColorCombinations.DIMIR,
        "Scrubland": ColorCombinations.ORZHOV,
        "Taiga": ColorCombinations.GRUUL,
        "Tropical Island": ColorCombinations.SIMIC,
        "Savannah": ColorCombinations.SELESNYA,
        "Volcanic Island": ColorCombinations.IZZET,
        "Plateau": ColorCombinations.BOROS,
        "Tundra": ColorCombinations.AZORIUS,
    }
    tags = {LandTags.ENTERS_UNTAPPED, LandTags.FETCHABLE}


class PainLands(metaclass=LandSetMetaclass):
    lands = {
        "Adarkar Wastes": ColorCombinations.AZORIUS,
        "Battlefield Forge": ColorCombinations.BOROS,
        "Brushland": ColorCombinations.SELESNYA,
        "Caves of Koilos": ColorCombinations.ORZHOV,
        "Karplusan Forest": ColorCombinations.GRUUL,
        "Llanowar Wastes": ColorCombinations.GOLGARI,
        "Shivan Reef": ColorCombinations.IZZET,
        "Sulfurous Springs": ColorCombinations.RAKDOS,
        "Underground River": ColorCombinations.DIMIR,
        "Yavimaya Coast": ColorCombinations.SIMIC,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class Pathways(metaclass=LandSetMetaclass):
    lands = {
        "Darkbore Pathway // Slitherbore Pathway": ColorCombinations.GOLGARI,
        "Blightstep Pathway // Searstep Pathway": ColorCombinations.RAKDOS,
        "Clearwater Pathway // Murkwater Pathway": ColorCombinations.DIMIR,
        "Brightclimb Pathway // Grimclimb Pathway": ColorCombinations.ORZHOV,
        "Cragcrown Pathway // Timbercrown Pathway": ColorCombinations.GRUUL,
        "Barkchannel Pathway // Tidechannel Pathway": ColorCombinations.SIMIC,
        "Branchloft Pathway // Boulderloft Pathway": ColorCombinations.SELESNYA,
        "Riverglide Pathway // Lavaglide Pathway": ColorCombinations.IZZET,
        "Needleverge Pathway // Pillarverge Pathway": ColorCombinations.BOROS,
        "Hengegate Pathway // Mistgate Pathway": ColorCombinations.AZORIUS,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class ShockLands(metaclass=LandSetMetaclass):
    lands = {
        "Overgrown Tomb": ColorCombinations.GOLGARI,
        "Blood Crypt": ColorCombinations.RAKDOS,
        "Watery Grave": ColorCombinations.DIMIR,
        "Godless Shrine": ColorCombinations.ORZHOV,
        "Stomping Ground": ColorCombinations.GRUUL,
        "Breeding Pool": ColorCombinations.SIMIC,
        "Temple Garden": ColorCombinations.SELESNYA,
        "Steam Vents": ColorCombinations.IZZET,
        "Sacred Foundry": ColorCombinations.BOROS,
        "Hallowed Fountain": ColorCombinations.AZORIUS,
    }
    tags = {LandTags.FETCHABLE, LandTags.ENTERS_UNTAPPED}


class SlowLands(metaclass=LandSetMetaclass):
    lands = {
        "Deathcap Glade": ColorCombinations.GOLGARI,
        "Haunted Ridge": ColorCombinations.RAKDOS,
        "Shipwreck Marsh": ColorCombinations.DIMIR,
        "Shattered Sanctum": ColorCombinations.ORZHOV,
        "Rockfall Vale": ColorCombinations.GRUUL,
        "Dreamroot Cascade": ColorCombinations.SIMIC,
        "Overgrown Farmland": ColorCombinations.SELESNYA,
        "Stormcarved Coast": ColorCombinations.IZZET,
        "Sundown Pass": ColorCombinations.BOROS,
        "Deserted Beach": ColorCombinations.AZORIUS,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class FastLands(metaclass=LandSetMetaclass):
    lands = {
        "Seachrome Coast": ColorCombinations.AZORIUS,
        "Darkslick Shores": ColorCombinations.DIMIR,
        "Blackcleave Cliffs": ColorCombinations.RAKDOS,
        "Copperline Gorge": ColorCombinations.GRUUL,
        "Razorverge Thicket": ColorCombinations.SELESNYA,
        "Concealed Courtyard": ColorCombinations.ORZHOV,
        "Spirebluff Canal": ColorCombinations.IZZET,
        "Blooming Marsh": ColorCombinations.GOLGARI,
        "Inspiring Vantage": ColorCombinations.BOROS,
        "Botanical Sanctum": ColorCombinations.SIMIC,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class TangoLands(metaclass=LandSetMetaclass):
    lands = {
        "Smoldering Marsh": ColorCombinations.RAKDOS,
        "Sunken Hollow": ColorCombinations.DIMIR,
        "Cinder Glade": ColorCombinations.GRUUL,
        "Canopy Vista": ColorCombinations.SELESNYA,
        "Prairie Stream": ColorCombinations.AZORIUS,
    }
    tags = {LandTags.FETCHABLE, LandTags.ENTERS_UNTAPPED}


class FetchableTapLands(metaclass=LandSetMetaclass):
    lands = {
        "Haunted Mire": ColorCombinations.GOLGARI,
        "Idyllic Beachfront": ColorCombinations.AZORIUS,
        "Contaminated Aquifer": ColorCombinations.DIMIR,
        "Geothermal Bog": ColorCombinations.RAKDOS,
        "Molten Tributary": ColorCombinations.IZZET,
        "Sunlit Marsh": ColorCombinations.ORZHOV,
        "Sacred Peaks": ColorCombinations.BOROS,
        "Wooded Ridgeline": ColorCombinations.GRUUL,
        "Tangled Islet": ColorCombinations.SIMIC,
        "Radiant Grove": ColorCombinations.SELESNYA,
    }
    tags = {LandTags.FETCHABLE}


class KhaldheimSnowLands(metaclass=LandSetMetaclass):
    lands = {
        "Arctic Treeline": ColorCombinations.SELESNYA,
        "Highland Forest": ColorCombinations.GRUUL,
        "Ice Tunnel": ColorCombinations.DIMIR,
        "Glacial Floodplain": ColorCombinations.AZORIUS,
        "Rimewood Falls": ColorCombinations.SIMIC,
        "Sulfurous Mire": ColorCombinations.RAKDOS,
        "Volatile Fjord": ColorCombinations.IZZET,
        "Woodland Chasm": ColorCombinations.GOLGARI,
        "Alpine Meadow": ColorCombinations.BOROS,
        "Snowfield Sinkhole": ColorCombinations.ORZHOV,
    }
    tags = {LandTags.FETCHABLE, LandTags.SNOW}


class Temples(metaclass=LandSetMetaclass):
    lands = {
        "Temple of Malady": ColorCombinations.GOLGARI,
        "Temple of Malice": ColorCombinations.RAKDOS,
        "Temple of Deceit": ColorCombinations.DIMIR,
        "Temple of Silence": ColorCombinations.ORZHOV,
        "Temple of Abandon": ColorCombinations.GRUUL,
        "Temple of Mystery": ColorCombinations.SIMIC,
        "Temple of Plenty": ColorCombinations.SELESNYA,
        "Temple of Epiphany": ColorCombinations.IZZET,
        "Temple of Triumph": ColorCombinations.BOROS,
        "Temple of Enlightenment": ColorCombinations.AZORIUS,
    }
    tags = {LandTags.SCRY}


class ColdsnapSnowLands(metaclass=LandSetMetaclass):
    lands = {
        "Arctic Flats": ColorCombinations.AZORIUS,
        "Boreal Shelf": ColorCombinations.DIMIR,
        "Frost Marsh": ColorCombinations.IZZET,
        "Highland Weald": ColorCombinations.GRUUL,
        "Tresserhorn Sinks": ColorCombinations.ORZHOV,
    }
    tags = {LandTags.SNOW}


class Bridges(metaclass=LandSetMetaclass):
    lands = {
        "Razortide Bridge": ColorCombinations.AZORIUS,
        "Mistvault Bridge": ColorCombinations.DIMIR,
        "Drossforge Bridge": ColorCombinations.RAKDOS,
        "Slagwoods Bridge": ColorCombinations.GRUUL,
        "Thornglint Bridge": ColorCombinations.SELESNYA,
        "Goldmire Bridge": ColorCombinations.ORZHOV,
        "Silverbluff Bridge": ColorCombinations.IZZET,
        "Darkmoss Bridge": ColorCombinations.GOLGARI,
        "Rustvale Bridge": ColorCombinations.BOROS,
        "Tanglepool Bridge": ColorCombinations.SIMIC,
    }
    tags = {LandTags.ARTIFACT}


class ManLands(metaclass=LandSetMetaclass):
    lands = {
        "Celestial Colonnade": ColorCombinations.AZORIUS,
        "Creeping Tar Pit": ColorCombinations.DIMIR,
        "Lavaclaw Reaches": ColorCombinations.RAKDOS,
        "Raging Ravine": ColorCombinations.GRUUL,
        "Stirring Wildwood": ColorCombinations.SELESNYA,
        "Shambling Vent": ColorCombinations.ORZHOV,
        "Wandering Fumarole": ColorCombinations.IZZET,
        "Hissing Quagmire": ColorCombinations.GOLGARI,
        "Needle Spires": ColorCombinations.BOROS,
        "Lumbering Falls": ColorCombinations.SIMIC,
    }
    tags = {LandTags.BECOMES_CREATURE}


class RestlessManLands(metaclass=LandSetMetaclass):
    lands = {
        "Restless Anchorage": ColorCombinations.AZORIUS,
        "Restless Reef": ColorCombinations.DIMIR,
        "Restless Vents": ColorCombinations.RAKDOS,
        "Restless Ridgeline": ColorCombinations.GRUUL,
        "Restless Prairie": ColorCombinations.SELESNYA,
        "Restless Fortress": ColorCombinations.ORZHOV,
        "Restless Spire": ColorCombinations.IZZET,
        "Restless Cottage": ColorCombinations.GOLGARI,
        "Restless Bivouac": ColorCombinations.BOROS,
        "Restless Vinestalk": ColorCombinations.SIMIC,
    }
    tags = {LandTags.BECOMES_CREATURE}


class RevealLands(metaclass=LandSetMetaclass):
    lands = {
        "Port Town": ColorCombinations.AZORIUS,
        "Choked Estuary": ColorCombinations.DIMIR,
        "Foreboding Ruins": ColorCombinations.RAKDOS,
        "Game Trail": ColorCombinations.GRUUL,
        "Fortified Village": ColorCombinations.SELESNYA,
        "Shineshadow Snarl": ColorCombinations.ORZHOV,
        "Frostboil Snarl": ColorCombinations.IZZET,
        "Necroblossom Snarl": ColorCombinations.GOLGARI,
        "Furycalm Snarl": ColorCombinations.BOROS,
        "Vineglimmer Snarl": ColorCombinations.SIMIC,
    }
    tags = {LandTags.ENTERS_UNTAPPED}


class Campuses(metaclass=LandSetMetaclass):
    lands = {
        "Silverquill Campus": ColorCombinations.ORZHOV,
        "Prismari Campus": ColorCombinations.IZZET,
        "Witherbloom Campus": ColorCombinations.GOLGARI,
        "Lorehold Campus": ColorCombinations.BOROS,
        "Quandrix Campus": ColorCombinations.SIMIC,
    }
    tags = {LandTags.MANA_SINK}


class CapennaLocales(metaclass=LandSetMetaclass):
    lands = {
        "Botanical Plaza": ColorCombinations.SELESNYA,
        "Racers' Ring": ColorCombinations.GRUUL,
        "Skybridge Towers": ColorCombinations.AZORIUS,
        "Tramway Station": ColorCombinations.RAKDOS,
        "Waterfront District": ColorCombinations.DIMIR,
    }
    tags = {LandTags.MANA_SINK}


class OldPureTapLands(metaclass=LandSetMetaclass):
    lands = {
        "Coastal Tower": ColorCombinations.AZORIUS,
        "Salt Marsh": ColorCombinations.DIMIR,
        "Urborg Volcano": ColorCombinations.RAKDOS,
        "Shivan Oasis": ColorCombinations.GRUUL,
        "Elfhame Palace": ColorCombinations.SELESNYA,
    }
    tags = {}


class PureTapLands(metaclass=LandSetMetaclass):
    lands = {
        "Meandering River": ColorCombinations.AZORIUS,
        "Submerged Boneyard": ColorCombinations.DIMIR,
        "Cinder Barrens": ColorCombinations.RAKDOS,
        "Timber Gorge": ColorCombinations.GRUUL,
        "Tranquil Expanse": ColorCombinations.SELESNYA,
        "Forsaken Sanctuary": ColorCombinations.ORZHOV,
        "Highland Lake": ColorCombinations.IZZET,
        "Foul Orchard": ColorCombinations.GOLGARI,
        "Stone Quarry": ColorCombinations.BOROS,
        "Woodland Stream": ColorCombinations.SIMIC,
    }
    tags = {}


PICK_PRIORITY = {
    0: OGDuals,
    1: ShockLands,
    2: CheckLands,
    3: TangoLands,
    4: BoundLands,
    5: SlowLands,
    6: FilterLands,
    7: Pathways,
    8: BicycleLands,
    9: HorizonLands,
    10: PainLands,
    11: RevealLands,
    12: OldFilterLands,
    13: FastLands,
    15: Temples,
    16: Campuses,
    17: CapennaLocales,
    20: FetchableTapLands,
    21: KhaldheimSnowLands,
    22: BounceLands,
    90: GuildGates,
    91: Bridges,
    92: ManLands,
    93: RestlessManLands,
    94: ColdsnapSnowLands,
    95: GainLands,
    96: GainLandsOld,
    98: OldPureTapLands,
    99: PureTapLands
}
