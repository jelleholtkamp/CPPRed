import src.classes.ComputerVision as ComputerVision
import src.classes.GameData as GameData

masks = [
    {
        "startX": 48,
        "startY": 80,
        "endX": 88,
        "endY": 432
    }
]
result = GameData.Battle.Update()
print(result.turn)
