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

class Items:
    def __init__(self):
        self.item1 = 'None'
        self.item1Quantity = 0
        self.item2 = 'None'
        self.item2Quantity = 0
        self.item3 = 'None'
        self.item3Quantity = 0
        self.item4 = 'None'
        self.item4Quantity = 0
        self.item5 = 'None'
        self.item5Quantity = 0
        self.item6 = 'None'
        self.item6Quantity = 0
        self.item7 = 'None'
        self.item7Quantity = 0
        self.item8 = 'None'
        self.item8Quantity = 0
        self.item9 = 'None'
        self.item9Quantity = 0
        self.item10 = 'None'
        self.item10Quantity = 0
        self.item11 = 'None'
        self.item11Quantity = 0
        self.item12 = 'None'
        self.item12Quantity = 0
        self.item13 = 'None'
        self.item13Quantity = 0
        self.item14 = 'None'
        self.item14Quantity = 0
        self.item15 = 'None'
        self.item15Quantity = 0
        self.item16 = 'None'
        self.item16Quantity = 0
        self.item17 = 'None'
        self.item17Quantity = 0
        self.item18 = 'None'
        self.item18Quantity = 0
        self.item19 = 'None'
        self.item19Quantity = 0
        self.item20 = 'None'
        self.item20Quantity = 0
        
    def Update(self, session): 
        bagItem1Index = (session.get_memory_value(0xD31E))
        bagItem1Qty = (session.get_memory_value(0xD31F))
        bagItem1Name = PokemonData.Items(bagItem1Index).name
        self.item1 = bagItem1Name
        self.item1Quantity = bagItem1Qty

        bagItem2Index = (session.get_memory_value(0xD320))
        bagItem2Qty = (session.get_memory_value(0xD321))
        bagItem2Name = PokemonData.Items(bagItem2Index).name
        self.item2 = bagItem2Name
        self.item2Quantity = bagItem2Qty

        bagItem3Index = (session.get_memory_value(0xD322))
        bagItem3Qty = (session.get_memory_value(0xD323))
        bagItem3Name = PokemonData.Items(bagItem3Index).name
        self.item3 = bagItem3Name
        self.item3Quantity = bagItem3Qty

        bagItem4Index = (session.get_memory_value(0xD324))
        bagItem4Qty = (session.get_memory_value(0xD325))
        bagItem4Name = PokemonData.Items(bagItem4Index).name
        self.item4 = bagItem4Name
        self.item4Quantity = bagItem4Qty

        bagItem5Index = (session.get_memory_value(0xD326))
        bagItem5Qty = (session.get_memory_value(0xD327))
        bagItem5Name = PokemonData.Items(bagItem4Index).name
        self.item5 = bagItem5Name
        self.item5Quantity = bagItem5Qty

        bagItem6Index = (session.get_memory_value(0xD328))
        bagItem6Qty = (session.get_memory_value(0xD329))
        bagItem6Name = PokemonData.Items(bagItem6Index).name
        self.item6 = bagItem6Name
        self.item6Quantity = bagItem6Qty

        bagItem7Index = (session.get_memory_value(0xD32A))
        bagItem7Qty = (session.get_memory_value(0xD32B))
        bagItem7Name = PokemonData.Items(bagItem7Index).name
        self.item7 = bagItem7Name
        self.item7Quantity = bagItem7Qty

        bagItem8Index = (session.get_memory_value(0xD32C))
        bagItem8Qty = (session.get_memory_value(0xD32D))
        bagItem8Name = PokemonData.Items(bagItem8Index).name
        self.item8 = bagItem8Name
        self.item8Quantity = bagItem8Qty

        bagItem9Index = (session.get_memory_value(0xD32E))
        bagItem9Qty = (session.get_memory_value(0xD32F))
        bagItem9Name = PokemonData.Items(bagItem9Index).name
        self.item9 = bagItem9Name
        self.item9Quantity = bagItem9Qty

        bagItem10Index = (session.get_memory_value(0xD330))
        bagItem10Qty = (session.get_memory_value(0xD331))
        bagItem10Name = PokemonData.Items(bagItem10Index).name
        self.item10 = bagItem10Name
        self.item10Quantity = bagItem10Qty
        
        bagItem11Index = (session.get_memory_value(0xD332))
        bagItem11Qty = (session.get_memory_value(0xD333))
        bagItem11Name = PokemonData.Items(bagItem11Index).name
        self.item11 = bagItem11Name
        self.item11Quantity = bagItem11Qty

        bagItem12Index = (session.get_memory_value(0xD334))
        bagItem12Qty = (session.get_memory_value(0xD335))
        bagItem12Name = PokemonData.Items(bagItem12Index).name
        self.item12 = bagItem12Name
        self.item12Quantity = bagItem12Qty

        bagItem13Index = (session.get_memory_value(0xD336))
        bagItem13Qty = (session.get_memory_value(0xD337))
        bagItem13Name = PokemonData.Items(bagItem13Index).name
        self.item13 = bagItem13Name
        self.item13Quantity = bagItem13Qty

        bagItem14Index = (session.get_memory_value(0xD338))
        bagItem14Qty = (session.get_memory_value(0xD339))
        bagItem14Name = PokemonData.Items(bagItem14Index).name
        self.item14 = bagItem14Name
        self.item14Quantity = bagItem14Qty

        bagItem15Index = (session.get_memory_value(0xD33A))
        bagItem15Qty = (session.get_memory_value(0xD33B))
        bagItem15Name = PokemonData.Items(bagItem15Index).name
        self.item15 = bagItem15Name
        self.item15Quantity = bagItem15Qty

        bagItem16Index = (session.get_memory_value(0xD33C))
        bagItem16Qty = (session.get_memory_value(0xD33D))
        bagItem16Name = PokemonData.Items(bagItem16Index).name
        self.item16 = bagItem16Name
        self.item16Quantity = bagItem16Qty

        bagItem17Index = (session.get_memory_value(0xD33E))
        bagItem17Qty = (session.get_memory_value(0xD33F))
        bagItem17Name = PokemonData.Items(bagItem17Index).name
        self.item17 = bagItem17Name
        self.item17Quantity = bagItem17Qty

        bagItem18Index = (session.get_memory_value(0xD340))
        bagItem18Qty = (session.get_memory_value(0xD341))
        bagItem18Name = PokemonData.Items(bagItem18Index).name
        self.item18 = bagItem18Name
        self.item18Quantity = bagItem18Qty
        
        bagItem19Index = (session.get_memory_value(0xD342))
        bagItem19Qty = (session.get_memory_value(0xD343))
        bagItem19Name = PokemonData.Items(bagItem4Index).name
        self.item19 = bagItem19Name
        self.item19Quantity = bagItem19Qty

        bagItem20Index = (session.get_memory_value(0xD344))
        bagItem20Qty = (session.get_memory_value(0xD345))
        bagItem20Name = PokemonData.Items(bagItem4Index).name
        self.item20 = bagItem20Name
        self.item20Quantity = bagItem20Qty

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
        spriteList = {
            0: "Player",
            1: "Player",
            2: "Player",
            3: "Player",
            4: "Player",
            5: "Player",
            6: "Player",
            7: "Player",
            8: "Player",
            9: "Player",
            10: "Player",
            11: "Player",
            12: "Nurse Joy",
            13: "Nurse Joy",
            14: "Nurse Joy",
            15: "Nurse Joy",

        }
        sprite0 = session.botsupport_manager().sprite(0)
        sprite1 = session.botsupport_manager().sprite(1)
        sprite2 = session.botsupport_manager().sprite(2)
        sprite3 = session.botsupport_manager().sprite(3)

        try:
            npc0Name = spriteList[sprite0.tile_identifier]
        except:
            npc0Name = "None"

        npc0 = {
            'name': npc0Name, 
            'topLeft': (sprite0.x, sprite0.y),
            'topRight': (sprite1.x, sprite1.y),
            'bottomLeft': (sprite2.x, sprite2.y),
            'bottomRight': (sprite3.x, sprite3.y)
        }

        sprite4 = session.botsupport_manager().sprite(4)
        sprite5 = session.botsupport_manager().sprite(5)
        sprite6 = session.botsupport_manager().sprite(6)
        sprite7 = session.botsupport_manager().sprite(7)

        try:
            npc1Name = spriteList[sprite4.tile_identifier]
        except:
            npc1Name = "None"

        npc1 = {
            'name': npc1Name,
            'topLeft': (sprite4.x, sprite4.y),
            'topRight': (sprite5.x, sprite5.y),
            'bottomLeft': (sprite6.x, sprite6.y),
            'bottomRight': (sprite7.x, sprite7.y)
        }

        return npc0, npc1

        # sprite8 = session.botsupport_manager().sprite(8)
        # sprite9 = session.botsupport_manager().sprite(9)
        # sprite10 = session.botsupport_manager().sprite(10)
        # sprite11 = session.botsupport_manager().sprite(11)
        


        # sprite12 = session.botsupport_manager().sprite(12)
        # sprite13 = session.botsupport_manager().sprite(13)
        # sprite14 = session.botsupport_manager().sprite(14)
        # sprite15 = session.botsupport_manager().sprite(15)
        # print("NPC3T1X: ", sprite12.x, "NPC3T1Y: ", sprite12.y, "Tile Identifier: ", sprite12.tile_identifier)
        # print("NPC3T2X: ", sprite13.x, "NPC3T2Y: ", sprite13.y, "Tile Identifier: ", sprite13.tile_identifier)
        # print("NPC3T3X: ", sprite14.x, "NPC3T3Y: ", sprite14.y, "Tile Identifier: ", sprite14.tile_identifier)
        # print("NPC3T4X: ", sprite15.x, "NPC3T4Y: ", sprite15.y, "Tile Identifier: ", sprite15.tile_identifier)
