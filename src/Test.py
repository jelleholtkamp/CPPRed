import classes.ComputerVision as ComputerVision
test = ComputerVision.MatchTemplate.OnScreen("C:\data\git\jelleholtkamp\CPPRed\TemplateMatching\WindowBar.png",0.8,"C:\data\git\jelleholtkamp\CPPRed\Debug\Test")
print(test.startX)
print(test.startY)
print(test.endX)
print(test.endY)