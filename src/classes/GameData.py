import src.classes.PokemonData as PokemonData
import src.classes.ComputerVision as ComputerVision
import logging
import pyboy
class MenuBitmaskContent:
    def __init__(self):
        self._3 = ["Heal","Cancel"]
        self._7 = ["Menu.Items"]
        self._11 = ["Unknown"]
        self._17 = ["Fight","Item"]
        self._33 = ["Pokémon","Run"]
        self._199 = ["Menu.Moves"]

class MenuBitmaskNames:
    def __init__(self):
        self._3 = "Pokémon Center"
        self._7 = "Items"
        self._11 = "BattleStart????"
        self._17 = "Battle"
        self._33 = "Battle"
        self._199 = "Battle"

class CursorPosition:
    def Get(session):
        logging.info("Getting cursor position")
        cursorPosition = (session.get_memory_value(0xCC26))
        logging.info("Cursor position is " + str(cursorPosition))
        return cursorPosition

class Map:
    def Get(session):
        maps = {
            '0': 'Pallet Town',
            '1': 'Viridian City',
            '2': 'Pewter City', 
            '12': 'Route 1',
            '13': 'Route 2',
            '37': 'Red\'s House',
            '39': 'Blue\'s House',
            '40': 'Oak\'s Lab',
            '41': 'Viridan Poké Center',
            '47': 'Route 2 Gatehouse',
            '50': 'Viridian Forrest Gatehouse',
            '51': 'Viridian Forrest',
            '58': 'Pewter Poké Center'
        } 
        mapId = (session.get_memory_value(0xD35E))
        mapName = maps[str(mapId)]

        return mapName

class Pokemon:
    def __init__(self):
        self.species = 'None'
        self.hp = 0
        self.maxHp = 0
        self.level = 0
        self.status = 0
        self.move1 = 0
        self.move1PP = 0
        self.move2 = 0
        self.move2PP = 0
        self.move3 = 0
        self.move3PP = 0
        self.move4 = 0
        self.move4PP = 0

