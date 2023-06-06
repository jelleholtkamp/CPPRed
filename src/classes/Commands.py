from pyboy.utils import WindowEvent
import time

class StartGame():
    def __init__(self):
        self.Started = 0

    def Start(self, pyboy):
        cursorPosition = pyboy.get_memory_value(0xCC26)
        menuBitmask = pyboy.get_memory_value(0xCC29)

        while not (cursorPosition == 0 and menuBitmask == 11):
            cursorPosition = pyboy.get_memory_value(0xCC26)
            menuBitmask = pyboy.get_memory_value(0xCC29)
            pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
            pyboy.tick() 
            pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
            pyboy.tick() 
            pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
            pyboy.tick() 
            pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)            
       
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        pyboy.tick() 
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        for i in range(0, 100):
            pyboy.tick()
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        pyboy.tick() 
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)
        for i in range(0, 100):
                    pyboy.tick()
        self.Started = 1

        # while  pyboy.get_memory_value(0xCC26) != 0 and pyboy.get_memory_value(0xCC29) != 11:
        #     print("Waiting for game to start...")
        #     pyboy.tick()