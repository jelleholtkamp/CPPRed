import pyautogui
import cv2
import numpy as np
import os
import sys
from matplotlib import pyplot as plt

class MatchResult:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
    

class MatchTemplate:
    def OnScreen(templatePath, threshold, debugPath):
        screenshot = pyautogui.screenshot()
        # screenshotDebugPath = debugPath + "\screenshot.png"
        # cv2.imwrite(screenshotDebugPath, screenshot)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        print(templatePath)
            
        template = cv2.imread(templatePath, 0)  

        w, h = template.shape[::-1]

        matchResult = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        location = np.where(matchResult >= threshold)
        for pt in zip(*location[::-1]):
            cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            if pt != None:
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)
                (startX, startY) = maxLoc
                endX = startX + template.shape[1]
                endY = startY + template.shape[0]
                result = MatchResult(startX,startY,endX,endY)
                return result