class PartyPokemon:
    def __init__(self):
        self.Pokemon1 = 'None'
        self.Pokemon2 = 'None'
        self.Pokemon3 = 'None'
        self.Pokemon4 = 'None'
        self.Pokemon5 = 'None'
        self.Pokemon6 = 'None'

    def Update(self, session):
        pokemon1SpeciesData = (session.get_memory_value(0xD164))
        pokemon1Species = PokemonData.PokemonSpecies(pokemon1SpeciesData).name
        self.Pokemon1 = Pokemon()
        self.Pokemon1.species = pokemon1Species

        pokemon1Hp1 = (session.get_memory_value(0xD16C))
        pokemon1Hp2 = (session.get_memory_value(0xD16D))
        self.Pokemon1.hp = (pokemon1Hp1 + pokemon1Hp2)

        pokemon1MaxHp1 = (session.get_memory_value(0xD18D))
        pokemon1MaxHp2 = (session.get_memory_value(0xD18E))
        self.Pokemon1.maxHp = (pokemon1MaxHp1 + pokemon1MaxHp2)

        pokemon1Level = (session.get_memory_value(0xD18C))
        self.Pokemon1.level = pokemon1Level

        pokemon1Status = (session.get_memory_value(0xD16F))
        self.Pokemon1.status = pokemon1Status

        pokemon1Move1 = (session.get_memory_value(0xD173))
        pokemon1Move1Name = PokemonData.Moves(pokemon1Move1).name
        self.Pokemon1.move1 = pokemon1Move1Name
        pokemon1Move1PP = (session.get_memory_value(0xD188))
        self.Pokemon1.move1PP = pokemon1Move1PP

        pokemon1Move2 = (session.get_memory_value(0xD174))
        pokemon1Move2Name = PokemonData.Moves(pokemon1Move2).name
        self.Pokemon1.move2 = pokemon1Move2Name
        pokemon1Move2PP = (session.get_memory_value(0xD189))
        self.Pokemon1.move2PP = pokemon1Move2PP

        pokemon1Move3 = (session.get_memory_value(0xD175))
        pokemon1Move3Name = PokemonData.Moves(pokemon1Move3).name
        self.Pokemon1.move3 = pokemon1Move3Name
        pokemon1Move3PP = (session.get_memory_value(0xD18A))
        self.Pokemon1.move3PP = pokemon1Move3PP

        pokemon1Move4 = (session.get_memory_value(0xD176))
        pokemon1Move4Name = PokemonData.Moves(pokemon1Move4).name
        self.Pokemon1.move4 = pokemon1Move4Name
        pokemon1Move4PP = (session.get_memory_value(0xD18B))
        self.Pokemon1.move4PP = pokemon1Move4PP

        pokemon2SpeciesData = (session.get_memory_value(0xD197))
        pokemon2Species = PokemonData.PokemonSpecies(pokemon2SpeciesData).name
        self.Pokemon2 = Pokemon()
        self.Pokemon2.species = pokemon2Species

        pokemon2Hp1 = (session.get_memory_value(0xD198))
        pokemon2Hp2 = (session.get_memory_value(0xD199))
        self.Pokemon2.hp = (pokemon2Hp1 + pokemon2Hp2)

        pokemon2MaxHp1 = (session.get_memory_value(0xD1B9))
        pokemon2MaxHp2 = (session.get_memory_value(0xD1BA))
        self.Pokemon2.maxHp = (pokemon2MaxHp1 + pokemon2MaxHp2)

        pokemon2Level = (session.get_memory_value(0xD1B8))
        self.Pokemon2.level = pokemon2Level

        pokemon2Status = (session.get_memory_value(0xD19B))
        self.Pokemon2.status = pokemon2Status

        pokemon2Move1 = (session.get_memory_value(0xD19F))
        pokemon2Move1Name = PokemonData.Moves(pokemon2Move1).name
        self.Pokemon2.move1 = pokemon2Move1Name
        pokemon2Move1PP = (session.get_memory_value(0xD1B4))
        self.Pokemon2.move1PP = pokemon2Move1PP

        pokemon2Move2 = (session.get_memory_value(0xD1A0))
        pokemon2Move2Name = PokemonData.Moves(pokemon2Move2).name
        self.Pokemon2.move2 = pokemon2Move2Name
        pokemon2Move2PP = (session.get_memory_value(0xD1B5))
        self.Pokemon2.move2PP = pokemon2Move2PP

        pokemon2Move3 = (session.get_memory_value(0xD1A1))
        pokemon2Move3Name = PokemonData.Moves(pokemon2Move3).name
        self.Pokemon2.move3 = pokemon2Move3Name
        pokemon2Move3PP = (session.get_memory_value(0xD1B6))
        self.Pokemon2.move3PP = pokemon2Move3PP

        pokemon2Move4 = (session.get_memory_value(0xD1A2))
        pokemon2Move4Name = PokemonData.Moves(pokemon2Move4).name
        self.Pokemon2.move4 = pokemon2Move4Name
        pokemon2Move4PP = (session.get_memory_value(0xD1B7))
        self.Pokemon2.move4PP = pokemon2Move4PP

        pokemon3SpeciesData = (session.get_memory_value(0xD1C3))
        pokemon3Species = PokemonData.PokemonSpecies(pokemon3SpeciesData).name
        self.Pokemon3 = Pokemon()
        self.Pokemon3.species = pokemon3Species

        pokemon3Hp1 = (session.get_memory_value(0xD1C4))
        pokemon3Hp2 = (session.get_memory_value(0xD1C5))
        self.Pokemon3.hp = (pokemon3Hp1 + pokemon3Hp2)

        pokemon3MaxHp1 = (session.get_memory_value(0xD1E5))
        pokemon3MaxHp2 = (session.get_memory_value(0xD1E6))
        self.Pokemon3.maxHp = (pokemon3MaxHp1 + pokemon3MaxHp2)

        pokemon3Level = (session.get_memory_value(0xD1E4))
        self.Pokemon3.level = pokemon3Level

        pokemon3Status = (session.get_memory_value(0xD1C7))
        self.Pokemon3.status = pokemon3Status

        pokemon3Move1 = (session.get_memory_value(0xD1CB))
        pokemon3Move1Name = PokemonData.Moves(pokemon3Move1).name
        self.Pokemon3.move1 = pokemon3Move1Name
        pokemon3Move1PP = (session.get_memory_value(0xD1E0))
        self.Pokemon3.move1PP = pokemon3Move1PP

        pokemon3Move2 = (session.get_memory_value(0xD1CC))
        pokemon3Move2Name = PokemonData.Moves(pokemon3Move2).name
        self.Pokemon3.move2 = pokemon3Move2Name
        pokemon3Move2PP = (session.get_memory_value(0xD1E1))
        self.Pokemon3.move2PP = pokemon3Move2PP

        pokemon3Move3 = (session.get_memory_value(0xD1CD))
        pokemon3Move3Name = PokemonData.Moves(pokemon3Move3).name
        self.Pokemon3.move3 = pokemon3Move3Name
        pokemon3Move3PP = (session.get_memory_value(0xD1E2))
        self.Pokemon3.move3PP = pokemon3Move3PP

        pokemon3Move4 = (session.get_memory_value(0xD1CE))
        pokemon3Move4Name = PokemonData.Moves(pokemon3Move4).name
        self.Pokemon3.move4 = pokemon3Move4Name
        pokemon3Move4PP = (session.get_memory_value(0xD1E3))
        self.Pokemon3.move4PP = pokemon3Move4PP

        pokemon4SpeciesData = (session.get_memory_value(0xD1EF))
        pokemon4Species = PokemonData.PokemonSpecies(pokemon4SpeciesData).name
        self.Pokemon4 = Pokemon()
        self.Pokemon4.species = pokemon4Species

        pokemon4Hp1 = (session.get_memory_value(0xD1F0))
        pokemon4Hp2 = (session.get_memory_value(0xD1F1))
        self.Pokemon4.hp = (pokemon4Hp1 + pokemon4Hp2)

        pokemon4MaxHp1 = (session.get_memory_value(0xD111))
        pokemon4MaxHp2 = (session.get_memory_value(0xD112))
        self.Pokemon4.maxHp = (pokemon4MaxHp1 + pokemon4MaxHp2)

        pokemon4Level = (session.get_memory_value(0xD210))
        self.Pokemon4.level = pokemon4Level

        pokemon4Status = (session.get_memory_value(0xD1F3))
        self.Pokemon4.status = pokemon4Status

        pokemon4Move1 = (session.get_memory_value(0xD1F7))
        pokemon4Move1Name = PokemonData.Moves(pokemon4Move1).name
        self.Pokemon4.move1 = pokemon4Move1Name
        pokemon4Move1PP = (session.get_memory_value(0xD20C))
        self.Pokemon4.move1PP = pokemon4Move1PP

        pokemon4Move2 = (session.get_memory_value(0xD1F8))
        pokemon4Move2Name = PokemonData.Moves(pokemon4Move2).name
        self.Pokemon4.move2 = pokemon4Move2Name
        pokemon4Move2PP = (session.get_memory_value(0xD20D))
        self.Pokemon4.move2PP = pokemon4Move2PP

        pokemon4Move3 = (session.get_memory_value(0xD1F9))
        pokemon4Move3Name = PokemonData.Moves(pokemon4Move3).name
        self.Pokemon4.move3 = pokemon4Move3Name
        pokemon4Move3PP = (session.get_memory_value(0xD20E))
        self.Pokemon4.move3PP = pokemon4Move3PP

        pokemon4Move4 = (session.get_memory_value(0xD1FA))
        pokemon4Move4Name = PokemonData.Moves(pokemon4Move4).name
        self.Pokemon4.move4 = pokemon4Move4Name
        pokemon4Move4PP = (session.get_memory_value(0xD20F))
        self.Pokemon4.move4PP = pokemon4Move4PP

        pokemon5SpeciesData = (session.get_memory_value(0xD21B))
        pokemon5Species = PokemonData.PokemonSpecies(pokemon5SpeciesData).name
        self.Pokemon5 = Pokemon()
        self.Pokemon5.species = pokemon5Species

        pokemon5Hp1 = (session.get_memory_value(0xD21C))
        pokemon5Hp2 = (session.get_memory_value(0xD21D))
        self.Pokemon5.hp = (pokemon5Hp1 + pokemon5Hp2)

        pokemon5MaxHp1 = (session.get_memory_value(0xD23D))
        pokemon5MaxHp2 = (session.get_memory_value(0xD23E))
        self.Pokemon5.maxHp = (pokemon5MaxHp1 + pokemon5MaxHp2)

        pokemon5Level = (session.get_memory_value(0xD23C))
        self.Pokemon5.level = pokemon5Level

        pokemon5Status = (session.get_memory_value(0xD21F))
        self.Pokemon5.status = pokemon5Status

        pokemon5Move1 = (session.get_memory_value(0xD223))
        pokemon5Move1Name = PokemonData.Moves(pokemon5Move1).name
        self.Pokemon5.move1 = pokemon5Move1Name
        pokemon5Move1PP = (session.get_memory_value(0xD238))
        self.Pokemon5.move1PP = pokemon5Move1PP

        pokemon5Move2 = (session.get_memory_value(0xD224))
        pokemon5Move2Name = PokemonData.Moves(pokemon5Move2).name
        self.Pokemon5.move2 = pokemon5Move2Name
        pokemon5Move2PP = (session.get_memory_value(0xD239))
        self.Pokemon5.move2PP = pokemon5Move2PP

        pokemon5Move3 = (session.get_memory_value(0xD225))
        pokemon5Move3Name = PokemonData.Moves(pokemon5Move3).name
        self.Pokemon5.move3 = pokemon5Move3Name
        pokemon5Move3PP = (session.get_memory_value(0xD23A))
        self.Pokemon5.move3PP = pokemon5Move3PP

        pokemon4Move5 = (session.get_memory_value(0xD226))
        pokemon4Move5Name = PokemonData.Moves(pokemon4Move5).name
        self.Pokemon4.move5 = pokemon4Move5Name
        pokemon4Move5PP = (session.get_memory_value(0xD23B))
        self.Pokemon4.move5PP = pokemon4Move5PP


        pokemon6SpeciesData = (session.get_memory_value(0xD247))
        pokemon6Species = PokemonData.PokemonSpecies(pokemon6SpeciesData).name
        self.Pokemon6 = Pokemon()
        self.Pokemon6.species = pokemon6Species

        pokemon6Hp1 = (session.get_memory_value(0xD248))
        pokemon6Hp2 = (session.get_memory_value(0xD249))
        self.Pokemon6.hp = (pokemon6Hp1 + pokemon6Hp2)

        pokemon6MaxHp1 = (session.get_memory_value(0xD269))
        pokemon6MaxHp2 = (session.get_memory_value(0xD26A))
        self.Pokemon6.maxHp = (pokemon6MaxHp1 + pokemon6MaxHp2)

        pokemon6Level = (session.get_memory_value(0xD268))
        self.Pokemon6.level = pokemon6Level

        pokemon6Status = (session.get_memory_value(0xD24B))
        self.Pokemon6.status = pokemon6Status

        pokemon6Move1 = (session.get_memory_value(0xD24F))
        pokemon6Move1Name = PokemonData.Moves(pokemon6Move1).name
        self.Pokemon6.move1 = pokemon6Move1Name
        pokemon6Move1PP = (session.get_memory_value(0xD264))
        self.Pokemon6.move1PP = pokemon6Move1PP

        pokemon6Move2 = (session.get_memory_value(0xD250))
        pokemon6Move2Name = PokemonData.Moves(pokemon6Move2).name
        self.Pokemon6.move2 = pokemon6Move2Name
        pokemon6Move2PP = (session.get_memory_value(0xD265))
        self.Pokemon6.move2PP = pokemon6Move2PP

        pokemon6Move3 = (session.get_memory_value(0xD251))
        pokemon6Move3Name = PokemonData.Moves(pokemon6Move3).name
        self.Pokemon6.move3 = pokemon6Move3Name
        pokemon6Move3PP = (session.get_memory_value(0xD266))
        self.Pokemon6.move3PP = pokemon6Move3PP

        pokemon4Move6 = (session.get_memory_value(0xD252))
        pokemon4Move6Name = PokemonData.Moves(pokemon4Move6).name
        self.Pokemon4.move6 = pokemon4Move6Name
        pokemon4Move6PP = (session.get_memory_value(0xD267))
        self.Pokemon4.move6PP = pokemon4Move6PP

