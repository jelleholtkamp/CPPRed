from pyboy.utils import WindowEvent
import logging
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision
import src.classes.PokemonData as pokemonData
import numpy
import PIL
import pyboy

class StartGame():
    def __init__(self):
        self.Started = 0

    def Start(self, pyboy):
        # cursorPosition = pyboy.get_memory_value(0xCC26)
        # menuBitmask = pyboy.get_memory_value(0xCC29)

        # while not (cursorPosition == 0 and menuBitmask == 11):
        #     cursorPosition = pyboy.get_memory_value(0xCC26)
        #     menuBitmask = pyboy.get_memory_value(0xCC29)
        #     pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        #     pyboy.tick() 
        #     pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        #     pyboy.tick() 
        #     pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        #     pyboy.tick() 
        #     pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)            
       
        # pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        # pyboy.tick() 
        # pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        # for i in range(0, 100):
        #     pyboy.tick()
        # pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        # pyboy.tick() 
        # pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        # for i in range(0, 100):
        #             pyboy.tick()
        self.Started = 1

        # while  pyboy.get_memory_value(0xCC26) != 0 and pyboy.get_memory_value(0xCC29) != 11:
        #     print("Waiting for game to start...")
        #     pyboy.tick()
class PressButton():
    def A(session):
        logging.info("Pressing A")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_A)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_A)
        for i in range(0, tickSlack):
            session.tick()

    def B(session):
        logging.info("Pressing B")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_B)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_B)
        for i in range(0, tickSlack):
            session.tick()
    def Up(session):
        logging.info("Pressing Up")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_UP)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_UP)
        for i in range(0, tickSlack):
            session.tick()
    def Down(session):
        logging.info("Pressing Down")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_DOWN)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_DOWN)
        for i in range(0, tickSlack):
            session.tick()
    def Left(session):
        logging.info("Pressing Left")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_LEFT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        for i in range(0, tickSlack):
            session.tick()
    def Right(session):
        logging.info("Pressing Right")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()

    def Start(session):
        logging.info("Pressing Start")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_START)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_START)
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
    def Select(session):
        logging.info("Pressing Select")
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
        tickSlack = 100
        for i in range(0, tickSlack):
            session.tick()
class MoveCursor():
    def Move(start, target, session, delimit = None):
        moves = int(target) - int(start)
        logging.info("Moves required: " + str(moves))
        if moves > 0:
            logging.info("Moving cursor down" + str(moves) + " times")
            for i in range(0, moves):
                PressButton.Down(session)
                i += 1

        elif moves < 0:
            moves = moves * -1
            logging.info("Moving cursor up" + str(moves) + " times")
            for i in range(0, moves):
                PressButton.Up(session)
                i += 1  

class PlayerFeedback():
    def Get(options):
        i = 1
        for option in options:
            print(str(i) + ": " + option.get(i))
            i += 1
        playerInput = input("Select an option: ")
        return playerInput

