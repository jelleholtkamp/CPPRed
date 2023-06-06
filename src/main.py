import classes.PokemonData as PokemonData
import classes.Commands as Commands
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
pyboy = PyBoy(filename, window_type="headless" if quiet else "SDL2", window_scale=3, debug=quiet, game_wrapper=True)
pyboy.set_emulation_speed(0)
assert pyboy.cartridge_title() == "POKEMON RED"

startGame = Commands.StartGame()

startGame.Start(pyboy)

while not pyboy.tick():
    print("Game Started")

pyboy.stop()
