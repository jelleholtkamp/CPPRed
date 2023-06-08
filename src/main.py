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
    activePokemon = GameData.ActivePokemon()
    activePokemon.Update(session)
    print(activePokemon.species)
    print(activePokemon.level)
    print(activePokemon.status)
    print(activePokemon.hp)
    print(activePokemon.maxHp)
    print(activePokemon.move1)
    print(activePokemon.move1PP)
    print(activePokemon.move2)
    print(activePokemon.move2PP)
    print(activePokemon.move3)
    print(activePokemon.move3PP)
    print(activePokemon.move4)
    print(activePokemon.move4PP)



session.stop()
