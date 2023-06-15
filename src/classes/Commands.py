from pyboy.utils import WindowEvent
import logging
import src.classes.GameData as GameData
import src.classes.ComputerVision as ComputerVision

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
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_A)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_A)
        session.tick()
        session.tick()

    def B(session):
        logging.info("Pressing B")
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_B)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_B)
        session.tick()
        session.tick()

    def Up(session):
        logging.info("Pressing Up")
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_UP)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_UP)
        session.tick()
        session.tick()

    def Down(session):
        logging.info("Pressing Down")
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_DOWN)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_DOWN)
        session.tick()
        session.tick()

    def Left(session):
        logging.info("Pressing Left")
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_LEFT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        session.tick()
        session.tick()

    def Right(session):
        logging.info("Pressing Right")
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        session.tick()
        session.tick()

    def Start(session):
        logging.info("Pressing Start")
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_START)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_START)
        session.tick()
        session.tick()
        
    def Select(session):
        logging.info("Pressing Select")
        session.tick()
        session.tick()
        session.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
        session.tick() 
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
    def NurseJoy(session):
        check = ComputerVision.FindStuff.NurseJoyDialogBox()
        if check != None and check != "NotFound":
            options = [
                "Heal",
                "Cancel"
            ]
            position = GameData.CursorPosition.Get(session)
            result = {
                "options": options,
                "selectedOption": options[position]
            }
            return result
        else:
            return None
        
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

            
            # return result
        else:
            return None
   