class PokemonMemoryAddresses:
    def __init__(self):
        self.addresses = {
            "0": "None",
            "1": "Rhydon",
            "2": "Kangaskhan",
            "3": "Nidoran♂",
            "4": "Clefairy",
            "5": "Spearow",
            "6": "Voltorb",
            "7": "Nidoking",
            "8": "Slowbro",
            "9": "Ivysaur",
            "10": "Exeggutor",
            "11": "Lickitung",
            "12": "Exeggcute",
            "13": "Grimer",
            "14": "Gengar",
            "15": "Nidoran♀",
            "16": "Nidoqueen",
            "17": "Cubone",
            "18": "Rhyhorn",
            "19": "Lapras",
            "20": "Arcanine",
            "21": "Mew",
            "22": "Gyarados",
            "23": "Shellder",
            "24": "Tentacool",
            "25": "Gastly",
            "26": "Scyther",
            "27": "Staryu",
            "28": "Blastoise",
            "29": "Pinsir",
            "30": "Tangela",
            "31": "MissingNo.",
            "32": "MissingNo.",
            "33": "Growlithe",
            "34": "Onix",
            "35": "Fearow",
            "36": "Pidgey",
            "37": "Slowpoke",
            "38": "Kadabra",
            "39": "Graveler",
            "40": "Chansey",
            "41": "Machoke",
            "42": "Mr. Mime",
            "43": "Hitmonlee",
            "44": "Hitmonchan",
            "45": "Arbok",
            "46": "Parasect",
            "47": "Psyduck",
            "48": "Drowzee",
            "49": "Golem",
            "50": "MissingNo.",
            "51": "Magmar",
            "52": "MissingNo.",
            "53": "Electabuzz",
            "54": "Magneton",
            "55": "Koffing",
            "56": "MissingNo.",
            "57": "Mankey",
            "58": "Seel",
            "59": "Diglett",
            "60": "Tauros",
            "61": "MissingNo.",
            "62": "MissingNo.",
            "63": "MissingNo.",
            "64": "Farfetch'd",
            "65": "Venonat",
            "66": "Dragonite",
            "67": "MissingNo.",
            "68": "MissingNo.",
            "69": "MissingNo.",
            "70": "Doduo",
            "71": "Poliwag",
            "72": "Jynx",
            "73": "Moltres",
            "74": "Articuno",
            "75": "Zapdos",
            "76": "Ditto",
            "77": "Meowth",
            "78": "Krabby",
            "79": "MissingNo.",
            "80": "MissingNo.",
            "81": "MissingNo.",
            "82": "Vulpix",
            "83": "Ninetales",
            "84": "Pikachu",
            "85": "Raichu",
            "86": "MissingNo.",
            "87": "MissingNo.",
            "88": "Dratini",
            "89": "Dragonair",
            "90": "Kabuto",
            "91": "Kabutops",
            "92": "Horsea",
            "93": "Seadra",
            "94": "MissingNo.",
            "95": "MissingNo.",
            "96": "Sandshrew",
            "97": "Sandslash",
            "98": "Omanyte",
            "99": "Omastar",
            "100": "Jigglypuff",
            "101": "Wigglytuff",
            "102": "Eevee",
            "103": "Flareon",
            "104": "Jolteon",
            "105": "Vaporeon",
            "106": "Machop",
            "107": "Zubat",
            "108": "Ekans",
            "109": "Paras",
            "110": "Poliwhirl",
            "111": "Poliwrath",
            "112": "Weedle",
            "113": "Kakuna",
            "114": "Beedrill",
            "115": "MissingNo.",
            "116": "Dodrio",
            "117": "Primeape",
            "118": "Dugtrio",
            "119": "Venomoth",
            "120": "Dewgong",
            "121": "MissingNo.",
            "122": "MissingNo.",
            "123": "Caterpie",
            "124": "Metapod",
            "125": "Butterfree",
            "126": "Machamp",
            "127": "MissingNo.",
            "128": "Golduck",
            "129": "Hypno",
            "130": "Golbat",
            "131": "Mewtwo",
            "132": "Snorlax",
            "133": "Magikarp",
            "134": "MissingNo.",
            "135": "MissingNo.",
            "136": "Muk",
            "137": "MissingNo.",
            "138": "Kingler",
            "139": "Cloyster",
            "140": "MissingNo.",
            "141": "Electrode",
            "142": "Clefable",
            "143": "Weezing",
            "144": "Persian",
            "145": "Marowak",
            "146": "MissingNo.",
            "147": "Haunter",
            "148": "Abra",
            "149": "Alakazam",
            "150": "Pidgeotto",
            "151": "Pidgeot",
            "152": "Starmie",
            "153": "Bulbasaur",
            "154": "Venusaur",
            "155": "Tentacruel",
            "156": "MissingNo.",
            "157": "Goldeen",
            "158": "Seaking",
            "159": "MissingNo.",
            "160": "MissingNo.",
            "161": "MissingNo.",
            "162": "MissingNo.",
            "163": "Ponyta",
            "164": "Rapidash",
            "165": "Rattata",
            "166": "Raticate",
            "167": "Nidorino",
            "168": "Nidorina",
            "169": "Geodude",
            "170": "Porygon",
            "171": "Aerodactyl",
            "172": "MissingNo.",
            "173": "Magnemite",
            "174": "MissingNo.",
            "175": "MissingNo.",
            "176": "Charmander",
            "177": "Squirtle",
            "178": "Charmeleon",
            "179": "Wartortle",
            "180": "Charizard",
            "181": "MissingNo.",
            "182": "MissingNo.",
            "183": "MissingNo.",
            "184": "MissingNo.",
            "185": "Oddish",
            "186": "Gloom",
            "187": "Vileplume",
            "188": "Bellsprout",
            "189": "Weepinbell",
            "190": "Victreebel"
        }

