import src.classes.PokemonData as PokemonData
import src.classes.Commands as Commands
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision
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
session = PyBoy(filename, window_type="headless" if quiet else "SDL2", scale=6, debug=not quiet, sound=True, color_palette=(0xFFFFFF,0xFF8484,0x943A3A,0x000000))
session.set_emulation_speed(0)
assert session.cartridge_title() == "POKEMON RED"

startGame = Commands.StartGame()

startGame.Start(session)

while not session.tick():
    tick  = 0
    print("///////////////////////////Tick: ", tick, "///////////////////////////")
    sprite0 = session.botsupport_manager().sprite(0)
    sprite1 = session.botsupport_manager().sprite(1)
    sprite2 = session.botsupport_manager().sprite(2)
    sprite3 = session.botsupport_manager().sprite(3)
    print("PlayerT1X: ", sprite0.x, "PlayerT1Y: ", sprite0.y, "Tile Identifier: ", sprite0.tile_identifier)
    print("PlayerT2X: ", sprite1.x, "PlayerT2Y: ", sprite1.y, "Tile Identifier: ", sprite1.tile_identifier)
    print("PlayerT3X: ", sprite2.x, "PlayerT3Y: ", sprite2.y, "Tile Identifier: ", sprite2.tile_identifier)
    print("PlayerT4X: ", sprite3.x, "PlayerT4Y: ", sprite3.y, "Tile Identifier: ", sprite3.tile_identifier)

    sprite4 = session.botsupport_manager().sprite(4)
    sprite5 = session.botsupport_manager().sprite(5)
    sprite6 = session.botsupport_manager().sprite(6)
    sprite7 = session.botsupport_manager().sprite(7)
    print("NPC1T1X: ", sprite4.x, "NPC1T1Y: ", sprite4.y, "Tile Identifier: ", sprite4.tile_identifier)
    print("NPC1T2X: ", sprite5.x, "NPC1T2Y: ", sprite5.y, "Tile Identifier: ", sprite5.tile_identifier)
    print("NPC1T3X: ", sprite6.x, "NPC1T3Y: ", sprite6.y, "Tile Identifier: ", sprite6.tile_identifier)
    print("NPC1T4X: ", sprite7.x, "NPC1T4Y: ", sprite7.y, "Tile Identifier: ", sprite7.tile_identifier)

    sprite8 = session.botsupport_manager().sprite(8)
    sprite9 = session.botsupport_manager().sprite(9)
    sprite10 = session.botsupport_manager().sprite(10)
    sprite11 = session.botsupport_manager().sprite(11)
    print("NPC2T1X: ", sprite8.x, "NPC2T1Y: ", sprite8.y, "Tile Identifier: ", sprite8.tile_identifier)
    print("NPC2T2X: ", sprite9.x, "NPC2T2Y: ", sprite9.y, "Tile Identifier: ", sprite9.tile_identifier)
    print("NPC2T3X: ", sprite10.x, "NPC2T3Y: ", sprite10.y, "Tile Identifier: ", sprite10.tile_identifier)
    print("NPC2T4X: ", sprite11.x, "NPC2T4Y: ", sprite11.y, "Tile Identifier: ", sprite11.tile_identifier)

    sprite12 = session.botsupport_manager().sprite(12)
    sprite13 = session.botsupport_manager().sprite(13)
    sprite14 = session.botsupport_manager().sprite(14)
    sprite15 = session.botsupport_manager().sprite(15)
    print("NPC3T1X: ", sprite12.x, "NPC3T1Y: ", sprite12.y, "Tile Identifier: ", sprite12.tile_identifier)
    print("NPC3T2X: ", sprite13.x, "NPC3T2Y: ", sprite13.y, "Tile Identifier: ", sprite13.tile_identifier)
    print("NPC3T3X: ", sprite14.x, "NPC3T3Y: ", sprite14.y, "Tile Identifier: ", sprite14.tile_identifier)
    print("NPC3T4X: ", sprite15.x, "NPC3T4Y: ", sprite15.y, "Tile Identifier: ", sprite15.tile_identifier)

    sprite16 = session.botsupport_manager().sprite(16)
    sprite17 = session.botsupport_manager().sprite(17)
    sprite18 = session.botsupport_manager().sprite(18)
    sprite19 = session.botsupport_manager().sprite(19)
    print("NPC4T1X: ", sprite16.x, "NPC4T1Y: ", sprite16.y, "Tile Identifier: ", sprite16.tile_identifier)
    print("NPC4T2X: ", sprite17.x, "NPC4T2Y: ", sprite17.y, "Tile Identifier: ", sprite17.tile_identifier)
    print("NPC4T3X: ", sprite18.x, "NPC4T3Y: ", sprite18.y, "Tile Identifier: ", sprite18.tile_identifier)
    print("NPC4T4X: ", sprite19.x, "NPC4T4Y: ", sprite19.y, "Tile Identifier: ", sprite19.tile_identifier)

    sprite20 = session.botsupport_manager().sprite(20)
    sprite21 = session.botsupport_manager().sprite(21)
    sprite22 = session.botsupport_manager().sprite(22)
    sprite23 = session.botsupport_manager().sprite(23)
    print("NPC5T1X: ", sprite20.x, "NPC5T1Y: ", sprite20.y, "Tile Identifier: ", sprite20.tile_identifier)
    print("NPC5T2X: ", sprite21.x, "NPC5T2Y: ", sprite21.y, "Tile Identifier: ", sprite21.tile_identifier)
    print("NPC5T3X: ", sprite22.x, "NPC5T3Y: ", sprite22.y, "Tile Identifier: ", sprite22.tile_identifier)
    print("NPC5T4X: ", sprite23.x, "NPC5T4Y: ", sprite23.y, "Tile Identifier: ", sprite23.tile_identifier)

    sprite24 = session.botsupport_manager().sprite(24)
    sprite25 = session.botsupport_manager().sprite(25)
    sprite26 = session.botsupport_manager().sprite(26)
    sprite27 = session.botsupport_manager().sprite(27)
    print("NPC6T1X: ", sprite24.x, "NPC6T1Y: ", sprite24.y, "Tile Identifier: ", sprite24.tile_identifier)
    print("NPC6T2X: ", sprite25.x, "NPC6T2Y: ", sprite25.y, "Tile Identifier: ", sprite25.tile_identifier)
    print("NPC6T3X: ", sprite26.x, "NPC6T3Y: ", sprite26.y, "Tile Identifier: ", sprite26.tile_identifier)
    print("NPC6T4X: ", sprite27.x, "NPC6T4Y: ", sprite27.y, "Tile Identifier: ", sprite27.tile_identifier)

    sprite28 = session.botsupport_manager().sprite(28)
    sprite29 = session.botsupport_manager().sprite(29)
    sprite30 = session.botsupport_manager().sprite(30)
    sprite31 = session.botsupport_manager().sprite(31)
    print("NPC7T1X: ", sprite28.x, "NPC7T1Y: ", sprite28.y, "Tile Identifier: ", sprite28.tile_identifier)
    print("NPC7T2X: ", sprite29.x, "NPC7T2Y: ", sprite29.y, "Tile Identifier: ", sprite29.tile_identifier)
    print("NPC7T3X: ", sprite30.x, "NPC7T3Y: ", sprite30.y, "Tile Identifier: ", sprite30.tile_identifier)
    print("NPC7T4X: ", sprite31.x, "NPC7T4Y: ", sprite31.y, "Tile Identifier: ", sprite31.tile_identifier)

    sprite32 = session.botsupport_manager().sprite(32)
    sprite33 = session.botsupport_manager().sprite(33)
    sprite34 = session.botsupport_manager().sprite(34)
    sprite35 = session.botsupport_manager().sprite(35)
    print("NPC8T1X: ", sprite32.x, "NPC8T1Y: ", sprite32.y, "Tile Identifier: ", sprite32.tile_identifier)
    print("NPC8T2X: ", sprite33.x, "NPC8T2Y: ", sprite33.y, "Tile Identifier: ", sprite33.tile_identifier)
    print("NPC8T3X: ", sprite34.x, "NPC8T3Y: ", sprite34.y, "Tile Identifier: ", sprite34.tile_identifier)
    print("NPC8T4X: ", sprite35.x, "NPC8T4Y: ", sprite35.y, "Tile Identifier: ", sprite35.tile_identifier)

    sprite36 = session.botsupport_manager().sprite(36)
    sprite37 = session.botsupport_manager().sprite(37)
    sprite38 = session.botsupport_manager().sprite(38)
    sprite39 = session.botsupport_manager().sprite(39)
    print("NPC9T1X: ", sprite36.x, "NPC9T1Y: ", sprite36.y, "Tile Identifier: ", sprite36.tile_identifier)
    print("NPC9T2X: ", sprite37.x, "NPC9T2Y: ", sprite37.y, "Tile Identifier: ", sprite37.tile_identifier)
    print("NPC9T3X: ", sprite38.x, "NPC9T3Y: ", sprite38.y, "Tile Identifier: ", sprite38.tile_identifier)
    print("NPC9T4X: ", sprite39.x, "NPC9T4Y: ", sprite39.y, "Tile Identifier: ", sprite39.tile_identifier)

    for i in range(0, 500):
        tick = i
        session.tick()
        
session.stop()
