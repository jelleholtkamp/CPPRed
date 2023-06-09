from pyboy.utils import WindowEvent
import src.classes.GameData as GameData

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
        session.send_input(WindowEvent.PRESS_BUTTON_A)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_A)
        session.tick()
    def B(session):
        session.send_input(WindowEvent.PRESS_BUTTON_B)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_B)
        session.tick()
    def Up(session):
        session.send_input(WindowEvent.PRESS_ARROW_UP)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_UP)
        session.tick()
    def Down(session):
        session.send_input(WindowEvent.PRESS_ARROW_DOWN)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_DOWN)
        session.tick()
    def Left(session):
        session.send_input(WindowEvent.PRESS_ARROW_LEFT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        session.tick()
    def Right(session):
        session.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        session.tick()
    def Start(session):
        session.send_input(WindowEvent.PRESS_BUTTON_START)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_START)
        session.tick()
    def Select(session):
        session.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        session.tick()
        session.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
        session.tick()         

class MoveCursor():
    def To(targetItem, session):
        cursorPosition = GameData.CursorPosition()
        cursorPosition.Update(session)

        if cursorPosition.menu == "Battle":
            if targetItem == "Fight":
                if cursorPosition.selection == "Fight":
                    return
                elif cursorPosition.selection == "Pokémon":
                    PressButton.Left(session)
                elif cursorPosition.selection == "Item":
                    PressButton.Up(session)
                elif cursorPosition.selection == "Run":
                    PressButton.Up(session)
                    PressButton.Left(session)
            elif targetItem == "Pokémon":
                if cursorPosition.selection == "Fight":
                    PressButton.Right(session)
                elif cursorPosition.selection == "Pokémon":
                    return
                elif cursorPosition.selection == "Item":
                    PressButton.Up(session)
                    PressButton.Right(session)
                elif cursorPosition.selection == "Run":
                    PressButton.Down(session)
            elif targetItem == "Item":
                if cursorPosition.selection == "Fight":
                    PressButton.Down(session)
                elif cursorPosition.selection == "Pokémon":
                    PressButton.Down(session)
                    PressButton.Left(session)
                elif cursorPosition.selection == "Item":
                    return
                elif cursorPosition.selection == "Run":
                    PressButton.left(session)
            elif targetItem == "Run":
                if cursorPosition.selection == "Fight":
                    PressButton.Right(session)
                    PressButton.Down(session)
                elif cursorPosition.selection == "Pokémon":
                    PressButton.Down(session)
                elif cursorPosition.selection == "Item":
                    PressButton.Right(session)
                elif cursorPosition.selection == "Run":
                    return



   