class ItemMemoryAddresses:
    def __init__(self):
        self.addresses = {
            "0": "None",
            "1": "Master Ball",
            "2": "Ultra Ball",
            "3": "Great Ball",
            "4": "Poké Ball",
            "5": "Town Map",
            "6": "Bicycle",
            "7": "?????",
            "8": "Safari Ball",
            "9": "Pokédex",
            "10": "Moon Stone",
            "11": "Antidote",
            "12": "Burn Heal",
            "13": "Ice Heal",
            "14": "Awakening",
            "15": "Parlyz Heal",
            "16": "Full Restore",
            "17": "Max Potion",
            "18": "Hyper Potion",
            "19": "Super Potion",
            "20": "Potion",
            "21": "BoulderBadge",
            "22": "CascadeBadge",
            "23": "ThunderBadge",
            "24": "RainbowBadge",
            "25": "SoulBadge",
            "26": "MarshBadge",
            "27": "VolcanoBadge",
            "28": "EarthBadge",
            "29": "Escape Rope",
            "30": "Repel",
            "31": "Old Amber",
            "32": "Fire Stone",
            "33": "Thunderstone",
            "34": "Water Stone",
            "35": "HP Up",
            "36": "Protein",
            "37": "Iron",
            "38": "Carbos",
            "39": "Calcium",
            "40": "Rare Candy",
            "41": "Dome Fossil",
            "42": "Helix Fossil",
            "43": "Secret Key",
            "44": "?????",
            "45": "Bike Voucher",
            "46": "X Accuracy",
            "47": "Leaf Stone",
            "48": "Card Key",
            "49": "Nugget",
            "50": "PP Up",
            "51": "Poké Doll",
            "52": "Full Heal",
            "53": "Revive",
            "54": "Max Revive",
            "55": "Guard Spec.",
            "56": "Super Repel",
            "57": "Max Repel"
        }


