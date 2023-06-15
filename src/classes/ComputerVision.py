import pyautogui
import cv2
import numpy as np
import logging
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
        if gameWindow != None and gameWindow != "NotFound":
            logging.info("Taking scnreeshot of game window region")
            screenshot = pyautogui.screenshot(region=(gameWindow.startX,gameWindow.startY,gameWindow.width,gameWindow.height))
            screenshot.save(outputPath)
            return screenshot

class MatchTemplate: 
    def OnScreen(templatePath, threshold, masks = None):
        logging.info("Matching template " + templatePath + " with threshold " + str(threshold) + " on screen")
        debugPath = "Debug\MatchTemplate\OnScreen"
        result = None
        logging.info("Taking screenshot of entire screen")
        screenshot = pyautogui.screenshot()
        screenshotDebugPath = debugPath + "\screenshot.png"
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        if masks != None:
            logging.info("Masking screenshot")
            for mask in masks:
                screenshotMaskedDebugPath = debugPath + "\screenshotMasked.png"
                cv2.rectangle(screenshot, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
                logging.info("Saving masked screenshot to " + screenshotMaskedDebugPath)
                cv2.imwrite(screenshotMaskedDebugPath, screenshot)
            
        template = cv2.imread(templatePath, 0)  

        w, h = template.shape[::-1]

        logging.info("Matching template " + templatePath + " with threshold " + str(threshold))
        matchResult = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        location = np.where(matchResult >= threshold)
        for pt in zip(*location[::-1]):
            cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
            if pt != None:
                logging.info("Template found")
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)
                (startX, startY) = maxLoc
                endX = startX + template.shape[1]
                endY = startY + template.shape[0]
                result = MatchResult(startX,startY,endX,endY)
                logging.info("Saving debug screenshot to " + screenshotDebugPath)
                cv2.imwrite(screenshotDebugPath, screenshot)
                return result


    def InGameWindow(templatePath, threshold, masks = None):
        debugPath = "Debug\MatchTemplate\InGameWindow"
        result = None

        screenshotDebugPath = debugPath + "\screenshot.png"
        screenshot = Screenshot.GameWindow(screenshotDebugPath)
        if screenshot != None:
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            if masks != None:
                logging.info("Masking screenshot")
                for mask in masks:
                    screenshotMaskedDebugPath = debugPath + "\screenshotMasked.png"
                    cv2.rectangle(screenshot, (mask["startX"], mask["startY"]), (mask["endX"], mask["endY"]), (255, 255, 255), -1)
                    logging.info("Saving masked screenshot to " + screenshotMaskedDebugPath)
                    cv2.imwrite(screenshotMaskedDebugPath, screenshot)
                
            template = cv2.imread(templatePath, 0)  

            w, h = template.shape[::-1]

            logging.info("Matching template " + templatePath + " with threshold " + str(threshold))
            matchResult = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
            location = np.where(matchResult >= threshold)
            for pt in zip(*location[::-1]):
                cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
                if pt != None:
                    logging.info("Template found")
                    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(matchResult)
                    (startX, startY) = maxLoc
                    endX = startX + template.shape[1]
                    endY = startY + template.shape[0]
                    result = MatchResult(startX,startY,endX,endY)
                    logging.info("Saving debug screenshot to " + screenshotDebugPath)
                    cv2.imwrite(screenshotDebugPath, screenshot)
                    return result

class FindStuff:
    def WindowBar():
        logging.info("Finding window bar")
        WindowBarLocation = MatchTemplate.OnScreen("TemplateMatching\WindowBar.png",0.8)
        if WindowBarLocation != None:
            logging.info("Window bar found")
            global WindowBar
            WindowBar = WindowBarLocation
            return WindowBar
        else:
            logging.info("Window bar not found")
            return "NotFound"
        
    def GameWindow():
        logging.info("Finding game window")
        WindowBar = FindStuff.WindowBar()

        if WindowBar != None and WindowBar != "NotFound":
            logging.info("Window bar found")
            startX = WindowBar.startX
            endX = WindowBar.endX
            startY = WindowBar.startY + WindowBar.height
            endY = WindowBar.endY + 864 
            result = MatchResult(startX,startY,endX,endY)
            pyautogui.screenshot(region=(startX,startY,result.width,result.height)).save("Debug\GameWindow\screenshot.png")
            return result
        else:
            logging.info("Window bar not found")
        
    def ConvoBar():
        logging.info("Finding convo bar")
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
            logging.info("Convo bar found")
            return convoBar    
        else:
            logging.info("Convo bar not found")
            return "NotFound"
        
    def NurseJoyDialogBox():
        logging.info("Finding Nurse Joy dialog box")
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
            logging.info("Nurse Joy dialog box found")
            return convoBar    
        else:
            logging.info("Nurse Joy dialog box not found")
            return "NotFound"
        
    def PCDialogBox():
        logging.info("Finding PC dialog box")
        masks = [
            {
                "startX": 48,
                "startY": 80,
                "endX": 88,
                "endY": 432
            }
        ]
        convoBar = MatchTemplate.InGameWindow("TemplateMatching\\PCDialogBox.png", 0.8, masks)

        if convoBar != None:
            logging.info("PC dialog box found") 
            return convoBar    
        else:
            logging.info("PC dialog box not found")
            return "NotFound"