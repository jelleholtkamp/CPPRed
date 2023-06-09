import src.classes.ComputerVision as ComputerVision

masks = [
    {
        "startX": 48,
        "startY": 80,
        "endX": 88,
        "endY": 432
    }
]
result = ComputerVision.FindStuff.PCDialogBox()

print(result.startX)