class Items:
    def GetMemoryAddress(itemName):
        memoryAdresses = ItemMemoryAddresses()
        for key, value in memoryAdresses.addresses.items():
            if value == itemName:
                return key
    
    def GetItemName(memoryAddress):
        memoryAdresses = ItemMemoryAddresses() 
        return memoryAdresses.addresses[memoryAddress]
    
    def SetBagItem(session, index, item, quantity):
        bagIndexAddresses = {
            "0": 54046,
            "1": 54048,
            "2": 54050,
            "3": 54052,
            "4": 54054,
            "5": 54056,
            "6": 54058,
            "7": 54060,
            "8": 54062,
            "9": 54064,
            "10": 54066,
            "11": 54068,
            "12": 54070,
            "13": 54072,
            "14": 54074,
            "15": 54076,
            "16": 54078,
            "17": 54080,
            "18": 54082,
            "19": 54084,
        }
        bagQuantityAddresses = {
            "0": 54047,
            "1": 54049,
            "2": 54051,
            "3": 54053,
            "4": 54055,
            "5": 54057,
            "6": 54059,
            "7": 54061,
            "8": 54063,
            "9": 54065,
            "10": 54067,
            "11": 54069,
            "12": 54071,
            "13": 54073,
            "14": 54075,
            "15": 54077,
            "16": 54079,
            "17": 54081,
            "18": 54083,
            "19": 54085,
        }
        indexAddress = int(bagIndexAddresses[index])
        itemAddress = int(Items.GetMemoryAddress(item))
        quantityAddress = int(bagQuantityAddresses[index])
        
        logging.info("Setting item at index " + str(index) + "/" + str(indexAddress) + " to " + item + " with quantity " + str(quantity))
        session.set_memory_value(indexAddress, itemAddress)
        session.set_memory_value(quantityAddress, quantity)



    # def Update(self, session): 
    #     bagItem1Index = (session.get_memory_value(0xD31E))
    #     bagItem1Qty = (session.get_memory_value(0xD31F))
    #     bagItem1Name = PokemonData.Items(bagItem1Index).name
    #     self.item1 = bagItem1Name
    #     self.item1Quantity = bagItem1Qty

    #     bagItem2Index = (session.get_memory_value(0xD320))
    #     bagItem2Qty = (session.get_memory_value(0xD321))
    #     bagItem2Name = PokemonData.Items(bagItem2Index).name
    #     self.item2 = bagItem2Name
    #     self.item2Quantity = bagItem2Qty

    #     bagItem3Index = (session.get_memory_value(0xD322))
    #     bagItem3Qty = (session.get_memory_value(0xD323))
    #     bagItem3Name = PokemonData.Items(bagItem3Index).name
    #     self.item3 = bagItem3Name
    #     self.item3Quantity = bagItem3Qty

    #     bagItem4Index = (session.get_memory_value(0xD324))
    #     bagItem4Qty = (session.get_memory_value(0xD325))
    #     bagItem4Name = PokemonData.Items(bagItem4Index).name
    #     self.item4 = bagItem4Name
    #     self.item4Quantity = bagItem4Qty

    #     bagItem5Index = (session.get_memory_value(0xD326))
    #     bagItem5Qty = (session.get_memory_value(0xD327))
    #     bagItem5Name = PokemonData.Items(bagItem4Index).name
    #     self.item5 = bagItem5Name
    #     self.item5Quantity = bagItem5Qty

    #     bagItem6Index = (session.get_memory_value(0xD328))
    #     bagItem6Qty = (session.get_memory_value(0xD329))
    #     bagItem6Name = PokemonData.Items(bagItem6Index).name
    #     self.item6 = bagItem6Name
    #     self.item6Quantity = bagItem6Qty

    #     bagItem7Index = (session.get_memory_value(0xD32A))
    #     bagItem7Qty = (session.get_memory_value(0xD32B))
    #     bagItem7Name = PokemonData.Items(bagItem7Index).name
    #     self.item7 = bagItem7Name
    #     self.item7Quantity = bagItem7Qty

    #     bagItem8Index = (session.get_memory_value(0xD32C))
    #     bagItem8Qty = (session.get_memory_value(0xD32D))
    #     bagItem8Name = PokemonData.Items(bagItem8Index).name
    #     self.item8 = bagItem8Name
    #     self.item8Quantity = bagItem8Qty

    #     bagItem9Index = (session.get_memory_value(0xD32E))
    #     bagItem9Qty = (session.get_memory_value(0xD32F))
    #     bagItem9Name = PokemonData.Items(bagItem9Index).name
    #     self.item9 = bagItem9Name
    #     self.item9Quantity = bagItem9Qty

    #     bagItem10Index = (session.get_memory_value(0xD330))
    #     bagItem10Qty = (session.get_memory_value(0xD331))
    #     bagItem10Name = PokemonData.Items(bagItem10Index).name
    #     self.item10 = bagItem10Name
    #     self.item10Quantity = bagItem10Qty
        
    #     bagItem11Index = (session.get_memory_value(0xD332))
    #     bagItem11Qty = (session.get_memory_value(0xD333))
    #     bagItem11Name = PokemonData.Items(bagItem11Index).name
    #     self.item11 = bagItem11Name
    #     self.item11Quantity = bagItem11Qty

    #     bagItem12Index = (session.get_memory_value(0xD334))
    #     bagItem12Qty = (session.get_memory_value(0xD335))
    #     bagItem12Name = PokemonData.Items(bagItem12Index).name
    #     self.item12 = bagItem12Name
    #     self.item12Quantity = bagItem12Qty

    #     bagItem13Index = (session.get_memory_value(0xD336))
    #     bagItem13Qty = (session.get_memory_value(0xD337))
    #     bagItem13Name = PokemonData.Items(bagItem13Index).name
    #     self.item13 = bagItem13Name
    #     self.item13Quantity = bagItem13Qty

    #     bagItem14Index = (session.get_memory_value(0xD338))
    #     bagItem14Qty = (session.get_memory_value(0xD339))
    #     bagItem14Name = PokemonData.Items(bagItem14Index).name
    #     self.item14 = bagItem14Name
    #     self.item14Quantity = bagItem14Qty

    #     bagItem15Index = (session.get_memory_value(0xD33A))
    #     bagItem15Qty = (session.get_memory_value(0xD33B))
    #     bagItem15Name = PokemonData.Items(bagItem15Index).name
    #     self.item15 = bagItem15Name
    #     self.item15Quantity = bagItem15Qty

    #     bagItem16Index = (session.get_memory_value(0xD33C))
    #     bagItem16Qty = (session.get_memory_value(0xD33D))
    #     bagItem16Name = PokemonData.Items(bagItem16Index).name
    #     self.item16 = bagItem16Name
    #     self.item16Quantity = bagItem16Qty

    #     bagItem17Index = (session.get_memory_value(0xD33E))
    #     bagItem17Qty = (session.get_memory_value(0xD33F))
    #     bagItem17Name = PokemonData.Items(bagItem17Index).name
    #     self.item17 = bagItem17Name
    #     self.item17Quantity = bagItem17Qty

    #     bagItem18Index = (session.get_memory_value(0xD340))
    #     bagItem18Qty = (session.get_memory_value(0xD341))
    #     bagItem18Name = PokemonData.Items(bagItem18Index).name
    #     self.item18 = bagItem18Name
    #     self.item18Quantity = bagItem18Qty
        
    #     bagItem19Index = (session.get_memory_value(0xD342))
    #     bagItem19Qty = (session.get_memory_value(0xD343))
    #     bagItem19Name = PokemonData.Items(bagItem4Index).name
    #     self.item19 = bagItem19Name
    #     self.item19Quantity = bagItem19Qty

    #     bagItem20Index = (session.get_memory_value(0xD344))
    #     bagItem20Qty = (session.get_memory_value(0xD345))
    #     bagItem20Name = PokemonData.Items(bagItem4Index).name
    #     self.item20 = bagItem20Name
    #     self.item20Quantity = bagItem20Qty

