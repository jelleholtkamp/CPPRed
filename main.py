import src.classes.PokemonData as PokemonData
import src.classes.Commands as Commands
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision
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
session = PyBoy(filename, window_type="headless" if quiet else "SDL2", scale=6, debug=quiet, sound=True)
session.set_emulation_speed(0)
assert session.cartridge_title() == "POKEMON RED"

startGame = Commands.StartGame()

startGame.Start(session)

while not session.tick():
    battle = GameData.Battle()   
    battle.Update(session)
    print(battle.turn)


        


session.stop()
