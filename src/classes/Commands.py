from pyboy.utils import WindowEvent
import logging
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision
import src.classes.PokemonData as pokemonData
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



   