class Pokemon:
    def GetMemoryAddress(pokemonName):
        memoryAdresses = PokemonMemoryAddresses()
        for key, value in memoryAdresses.addresses.items():
            if value == pokemonName:
                print(key)
    
    def GetPokemonName(memoryAddress):
        memoryAdresses = PokemonMemoryAddresses() 
        print(memoryAdresses.addresses[memoryAddress])

class ActivePokemon:
    def __init__(self):
        self.species = 'None'
        self.hp = 0
        self.maxHp = 0
        self.level = 0
        self.status = 0
        self.move1 = 0
        self.move1PP = 0
        self.move2 = 0
        self.move2PP = 0
        self.move3 = 0
        self.move3PP = 0
        self.move4 = 0
        self.move4PP = 0

    def Update(self, session):
        activePokemonSpecies = (session.get_memory_value(0xD014))
        activePokemonSpeciesName = PokemonData.PokemonSpecies(activePokemonSpecies).name
        self.species = activePokemonSpeciesName

        activePokemonHp1 = (session.get_memory_value(0xD015))
        activePokemonHp2 = (session.get_memory_value(0xD016))
        self.hp = (activePokemonHp1 + activePokemonHp2)

        activePokemonMaxHp1 = (session.get_memory_value(0xD023))
        activePokemonMaxHp2 = (session.get_memory_value(0xD024))
        self.maxHp = (activePokemonMaxHp1 + activePokemonMaxHp2)

        activePokemonLevel = (session.get_memory_value(0xD022))
        self.level = activePokemonLevel

        activePokemonStatus = (session.get_memory_value(0xD018))
        self.status = activePokemonStatus

        activePokemonMove1 = (session.get_memory_value(0xD01C))
        activePokemonMove1Name = PokemonData.Moves(activePokemonMove1).name
        self.move1 = activePokemonMove1Name
        activePokemonMove1PP = (session.get_memory_value(0xD02D))
        self.move1PP = activePokemonMove1PP

        activePokemonMove2 = (session.get_memory_value(0xD01D))
        activePokemonMove2Name = PokemonData.Moves(activePokemonMove2).name
        self.move2 = activePokemonMove2Name
        activePokemonMove2PP = (session.get_memory_value(0xD02E))
        self.move2PP = activePokemonMove2PP

        activePokemonMove3 = (session.get_memory_value(0xD01E))
        activePokemonMove3Name = PokemonData.Moves(activePokemonMove3).name
        self.move3 = activePokemonMove3Name
        activePokemonMove3PP = (session.get_memory_value(0xD02F))
        self.move3PP = activePokemonMove3PP

        activePokemonMove4 = (session.get_memory_value(0xD01F))
        activePokemonMove4Name = PokemonData.Moves(activePokemonMove4).name
        self.move4 = activePokemonMove4Name
        activePokemonMove4PP = (session.get_memory_value(0xD030))
        self.move4PP = activePokemonMove4PP

