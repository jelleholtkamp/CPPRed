import src.classes.ComputerVision as ComputerVision

masks = [
    {
        "startX": 40,
        "startY": 624,
        "endX": 912,
        "endY": 816
    }
]
# for mask in masks:
#     print (mask["startX"])
result = ComputerVision.MatchTemplate.InGameWindow("TemplateMatching\\Convo.png", 0.8, masks)