class Dialog:
    # TODO: I should check out the sprite map functions of PyBoy to check if i am talking to a certain npc
    def NurseJoy(session):
        checkDialogBox = ComputerVision.FindStuff.NurseJoyDialogBox(session)
        if checkDialogBox != None and checkDialogBox != "NotFound":
            options = [
                {
                    1 : "Heal"
                },
                {
                    2 : "Cancel"
                }
            ]
            position = GameData.CursorPosition.Get(session)
            choice = int(PlayerFeedback.Get(options)) - 1
            MoveCursor.Move(position, choice, session)

            if (choice == 0):    
                PressButton.A(session)
                for i in range(0, 500):
                    session.tick()
                PressButton.B(session)
                PressButton.B(session)
                PressButton.B(session)

            if (choice == 1):
                PressButton.A(session)
                PressButton.B(session)               
        
    def PC(session):
        check = ComputerVision.FindStuff.PCDialogBox()
        if check != None and check != "NotFound":
            options = [
                {
                    1 : "Bill's PC"
                },
                {
                    2 : "<--Player-->'s PC"
                },
                {
                    3 : "Prof. Oak's PC"
                },
                {
                    4 : "Log Off"
                }
            ]
            position = GameData.CursorPosition.Get(session)
            choice = int(PlayerFeedback.Get(options)) - 1
            MoveCursor.Move(position, choice, session)
            
            if choice == 0:

                PressButton.A(session)
                PressButton.A(session)
                PressButton.A(session)

                Dialog.BillsPC(session)

    def BillsPC(session):
        options = [
            {
                1 : "Withdraw"
            },
            {
                2 : "Deposit"
            },
            {
                3 : "Release"
            },
            {
                4 : "Change Box"
            },
            {
                5 : "See ya!"
            }
        ]
        position = GameData.CursorPosition.Get(session)
        choice = int(PlayerFeedback.Get(options)) - 1
        MoveCursor.Move(position, choice, session)

        if choice == 0:
            PressButton.A(session)
            Dialog.BillsPCBox(session)

    def BillsPCBox(session):
        options = []
        pokemon1 = session.get_memory_value(0xDA81)
        if pokemon1 != None:
            pokemon1Species = pokemonData.PokemonSpecies.Get(pokemon1)
            logging.info("Pokemon 1: " + str(pokemon1Species))
            options.append(
                {
                    1: pokemon1Species
                }
            )
        pokemon2 = session.get_memory_value(0xDA82)
        if pokemon2 != None:
            pokemon2Species = pokemonData.PokemonSpecies.Get(pokemon2)
            if pokemon2Species != None:
                logging.info("Pokemon 2: " + str(pokemon2Species))
                options.append(
                    {
                        2: pokemon2Species
                    }
)
        pokemon3 = session.get_memory_value(0xDA83)
        if pokemon3 != None:
            pokemon3Species = pokemonData.PokemonSpecies.Get(pokemon3)
            pokemon3Species = pokemonData.PokemonSpecies.Get(pokemon3)
            if pokemon3Species != None:
                logging.info("Pokemon 3: " + str(pokemon3Species))
                options.append(
                    {
                        3: pokemon3Species
                    }
                )
        pokemon4 = session.get_memory_value(0xDA84)
        if pokemon4 != None:
            pokemon4Species = pokemonData.PokemonSpecies.Get(pokemon4)
            if pokemon4Species != None:
                logging.info("Pokemon 4: " + str(pokemon4Species))
                options.append(
                    {
                        4: pokemon4Species
                    }
                )
        pokemon5 = session.get_memory_value(0xDA85)
        if pokemon5 != None:
            pokemon5Species = pokemonData.PokemonSpecies.Get(pokemon5)
            if pokemon5Species != None:
                logging.info("Pokemon 5: " + str(pokemon5Species))
                options.append(
                    {
                        5: pokemon5Species
                    }
                )
        pokemon6 = session.get_memory_value(0xDA86)
        if pokemon6 != None:
            pokemon6Species = pokemonData.PokemonSpecies.Get(pokemon6)
            if pokemon6Species != None:
                logging.info("Pokemon 6: " + str(pokemon6Species))
                options.append(
                    {
                        6: pokemon6Species
                    }
                )
        pokemon7 = session.get_memory_value(0xDA87)
        if pokemon7 != None:
            pokemon7Species = pokemonData.PokemonSpecies.Get(pokemon7)
            if pokemon7Species != None:
                logging.info("Pokemon 7: " + str(pokemon7Species))
                options.append(
                    {
                        7: pokemon7Species
                    }
                )
        pokemon8 = session.get_memory_value(0xDA88)
        if pokemon8 != None:
            pokemon8Species = pokemonData.PokemonSpecies.Get(pokemon8)
            if pokemon8Species != None:
                logging.info("Pokemon 8: " + str(pokemon8Species))
                options.append(
                    {
                        8: pokemon8Species
                    }
                )
        pokemon9 = session.get_memory_value(0xDA89)
        if pokemon9 != None:
            pokemon9Species = pokemonData.PokemonSpecies.Get(pokemon9)
            if pokemon9Species != None:
                logging.info("Pokemon 9: " + str(pokemon9Species))
                options.append(
                    {
                        9: pokemon9Species
                    }
                )
        pokemon10 = session.get_memory_value(0xDA8A)
        if pokemon10 != None:
            pokemon10Species = pokemonData.PokemonSpecies.Get(pokemon10)
            if pokemon10Species != None:
                logging.info("Pokemon 10: " + str(pokemon10Species))
                options.append(
                    {
                        10: pokemon10Species
                    }
                )
        pokemon11 = session.get_memory_value(0xDA8B)
        if pokemon11 != None:
            pokemon11Species = pokemonData.PokemonSpecies.Get(pokemon11)
            if pokemon11Species != None:
                logging.info("Pokemon 11: " + str(pokemon11Species))
                options.append(str(
                    {
                        11: pokemon11Species
                    }
                ))
        pokemon12 = session.get_memory_value(0xDA8C)
        if pokemon12 != None:
            pokemon12Species = pokemonData.PokemonSpecies.Get(pokemon12)
            if pokemon12Species != None:
                logging.info("Pokemon 12: " + str(pokemon12Species))
                options.append(str(
                    {
                        12: pokemon12Species
                    }
                ))
        pokemon13 = session.get_memory_value(0xDA8D)
        if pokemon13 != None:
            pokemon13Species = pokemonData.PokemonSpecies.Get(pokemon13)
            if pokemon13Species != None:
                logging.info("Pokemon 13: " + str(pokemon13Species))
                options.append(str(
                    {
                        13: pokemon13Species
                    }
                ))
        pokemon14 = session.get_memory_value(0xDA8E)
        if pokemon14 != None:
            pokemon14Species = pokemonData.PokemonSpecies.Get(pokemon14)
            if pokemon14Species != None:
                logging.info("Pokemon 14: " + str(pokemon14Species))
                options.append(
                    {
                        14: pokemon14Species
                    }
                )
        pokemon15 = session.get_memory_value(0xDA8F)
        if pokemon15 != None:
            pokemon15Species = pokemonData.PokemonSpecies.Get(pokemon15)
            if pokemon15Species != None:
                logging.info("Pokemon 15: " + str(pokemon15Species))
                options.append(
                    {
                        15: pokemon15Species
                    }
                )
        pokemon16 = session.get_memory_value(0xDA90)
        if pokemon16 != None:
            pokemon16Species = pokemonData.PokemonSpecies.Get(pokemon16)
            if pokemon16Species != None:
                logging.info("Pokemon 16: " + str(pokemon16Species))
                options.append(
                    {
                        16: pokemon16Species
                    }
                )
        pokemon17 = session.get_memory_value(0xDA91)
        if pokemon17 != None:
            pokemon17Species = pokemonData.PokemonSpecies.Get(pokemon17)
            if pokemon17Species != None:
                logging.info("Pokemon 17: " + str(pokemon17Species))
                options.append(
                    {
                        17: pokemon17Species
                    }
                )
        pokemon18 = session.get_memory_value(0xDA92)
        if pokemon18 != None:
            pokemon18Species = pokemonData.PokemonSpecies.Get(pokemon18)
            if pokemon18Species != None:
                logging.info("Pokemon 18: " + str(pokemon18Species))
                options.append(
                    {
                        18: pokemon18Species
                    }
                )
        pokemon19 = session.get_memory_value(0xDA93)
        if pokemon19 != None:
            pokemon19Species = pokemonData.PokemonSpecies.Get(pokemon19)
            if pokemon19Species != None:
                logging.info("Pokemon 19: " + str(pokemon19Species))
                options.append(
                    {
                        19: pokemon19Species
                    }
                )
        pokemon20 = session.get_memory_value(0xDA94)
        if pokemon20 != None:
            pokemon20Species = pokemonData.PokemonSpecies.Get(pokemon20)
            if pokemon20Species != None:
                logging.info("Pokemon 20: " + str(pokemon20Species))
                options.append(
                    {
                        20: pokemon20Species
                    }
                )
 
        position = GameData.CursorPosition.Get(session)
        choice = int(PlayerFeedback.Get(options)) - 1
        MoveCursor.Move(position, choice, session)

        PressButton.A(session)
        Dialog.WithdrawPokemon(session)
    
    def WithdrawPokemon(session):
        options = [
            {
                1 : "Withdraw"
            },
            {
                2 : "Stats"
            },
            {
                3 : "Cancel"
            }
        ]
        position = GameData.CursorPosition.Get(session)
        choice = int(PlayerFeedback.Get(options)) - 1
        MoveCursor.Move(position, choice, session)
        PressButton.A(session)