class EnemyPokemon:
    def __init__(self):
        self.species = 'None'
        self.hp = 0
        self.level = 0
        self.status = 0
        self.move1 = 0
        self.move1PP = 0
        self.move2 = 0
        self.move2PP = 0
        self.move3 = 0
        self.move3PP = 0
        self.move4 = 0
        self.move4PP = 0

    def Update(self, session):
        enemyActivePokemonSpecies = (session.get_memory_value(0xCFD8))
        enemyActivePokemonSpeciesName = PokemonData.PokemonSpecies(enemyActivePokemonSpecies).name
        self.species = enemyActivePokemonSpeciesName

        enemyPokemonHP1 = (session.get_memory_value(0xCFE6))
        enemyPokemonHP2 = (session.get_memory_value(0xCFE7))
        
        enemyPokemonMaxHP1 = (session.get_memory_value(0xCFF4))
        enemyPokemonMaxHP2 = (session.get_memory_value(0xCFF5))
        enemyPokemonMaxHP = (enemyPokemonMaxHP1 + enemyPokemonMaxHP2)

        self.hp = (enemyPokemonHP1 + enemyPokemonHP2) / enemyPokemonMaxHP * 100

        enemyPokemonLevel = (session.get_memory_value(0XCFF3))
        self.level = enemyPokemonLevel

        enemyPokemonStatus = (session.get_memory_value(0xCFE9))
        self.status = enemyPokemonStatus

