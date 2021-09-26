import time
from threading import Timer
from Roles import *

#def UpdateCountdown(currentSlot1, currentSlot2, timeleftSlot1, timeleftSlot2, startSlot1, startSlot2, lane, window, tSlot1, tSlot2, nSlot1, nSlot2, lanerObj):
def UpdateCountdown(lanerObj, window):
    # Get current time
    lanerObj.Slot1_currentTime = time.time()
    lanerObj.Slot2_currentTime = time.time()

    # Update Countdown Timers
    if lanerObj.Slot1_timeLeft > 0:
        lanerObj.Slot1_timeLeft = lanerObj.Slot1Time - (lanerObj.Slot1_currentTime - lanerObj.Slot1_startTime)
        window["-{}Slot1-".format(lanerObj.name)].update("{}: ".format(str(lanerObj.Slot1)
                                                            ) + str(int(lanerObj.Slot1_timeLeft)))
    else:
        window["-{}Slot1-".format(lanerObj.name)].update("")
        lanerObj.Slot1 = ""
        lanerObj.Slot1Time = 0
    
    if lanerObj.Slot2_timeLeft > 0:
        lanerObj.Slot2_timeLeft = lanerObj.Slot2Time - (lanerObj.Slot2_currentTime - lanerObj.Slot2_startTime)
        window["-{}Slot2-".format(lanerObj.name)].update("{}: ".format(str(lanerObj.Slot2)
                                                            ) + str(int(lanerObj.Slot2_timeLeft)))
    else:
        window["-{}Slot2-".format(lanerObj.name)].update("")
        lanerObj.Slot2 = ""

    return lanerObj.Slot1_timeLeft, lanerObj.Slot2_timeLeft
