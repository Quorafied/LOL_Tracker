from cv2 import cv2
import numpy as np
import time
from pynput import mouse, keyboard
import pyautogui


class imgRecognize():
  def __init__(self):
    self.tries = 0

  def waitForScreen(self, obj):
    while True:
      if pyautogui.locateOnScreen("img/{}.png".format(str(obj)), confidence=0.9, grayscale=True): # Region
        time.sleep(0.5)

        coords = pyautogui.locateOnScreen("img/{}.png".format(str(obj)), confidence=0.9, grayscale=True)
        pyautogui.click(coords)
        break
      else:
        time.sleep(0.3)

        self.tries += 1
        print(str(self.tries))

        if self.tries > 50:
          break
    return self.tries


  def locateAll(self):
    time.sleep(2)
    img1 = pyautogui.screenshot("my_screenshotExBarr.png")
    while True:
      time.sleep(2)
      print('Ally:')  
      for pos in pyautogui.locateAllOnScreen("img/{}.png".format(str("Enemy_Flashes"))):
        print(pos)
      
      print("Enemy:")
      for pos in pyautogui.locateAllOnScreen("img/{}.png".format(str("Ally_Flashes"))):
        print(pos)
  
  def click(self):
    for i in range(5):
      time.sleep(2)
      pyautogui.click(1001, 320)

  def checkLaneSlots(self, objects): # Where objs is a list of objects.
    for obj in objects:
      # Check Slot1 of every object.
      if (pyautogui.locateOnScreen("img/{}.png".format(str("Ally_Flashes")), confidence=0.9, region=obj.Slot1Region)):
        obj.Slot1 = "Flash"
        print("Found Flash Slot1")
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Heal")), confidence=0.9, region=obj.Slot1Region)):
        obj.Slot1 = "Heal"
        print("Found Heal Slot1")
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Exhaust")), confidence=0.9, region=obj.Slot1Region)):
        obj.Slot1 = "Exhaust"
        print("Found Exhaust Slot1")
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Ignite")), confidence=0.9, region=obj.Slot1Region)):
        obj.Slot1 = "Ignite"
        print("Found Ignite Slot1")
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Barrier")), confidence=0.9, region=obj.Slot1Region)):
        obj.Slot1 = "Barrier"
        print("Found Barrier Slot1")
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_TP")), confidence=0.9, region=obj.Slot1Region)):
        obj.Slot1 = "Teleport"
        print("Found Teleport Slot1")
      else:
        print("Did not find spells.")

      # Check Slot 2 of every object.
      if (pyautogui.locateOnScreen("img/{}.png".format(str("Ally_Flashes")), confidence=0.9, region=obj.Slot2Region)):
        obj.Slot2 = "Flash"
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Heal")), confidence=0.9, region=obj.Slot2Region)):
        obj.Slot2 = "Heal"
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Exhaust")), confidence=0.9, region=obj.Slot2Region)):
        obj.Slot2 = "Exhaust"
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Ignite")), confidence=0.9, region=obj.Slot2Region)):
        obj.Slot2 = "Ignite"
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_Barrier")), confidence=0.9, region=obj.Slot2Region)):
        obj.Slot2 = "Barrier"
      elif (pyautogui.locateOnScreen("img/{}.png".format(str("Enemy_TP")), confidence=0.9, region=obj.Slot2Region)):
        obj.Slot2 = "Teleport"
      else:
        pass


    #if (pyautogui.locateOnScreen("img/{}.png".format(str("Ally_Flashes")), confidence=0.9, region=obj.Slot1Region) and
    #pyautogui.locateOnScreen("img/{}.png".format(str("Ally_Flashes")), confidence=0.9, region=obj.Slot2Region)):
    #  return True