class Battle:
    def __init__(self):
        self.status = 'NotInBattle'
        self.activePokemonSpecies = None
        self.activePokemonHP = 0
        self.activePokemonMaxHP = 0
        self.activePokemonLevel = 0
        self.activePokemonStatus = 0
        self.activePokemonMove1 = 0
        self.activePokemonMove1PP = 0
        self.activePokemonMove2 = 0
        self.activePokemonMove2PP = 0
        self.activePokemonMove3 = 0
        self.activePokemonMove3PP = 0
        self.activePokemonMove4 = 0
        self.activePokemonMove4PP = 0

        self.enemyPokemonSpecies = None
        self.enemyPokemonHP = 0
        self.enemyPokemonLevel = 0
        self.enemyPokemonStatus = 0

    def Update(self, session):
        battleStatus = (session.get_memory_value(0xD057))
        if(battleStatus == 1):
            self.status = "InBattle"
            playerActivePokemon = ActivePokemon()
            playerActivePokemon.Update(session)
            self.activePokemonSpecies = playerActivePokemon.species
            self.activePokemonHP = playerActivePokemon.hp
            self.activePokemonMaxHP = playerActivePokemon.maxHp
            self.activePokemonLevel = playerActivePokemon.level
            self.activePokemonStatus = playerActivePokemon.status
            self.activePokemonMove1 = playerActivePokemon.move1
            self.activePokemonMove1PP = playerActivePokemon.move1PP
            self.activePokemonMove2 = playerActivePokemon.move2
            self.activePokemonMove2PP = playerActivePokemon.move2PP
            self.activePokemonMove3 = playerActivePokemon.move3
            self.activePokemonMove3PP = playerActivePokemon.move3PP
            self.activePokemonMove4 = playerActivePokemon.move4
            self.activePokemonMove4PP = playerActivePokemon.move4PP

            enemyActivePokemon = EnemyPokemon()
            enemyActivePokemon.Update(session)
            self.enemyPokemonSpecies = enemyActivePokemon.species
            self.enemyPokemonHP = enemyActivePokemon.hp
            self.enemyPokemonLevel = enemyActivePokemon.level
            self.enemyPokemonStatus = enemyActivePokemon.status

class Sprites:
    def OnScreen(session):
        sprites = {
            # TODO: Populate
            'player': {
                'down': 32768,
                'up': 32832,
                'sidways': 32896
 
            },
            'Nurse Joy': {
                'down': 32960
            },      
            'Old man with fancy clothes': {
                'down': 33344,
                'sideways': 33280
            },
            'Old bald man': {
                'sideways': b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff\x00\x00\x00\xff\x84\x84\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff::\x94\xff\x84\x84\xff\xff\x84\x84\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff\x84\x84\xff\xff\x84\x84\xff\xff\x84\x84\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff\x84\x84\xff\xff\x84\x84\xff\xff\x84\x84\xff\xff\x84\x84\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff\x84\x84\xff\xff\x84\x84\xff\xff\x84\x84\xff\xff\x84\x84\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff\x84\x84\xff\xff\x00\x00\x00\xff\x00\x00\x00\xff\x84\x84\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\xff\x84\x84\xff\xff\x84\x84\xff\xff\x84\x84\xff\xff\x84\x84\xff\xff'
            }
        }
        sprite00 = session.botsupport_manager().sprite(0)
        sprite01 = session.botsupport_manager().sprite(4)
        sprite02 = session.botsupport_manager().sprite(8)
        sprite03 = session.botsupport_manager().sprite(12)

        sprite00TileId = sprite00.tiles[0].tile_identifier
        sprite00Tile = session.botsupport_manager().tile(sprite00TileId).data_address
        print(sprite00Tile)

        sprite01TileId = sprite01.tiles[0].tile_identifier
        sprite01Tile = session.botsupport_manager().tile(sprite01TileId).data_address
        print(sprite01Tile)

        sprite02TileId = sprite02.tiles[0].tile_identifier
        sprite02Tile = session.botsupport_manager().tile(sprite02TileId).data_address
        print(sprite02Tile)

        sprite03TileId = sprite03.tiles[0].tile_identifier
        sprite03Tile = session.botsupport_manager().tile(sprite03TileId).data_address
        print(sprite03Tile)
