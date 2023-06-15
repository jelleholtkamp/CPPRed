import src.classes.PokemonData as PokemonData
import src.classes.Commands as Commands
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision
import os
import sys
import logging
from pyboy import PyBoy, WindowEvent

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

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
session = PyBoy(filename, color_palette=(0xFFFFFF,0x999999,0x555555,0x000000), window_type="headless" if quiet else "SDL2", scale=6, debug=quiet, sound=True)
session.set_emulation_speed(0)
assert session.cartridge_title() == "POKEMON RED"

startGame = Commands.StartGame()

startGame.Start(session)

while not session.tick():
    result = Commands.Dialog.PC(session)
    if result != None:
        print(result)   
    for i in range(0, 500):
        session.tick()
        
   

        


session.stop()