class Debug:
    def SpriteFarm(session):
        outputPath = 'Debug\\SpriteFarm\\Spritefarm.txt'
        file = open(outputPath, 'w')
        file.close()
        file = open(outputPath, 'a')

        # Farm sprite0
        sprite00 = session.botsupport_manager().sprite(0)
        sprite01 = session.botsupport_manager().sprite(1)
        sprite02 = session.botsupport_manager().sprite(2)
        sprite03 = session.botsupport_manager().sprite(3)

        sprite00TileId = sprite00.tiles[0].tile_identifier
        sprite00Tile = session.botsupport_manager().tile(sprite00TileId).image_ndarray()

        sprite01TileId = sprite01.tiles[0].tile_identifier
        sprite01Tile = session.botsupport_manager().tile(sprite01TileId).image_ndarray()

        sprite02TileId = sprite02.tiles[0].tile_identifier
        sprite02Tile = session.botsupport_manager().tile(sprite02TileId).image_ndarray()
       
        sprite03TileId = sprite03.tiles[0].tile_identifier
        sprite03Tile = session.botsupport_manager().tile(sprite03TileId).image_ndarray()
       
        sprite00TopHalf = numpy.concatenate((sprite00Tile, sprite01Tile), axis=1)
        sprite00BottomHalf = numpy.concatenate((sprite02Tile, sprite03Tile), axis=1)
        sprite00Full = numpy.concatenate((sprite00TopHalf, sprite00BottomHalf), axis=0)

        sprite00FullPIL = PIL.Image.fromarray(sprite00Full)
        sprite00FullPIL.save('Debug\\SpriteFarm\\sprite00.png')

        # Farm sprite1
        sprite10 = session.botsupport_manager().sprite(4)
        sprite11 = session.botsupport_manager().sprite(5)
        sprite12 = session.botsupport_manager().sprite(6)
        sprite13 = session.botsupport_manager().sprite(7)

        sprite10TileId = sprite10.tiles[0].tile_identifier
        sprite10Tile = session.botsupport_manager().tile(sprite10TileId).image_ndarray()

        sprite11TileId = sprite11.tiles[0].tile_identifier
        sprite11Tile = session.botsupport_manager().tile(sprite11TileId).image_ndarray()

        sprite12TileId = sprite12.tiles[0].tile_identifier
        sprite12Tile = session.botsupport_manager().tile(sprite12TileId).image_ndarray()
       
        sprite13TileId = sprite13.tiles[0].tile_identifier
        sprite13Tile = session.botsupport_manager().tile(sprite13TileId).image_ndarray()
       
        sprite10TopHalf = numpy.concatenate((sprite10Tile, sprite11Tile), axis=1)
        sprite10BottomHalf = numpy.concatenate((sprite12Tile, sprite13Tile), axis=1)
        sprite10Full = numpy.concatenate((sprite10TopHalf, sprite10BottomHalf), axis=0)

        sprite10FullPIL = PIL.Image.fromarray(sprite10Full)
        sprite10FullPIL.save('Debug\\SpriteFarm\\sprite10.png')

        # Farm sprite2
        sprite20 = session.botsupport_manager().sprite(8)
        sprite21 = session.botsupport_manager().sprite(9)
        sprite22 = session.botsupport_manager().sprite(10)
        sprite23 = session.botsupport_manager().sprite(11)

        sprite20TileId = sprite20.tiles[0].tile_identifier
        sprite20Tile = session.botsupport_manager().tile(sprite20TileId).image_ndarray()

        sprite21TileId = sprite21.tiles[0].tile_identifier
        sprite21Tile = session.botsupport_manager().tile(sprite21TileId).image_ndarray()

        sprite22TileId = sprite22.tiles[0].tile_identifier
        sprite22Tile = session.botsupport_manager().tile(sprite22TileId).image_ndarray()
       
        sprite23TileId = sprite23.tiles[0].tile_identifier
        sprite23Tile = session.botsupport_manager().tile(sprite23TileId).image_ndarray()
       
        sprite20TopHalf = numpy.concatenate((sprite20Tile, sprite21Tile), axis=1)
        sprite20BottomHalf = numpy.concatenate((sprite22Tile, sprite23Tile), axis=1)
        sprite20Full = numpy.concatenate((sprite20TopHalf, sprite20BottomHalf), axis=0)

        sprite20FullPIL = PIL.Image.fromarray(sprite20Full)
        sprite20FullPIL.save('Debug\\SpriteFarm\\sprite20.png')

        # Farm sprite3
        sprite30 = session.botsupport_manager().sprite(12)
        sprite31 = session.botsupport_manager().sprite(13)
        sprite32 = session.botsupport_manager().sprite(14)
        sprite33 = session.botsupport_manager().sprite(15)

        sprite30TileId = sprite30.tiles[0].tile_identifier
        sprite30Tile = session.botsupport_manager().tile(sprite30TileId).image_ndarray()

        sprite31TileId = sprite31.tiles[0].tile_identifier
        sprite31Tile = session.botsupport_manager().tile(sprite31TileId).image_ndarray()

        sprite32TileId = sprite32.tiles[0].tile_identifier
        sprite32Tile = session.botsupport_manager().tile(sprite32TileId).image_ndarray()
       
        sprite33TileId = sprite33.tiles[0].tile_identifier
        sprite33Tile = session.botsupport_manager().tile(sprite33TileId).image_ndarray()
       
        sprite30TopHalf = numpy.concatenate((sprite30Tile, sprite31Tile), axis=1)
        sprite30BottomHalf = numpy.concatenate((sprite32Tile, sprite33Tile), axis=1)
        sprite30Full = numpy.concatenate((sprite30TopHalf, sprite30BottomHalf), axis=0)

        sprite30FullPIL = PIL.Image.fromarray(sprite30Full)
        sprite30FullPIL.save('Debug\\SpriteFarm\\sprite30.png')

        # Farm sprite4
        sprite40 = session.botsupport_manager().sprite(16)
        sprite41 = session.botsupport_manager().sprite(17)
        sprite42 = session.botsupport_manager().sprite(18)
        sprite43 = session.botsupport_manager().sprite(19)

        sprite40TileId = sprite40.tiles[0].tile_identifier
        sprite40Tile = session.botsupport_manager().tile(sprite40TileId).image_ndarray()

        sprite41TileId = sprite41.tiles[0].tile_identifier
        sprite41Tile = session.botsupport_manager().tile(sprite41TileId).image_ndarray()

        sprite42TileId = sprite42.tiles[0].tile_identifier
        sprite42Tile = session.botsupport_manager().tile(sprite42TileId).image_ndarray()
       
        sprite43TileId = sprite43.tiles[0].tile_identifier
        sprite43Tile = session.botsupport_manager().tile(sprite43TileId).image_ndarray()
       
        sprite40TopHalf = numpy.concatenate((sprite40Tile, sprite41Tile), axis=1)
        sprite40BottomHalf = numpy.concatenate((sprite42Tile, sprite43Tile), axis=1)
        sprite40Full = numpy.concatenate((sprite40TopHalf, sprite40BottomHalf), axis=0)

        sprite40FullPIL = PIL.Image.fromarray(sprite40Full)
        sprite40FullPIL.save('Debug\\SpriteFarm\\sprite40.png')

        # Farm sprite5
        sprite50 = session.botsupport_manager().sprite(20)
        sprite51 = session.botsupport_manager().sprite(21)
        sprite52 = session.botsupport_manager().sprite(22)
        sprite53 = session.botsupport_manager().sprite(23)

        sprite50TileId = sprite50.tiles[0].tile_identifier
        sprite50Tile = session.botsupport_manager().tile(sprite50TileId).image_ndarray()

        sprite51TileId = sprite51.tiles[0].tile_identifier
        sprite51Tile = session.botsupport_manager().tile(sprite51TileId).image_ndarray()

        sprite52TileId = sprite52.tiles[0].tile_identifier
        sprite52Tile = session.botsupport_manager().tile(sprite52TileId).image_ndarray()
       
        sprite53TileId = sprite53.tiles[0].tile_identifier
        sprite53Tile = session.botsupport_manager().tile(sprite53TileId).image_ndarray()
       
        sprite50TopHalf = numpy.concatenate((sprite50Tile, sprite51Tile), axis=1)
        sprite50BottomHalf = numpy.concatenate((sprite52Tile, sprite53Tile), axis=1)
        sprite50Full = numpy.concatenate((sprite50TopHalf, sprite50BottomHalf), axis=0)

        sprite50FullPIL = PIL.Image.fromarray(sprite50Full)
        sprite50FullPIL.save('Debug\\SpriteFarm\\sprite50.png')

        # Farm sprite6
        sprite60 = session.botsupport_manager().sprite(24)
        sprite61 = session.botsupport_manager().sprite(25)
        sprite62 = session.botsupport_manager().sprite(26)
        sprite63 = session.botsupport_manager().sprite(27)

        sprite60TileId = sprite60.tiles[0].tile_identifier
        sprite60Tile = session.botsupport_manager().tile(sprite60TileId).image_ndarray()

        sprite61TileId = sprite61.tiles[0].tile_identifier
        sprite61Tile = session.botsupport_manager().tile(sprite61TileId).image_ndarray()

        sprite62TileId = sprite62.tiles[0].tile_identifier
        sprite62Tile = session.botsupport_manager().tile(sprite62TileId).image_ndarray()
       
        sprite63TileId = sprite63.tiles[0].tile_identifier
        sprite63Tile = session.botsupport_manager().tile(sprite63TileId).image_ndarray()
       
        sprite60TopHalf = numpy.concatenate((sprite60Tile, sprite61Tile), axis=1)
        sprite60BottomHalf = numpy.concatenate((sprite62Tile, sprite63Tile), axis=1)
        sprite60Full = numpy.concatenate((sprite60TopHalf, sprite60BottomHalf), axis=0)

        sprite60FullPIL = PIL.Image.fromarray(sprite60Full)
        sprite60FullPIL.save('Debug\\SpriteFarm\\sprite60.png')

        # Farm sprite7
        sprite70 = session.botsupport_manager().sprite(28)
        sprite71 = session.botsupport_manager().sprite(29)
        sprite72 = session.botsupport_manager().sprite(30)
        sprite73 = session.botsupport_manager().sprite(31)

        sprite70TileId = sprite70.tiles[0].tile_identifier
        sprite70Tile = session.botsupport_manager().tile(sprite70TileId).image_ndarray()

        sprite71TileId = sprite71.tiles[0].tile_identifier
        sprite71Tile = session.botsupport_manager().tile(sprite71TileId).image_ndarray()

        sprite72TileId = sprite72.tiles[0].tile_identifier
        sprite72Tile = session.botsupport_manager().tile(sprite72TileId).image_ndarray()
       
        sprite73TileId = sprite73.tiles[0].tile_identifier
        sprite73Tile = session.botsupport_manager().tile(sprite73TileId).image_ndarray()
       
        sprite70TopHalf = numpy.concatenate((sprite70Tile, sprite71Tile), axis=1)
        sprite70BottomHalf = numpy.concatenate((sprite72Tile, sprite73Tile), axis=1)
        sprite70Full = numpy.concatenate((sprite70TopHalf, sprite70BottomHalf), axis=0)

        sprite70FullPIL = PIL.Image.fromarray(sprite70Full)
        sprite70FullPIL.save('Debug\\SpriteFarm\\sprite70.png')

        # Farm sprite8
        sprite80 = session.botsupport_manager().sprite(32)
        sprite81 = session.botsupport_manager().sprite(33)
        sprite82 = session.botsupport_manager().sprite(34)
        sprite83 = session.botsupport_manager().sprite(35)

        sprite80TileId = sprite80.tiles[0].tile_identifier
        sprite80Tile = session.botsupport_manager().tile(sprite80TileId).image_ndarray()

        sprite81TileId = sprite81.tiles[0].tile_identifier
        sprite81Tile = session.botsupport_manager().tile(sprite81TileId).image_ndarray()

        sprite82TileId = sprite82.tiles[0].tile_identifier
        sprite82Tile = session.botsupport_manager().tile(sprite82TileId).image_ndarray()
       
        sprite83TileId = sprite83.tiles[0].tile_identifier
        sprite83Tile = session.botsupport_manager().tile(sprite83TileId).image_ndarray()
       
        sprite80TopHalf = numpy.concatenate((sprite80Tile, sprite81Tile), axis=1)
        sprite80BottomHalf = numpy.concatenate((sprite82Tile, sprite83Tile), axis=1)
        sprite80Full = numpy.concatenate((sprite80TopHalf, sprite80BottomHalf), axis=0)

        sprite80FullPIL = PIL.Image.fromarray(sprite80Full)
        sprite80FullPIL.save('Debug\\SpriteFarm\\sprite80.png')

        # Farm sprite9
        sprite90 = session.botsupport_manager().sprite(36)
        sprite91 = session.botsupport_manager().sprite(37)
        sprite92 = session.botsupport_manager().sprite(38)
        sprite93 = session.botsupport_manager().sprite(39)

        sprite90TileId = sprite90.tiles[0].tile_identifier
        sprite90Tile = session.botsupport_manager().tile(sprite90TileId).image_ndarray()

        sprite91TileId = sprite91.tiles[0].tile_identifier
        sprite91Tile = session.botsupport_manager().tile(sprite91TileId).image_ndarray()

        sprite92TileId = sprite92.tiles[0].tile_identifier
        sprite92Tile = session.botsupport_manager().tile(sprite92TileId).image_ndarray()
       
        sprite93TileId = sprite93.tiles[0].tile_identifier
        sprite93Tile = session.botsupport_manager().tile(sprite93TileId).image_ndarray()
       
        sprite90TopHalf = numpy.concatenate((sprite90Tile, sprite91Tile), axis=1)
        sprite90BottomHalf = numpy.concatenate((sprite92Tile, sprite93Tile), axis=1)
        sprite90Full = numpy.concatenate((sprite90TopHalf, sprite90BottomHalf), axis=0)

        sprite90FullPIL = PIL.Image.fromarray(sprite90Full)
        sprite90FullPIL.save('Debug\\SpriteFarm\\sprite90.png')
