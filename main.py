import src.classes.PokemonData as PokemonData
import src.classes.Commands as Commands
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision
import src.classes.Debug as Debug
import os
import sys
import logging
from pyboy import PyBoy, WindowEvent
from pyboy import botsupport

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
session = PyBoy(filename, window_type="headless" if quiet else "SDL2", scale=6, debug=quiet, sound=True, color_palette=(0xFFFFFF,0xFF8484,0x943A3A,0x000000))
session.set_emulation_speed(0)
assert session.cartridge_title() == "POKEMON RED"

startGame = Commands.StartGame()

startGame.Start(session)

while not session.tick():
    for i in range(0, 1000):
        session.tick()
    choice = input("Enter command: ")
    if choice == "gos":
        GameData.Sprites.OnScreen(session)
    elif choice == "sf":
        Debug.Debug.SpriteFarm(session)
    elif choice == "nss":
        Debug.Debug.NewSpriteSheet()
    elif choice == "uss":
        Debug.Debug.UpdateSpriteSheet()
    elif choice == "gia":
        GameData.Items.GetMemoryAddress("Poké Ball")
    elif choice == "gin":
        GameData.Items.GetItemName("4")
    elif choice == "gpn":
        GameData.Pokemon.GetPokemonName("1")
    elif choice == "gpa":
        GameData.Pokemon.GetMemoryAddress("Charmander")
    elif choice == "sbi":
        itemChoice = input("Enter item name: ")
        quantityChoice = int(input("Enter quantity (0-99)"))
        indexChoice = input("Enter index (0-19, first item is 0)")
        GameData.Items.SetBagItem(session, indexChoice, itemChoice, quantityChoice)
    else:
        print("Unknown command")

        
session.stop()
