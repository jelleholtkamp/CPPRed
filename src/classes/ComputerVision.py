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

class Screenshot:
    def GameWindow(outputPath):
        gameWindow = FindStuff.GameWindow()
        screenshot = pyautogui.screenshot(region=(gameWindow.startX,gameWindow.startY,gameWindow.width,gameWindow.height))
        screenshot.save(outputPath)
        return screenshot

class MatchTemplate: 
    def OnScreen(templatePath, threshold, masks = None):
        debugPath = "Debug\MatchTemplate\OnScreen"
        result = None
        screenshot = pyautogui.screenshot()
        screenshotDebugPath = debugPath + "\screenshot.png"
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        if masks != None:
            for mask in masks:
                screenshotMaskedDebugPath = debugPath + "\screenshotMasked.png"
                cv2.rectangle(screenshot, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
                cv2.imwrite(screenshotMaskedDebugPath, screenshot)
            
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


    def InGameWindow(templatePath, threshold, masks = None):
        debugPath = "Debug\MatchTemplate\InGameWindow"
        result = None

        screenshotDebugPath = debugPath + "\screenshot.png"
        screenshot = Screenshot.GameWindow(screenshotDebugPath)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        for mask in masks:
            screenshotMaskedDebugPath = debugPath + "\screenshotMasked.png"
            cv2.rectangle(screenshot, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
            cv2.imwrite(screenshotMaskedDebugPath, screenshot)
            
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
    def WindowBar():
        WindowBarLocation = MatchTemplate.OnScreen("TemplateMatching\WindowBar.png",0.8)
        if WindowBarLocation != None:
            global WindowBar
            WindowBar = WindowBarLocation
            return WindowBar
        else:
            return "NotFound"
        
    def GameWindow():
        if 'WindowBar' not in globals():
            WindowBar = FindStuff.WindowBar()

        if WindowBar != None or WindowBar != "NotFound":
            startX = WindowBar.startX
            endX = WindowBar.endX
            startY = WindowBar.startY + WindowBar.height
            endY = WindowBar.endY + 864 
            result = MatchResult(startX,startY,endX,endY)
            pyautogui.screenshot(region=(startX,startY,result.width,result.height)).save("Debug\GameWindow\screenshot.png")
            return result
        
    def ConvoBar():
        masks = [
            {
                "startX": 40,
                "startY": 624,
                "endX": 912,
                "endY": 816
            }
        ]
        convoBar = MatchTemplate.InGameWindow("TemplateMatching\\Convo.png", 0.8, masks)

        if convoBar != None:
            return convoBar    
        else:
            return "NotFound"
        
    def NurseJoyDialogBox():
        masks = [
            {
                "startX": 576,
                "startY": 376,
                "endX": 616,
                "endY": 528
            }
        ]
        convoBar = MatchTemplate.InGameWindow("TemplateMatching\\NurseJoyDialogBox.png", 0.8, masks)

        if convoBar != None:
            return convoBar    
        else:
            return "NotFound"