class PokemonSpecies:
    def Get(decimalRamAdddress):
        species = {
            0: None,
            176: "Charmander",
            112 : "Weedle",
            113 : "Kakuna",
            114 : "Beedrill",
            36 : "Pidgey",
            3 : "Nidoran♂",
            165 : "Rattata",
            255: None
        }
        return species[decimalRamAdddress]



class MoveMemoryAddresses:
    _0 = "None"
    _10 = "Scratch"
    _16 = "Gust"
    _28 = "Sand Attack"
    _33 = "Quick Attack"
    _39 = "Tackle"
    _40 = "Horn Attack"
    _43 = "Growl"
    _45 = "Ember"
    _52 = "Leer"
    _81 = "Poison Sting"
    _106 = "String Shot"
    _165 = "Struggle"

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