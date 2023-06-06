from pyboy import PyBoy
pyboy = PyBoy('../Roms/Red.gb')
while not pyboy.tick():
    pass
pyboy.stop()