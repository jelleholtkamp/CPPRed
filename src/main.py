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
session = PyBoy(filename, window_type="headless" if quiet else "SDL2", scale=6, debug=quiet)
session.set_emulation_speed(0)
assert session.cartridge_title() == "POKEMON RED"

startGame = Commands.StartGame()

startGame.Start(session)

while not session.tick():
    battle = GameData.Battle()
    battle.Update(session)
    if battle.status == "InBattle":
        # print(battle.status)
        # print(battle.activePokemonSpecies)
        # print(battle.activePokemonLevel)
        # print(battle.activePokemonHP)
        # print(battle.activePokemonMaxHP)
        # print(battle.activePokemonStatus)
        # print(battle.activePokemonMove1)
        # print(battle.activePokemonMove2)
        # print(battle.activePokemonMove3)
        # print(battle.activePokemonMove4)
        # print(battle.activePokemonMove1PP)
        # print(battle.activePokemonMove2PP)
        # print(battle.activePokemonMove3PP)
        # print(battle.activePokemonMove4PP)

        # print(battle.enemyPokemonSpecies)
        # print(battle.enemyPokemonLevel)
        # print(battle.enemyPokemonHP)
        # print(battle.enemyPokemonStatus)

        cursorPosition = GameData.CursorPosition()
        cursorPosition.Update(session)

        # print("X:" + str(cursorPosition.x))
        # print("Y:" + str(cursorPosition.y))
        print(cursorPosition.selection)
        print(cursorPosition.menu)
        # print("LastMenuItemID" + str(cursorPosition.lastMenuItemId))
        # print("previouslySelectedMenuItemId" + str(cursorPosition.previouslySelectedMenuItemId))
        # print("lastPartyMenuPosition" + str(cursorPosition.lastPartyMenuPosition))
        # print("lastItemMenuPosition" + str(cursorPosition.lastItemMenuPosition))
        # print(cursorPosition.lastStartBattleMenuPosition)
        # print("lastStartBattleMenuPosition" + str(cursorPosition.firstDisplayedMenuItemId))
        # print("lastStartBattleMenuPosition" + str(cursorPosition.itemHighlitedWithSelect))

        


session.stop()
