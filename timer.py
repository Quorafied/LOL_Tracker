import time
from threading import Timer

def UpdateCountdown(currentSlot1, currentSlot2, timeleftSlot1, timeleftSlot2, startSlot1, startSlot2, lane, window, tSlot1, tSlot2, nameSlot1, nameSlot2):
  # Get current time
  currentSlot1 = time.time()
  currentSlot2 = time.time()

  # Calculate time left of each Slot
  timeleftSlot1 = tSlot1 - (currentSlot1 - startSlot1)
  timeleftSlot2 = tSlot2 - (currentSlot2 - startSlot2)

  # Update Countdown timers
  if timeleftSlot1 > 0:
      window["-{}Slot1-".format(lane)].update("{}: ".format(str(nameSlot1)) + str(int(timeleftSlot1)))
  else:
      window["-{}Slot1-".format(lane)].update("")
  if timeleftSlot2 > 0:
      window["-{}Slot2-".format(lane)].update("{}: ".format(str(nameSlot2)) + str(int(timeleftSlot2)))
  else:
      window["-{}Slot1-".format(lane)].update("")

  return timeleftSlot1, timeleftSlot2