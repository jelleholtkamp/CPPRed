import classes.PokemonData as PokemonData
import pyboy

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
        
