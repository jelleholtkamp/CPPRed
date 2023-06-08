import classes.PokemonData as PokemonData
import classes.Commands as Commands
import classes.GameData as GameData
import os
import sys

from pyboy import PyBoy, WindowEvent

# Makes us able to import PyBoy from the directory below
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, file_path + "/..")

# Check if the ROM is given through argv
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Usage: Test.py [ROM file]")
    exit(1)

quiet = "--quiet" in sys.argv
session = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=quiet, game_wrapper=True)
session.set_emulation_speed(0)
assert session.cartridge_title() == "POKEMON RED"

startGame = Commands.StartGame()

startGame.Start(session)

while not session.tick():
    partyPokemon = GameData.PartyPokemon()
    partyPokemon.Update(session)
    print(partyPokemon.Pokemon1.species)
    print(partyPokemon.Pokemon1.hp)
    print(partyPokemon.Pokemon1.maxHp)
    print(partyPokemon.Pokemon1.level)
    print(partyPokemon.Pokemon1.status)
    print(partyPokemon.Pokemon1.move1)
    print(partyPokemon.Pokemon1.move1PP)
    print(partyPokemon.Pokemon1.move2)
    print(partyPokemon.Pokemon1.move2PP)
    print(partyPokemon.Pokemon1.move3)
    print(partyPokemon.Pokemon1.move3PP)
    print(partyPokemon.Pokemon1.move4)
    print(partyPokemon.Pokemon1.move4PP)

    print(partyPokemon.Pokemon2.species)
    print(partyPokemon.Pokemon2.hp)
    print(partyPokemon.Pokemon2.maxHp)
    print(partyPokemon.Pokemon2.level)
    print(partyPokemon.Pokemon2.status)
    print(partyPokemon.Pokemon2.move1)
    print(partyPokemon.Pokemon2.move1PP)
    print(partyPokemon.Pokemon2.move2)
    print(partyPokemon.Pokemon2.move2PP)
    print(partyPokemon.Pokemon2.move3)
    print(partyPokemon.Pokemon2.move3PP)
    print(partyPokemon.Pokemon2.move4)
    print(partyPokemon.Pokemon2.move4PP)

    print(partyPokemon.Pokemon3.species)
    print(partyPokemon.Pokemon3.hp)
    print(partyPokemon.Pokemon3.maxHp)
    print(partyPokemon.Pokemon3.level)
    print(partyPokemon.Pokemon3.status)
    print(partyPokemon.Pokemon3.move1)
    print(partyPokemon.Pokemon3.move1PP)
    print(partyPokemon.Pokemon3.move2)
    print(partyPokemon.Pokemon3.move2PP)
    print(partyPokemon.Pokemon3.move3)
    print(partyPokemon.Pokemon3.move3PP)
    print(partyPokemon.Pokemon3.move4)
    print(partyPokemon.Pokemon3.move4PP)

    print(partyPokemon.Pokemon4.species)
    print(partyPokemon.Pokemon4.hp)
    print(partyPokemon.Pokemon4.maxHp)
    print(partyPokemon.Pokemon4.level)
    print(partyPokemon.Pokemon4.status)
    print(partyPokemon.Pokemon4.move1)
    print(partyPokemon.Pokemon4.move1PP)
    print(partyPokemon.Pokemon4.move2)
    print(partyPokemon.Pokemon4.move2PP)
    print(partyPokemon.Pokemon4.move3)
    print(partyPokemon.Pokemon4.move3PP)
    print(partyPokemon.Pokemon4.move4)
    print(partyPokemon.Pokemon4.move4PP)

    print(partyPokemon.Pokemon5.species)
    print(partyPokemon.Pokemon5.hp)
    print(partyPokemon.Pokemon5.maxHp)
    print(partyPokemon.Pokemon5.level)
    print(partyPokemon.Pokemon5.status)
    print(partyPokemon.Pokemon5.move1)
    print(partyPokemon.Pokemon5.move1PP)
    print(partyPokemon.Pokemon5.move2)
    print(partyPokemon.Pokemon5.move2PP)
    print(partyPokemon.Pokemon5.move3)
    print(partyPokemon.Pokemon5.move3PP)
    print(partyPokemon.Pokemon5.move4)
    print(partyPokemon.Pokemon5.move4PP)

    print(partyPokemon.Pokemon6.species)
    print(partyPokemon.Pokemon6.hp)
    print(partyPokemon.Pokemon6.maxHp)
    print(partyPokemon.Pokemon6.level)
    print(partyPokemon.Pokemon6.status)
    print(partyPokemon.Pokemon6.move1)
    print(partyPokemon.Pokemon6.move1PP)
    print(partyPokemon.Pokemon6.move2)
    print(partyPokemon.Pokemon6.move2PP)
    print(partyPokemon.Pokemon6.move3)
    print(partyPokemon.Pokemon6.move3PP)
    print(partyPokemon.Pokemon6.move4)
    print(partyPokemon.Pokemon6.move4PP)
    


session.stop()
