class PokemonSpeciesMemoryAddresses:
    _0 = "None"
    _176 = "Charmander"
    _112 = "Weedle"
    _113 = "Kakuna"
    _114 = "Beedrill"
    _36 = "Pidgey"
    _3 = "Nidoran♂"
    _165 = "Rattata"

class ItemsMemoryAddresses:
    _0 = "None"
    _4 = "Poké Ball"
    _5 = "Town Map"
    _11 = "Antidote"
    _234 = "TM34"
    _255 = "Cancel"

class MoveMemoryAddresses:
    _0 = "None"
    _10 = "Scratch"
    _16 = "Gust"
    _28 = "Sand Attack"
    _45 = "Ember"
    _52 = "Leer"
    _165 = "Struggle"

class PokemonSpecies:
    def __init__(self, decimalRamAddress):
        attribute_name = f"_{decimalRamAddress}"
        self.name = getattr(PokemonSpeciesMemoryAddresses, attribute_name)
    def GetPokemonName(self):
        print (self.name)

class Items:
    def __init__(self, decimalRamAddress):
        attribute_name = f"_{decimalRamAddress}"
        self.name = getattr(ItemsMemoryAddresses, attribute_name)
    def GetItemName(self):
        print (self.name)

class Moves:
    def __init__(self, decimalRamAddress):
        attribute_name = f"_{decimalRamAddress}"
        self.name = getattr(MoveMemoryAddresses, attribute_name)
    def GetMoveName(self):
        print (self.name)