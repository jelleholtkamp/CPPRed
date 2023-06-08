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
        self.width = endX - startX
        self.height = endY - startY  

class MatchTemplate:
    def OnScreen(templatePath, threshold, debugPath):
        result = None
        screenshot = pyautogui.screenshot()
        screenshotDebugPath = debugPath + "\screenshot.png"
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(screenshotDebugPath, screenshot)
            
        template = cv2.imread(templatePath, 0)  

        w, h = template.shape[::-1]

        matchResult = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        location = np.where(matchResult >= threshold)
        for pt in zip(*location[::-1]):
            cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
            if pt != None:
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)
                (startX, startY) = maxLoc
                endX = startX + template.shape[1]
                endY = startY + template.shape[0]
                result = MatchResult(startX,startY,endX,endY)
                cv2.imwrite(screenshotDebugPath, screenshot)
                return result

class FindStuff:
    def GameWindow():
        menuBar = MatchTemplate.OnScreen("C:\data\git\jelleholtkamp\CPPRed\TemplateMatching\WindowBar.png",0.8,"C:\data\git\jelleholtkamp\CPPRed\Debug\WindowBar")
        if menuBar != None:
            startX = menuBar.startX
            endX = menuBar.endX
            startY = menuBar.startY + menuBar.height
            endY = menuBar.endY + 864 
            result = MatchResult(startX,startY,endX,endY)
            pyautogui.screenshot(region=(startX,startY,result.width,result.height)).save("C:\data\git\jelleholtkamp\CPPRed\Debug\GameWindow\screenshot.png")
            return result