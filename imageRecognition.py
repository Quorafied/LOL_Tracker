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
    img1 = pyautogui.screenshot("my_screenshot.png")
    while True:
      time.sleep(2)
      print('Ally:')  
      for pos in pyautogui.locateAllOnScreen("img/{}.png".format(str("Enemy_Flashes"))):
        print(pos)
      
      print("Enemy:")
      for pos in pyautogui.locateAllOnScreen("img/{}.png".format(str("Ally_Flashes"))):
        print(pos)


dude = imgRecognize()
dude.locateAll()