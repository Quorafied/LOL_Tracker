import PySimpleGUI as gui
from Roles import *
from timer import *
import time
import imageRecognition

# Defining the layout of the window
layout = [
    [
        [
            gui.Button("Top", size=(4, 1), key="-selectTop-"), 
            gui.Button("Jungle", size=(7, 1), key="-selectJng-"),
            gui.Button("Middle", size=(7, 1), key="-selectMid-"),
            gui.Button("Adc", size=(4, 1), key="-selectAdc-"),
            gui.Button("Support", size=(8, 1), key="-selectSupp-"),
        ],
        [gui.Text("")], # Used for Space
        [
            gui.Text("Flash", click_submits=True, key="-Flash-"),
            gui.Text("Heal", click_submits=True, key="-Heal-"),
            gui.Text("Exhaust", click_submits=True, key="-Exhaust-"),
            gui.Text("Ignite", click_submits=True, key="-Ignite-"),
            gui.Text("Barrier", click_submits=True, key="-Barrier-"),
            gui.Text("Teleport", click_submits=True, key="-Teleport-"),
            gui.Text("Cleanse", click_submits=True, key="-Cleanse-"),
        ],
        [gui.Text("")] # Used for Space
    ],
    [
        [
            [gui.Text("Top")],
            [gui.Text(text="", key="-topSlot1-"), gui.Text("", key="-topSlot2-")],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Jng")],
            [gui.Text("", key="-jngSlot1-"), gui.Text("", key="-jngSlot2-",)],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Mid")],
            [gui.Text("", key="-midSlot1-"), gui.Text("", key="-midSlot2-")],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Adc")],
            [gui.Text("", key="-adcSlot1-"), gui.Text("", key="-adcSlot2-")],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Support")],
            [gui.Text("", key="-suppSlot1-"), gui.Text("", key="-suppSlot2-")],
            [gui.Text(" ")] # Used for Space
        ],
    ]
]

# Creating a window
global window 
window = gui.Window("LOL_Tracker",
                    layout,
                    auto_size_text=True,
                    auto_size_buttons=True,
                    element_justification="center",
                    font=("Arial", "12"),
                    use_default_focus=False,
                    default_element_size=100,
                    size=(800, 800))

# Initializing Lane Classes
TopLaner = Lane("top")
Jungler = Lane("jng")
MidLaner = Lane("mid")
AdcLaner = Lane("adc")
Support = Lane("supp")

# Time in seconds of Spells
Flash_Time = int(300)
Heal_Time = 180
Exhaust_Time = 210
Ignite_Time = 180
Barrier_Time = 180
Teleport_Time = 315
Cleanse_Time = 210

# Define variables that act like temporary variables.
global selectedSpell_time
global selectedSpell
selectedSpell_time = 0
selectedSpell = ""

# Defining a function to start a Timer for an object pressumed to be a Lane object.
def startTimer(obj, selSpell_time, selSpell):
    if obj.Slot1 == "":
        obj.setSlot1Time(selSpell_time)
        obj.setSlot1_timeLeft(selSpell_time)
        obj.setSlot1(selSpell)
        obj.setSlot1_startTime(time.time()) # start
        obj.setTimer(True)  
    elif obj.Slot2 == "":
        obj.setSlot2Time(selSpell_time) # Spell time.
        obj.setSlot2_timeLeft(selSpell_time)
        obj.setSlot2(selSpell)
        obj.setSlot2_startTime(time.time()) # start
        obj.setTimer(True)
    else:
        selSpell_time = 0
        selSpell = ""
        print("no")
    return selSpell_time, selSpell

# Initializing the Image Recognition Bot.
SpellChecker = imageRecognition.imgRecognize()

# Events and Calls
while True:
    window.Refresh()
    event, values = window.Read(timeout=100)

    if event in (gui.WIN_CLOSED, "EXIT"):
        break

    # Timers and Countdowns
    if TopLaner.Timer:
        TopLaner.Slot1_timeLeft, TopLaner.Slot2_timeLeft = UpdateCountdown(TopLaner, window)
    if Jungler.Timer:
        Jungler.Slot1_timeLeft, Jungler.Slot2_timeLeft = UpdateCountdown(Jungler, window)
    if MidLaner.Timer:
        MidLaner.Slot1_timeLeft, MidLaner.Slot2_timeLeft = UpdateCountdown(MidLaner, window)                                                       
    if AdcLaner.Timer:
        AdcLaner.Slot1_timeLeft, AdcLaner.Slot2_timeLeft = UpdateCountdown(AdcLaner, window)                                                       
    if Support.Timer:
        Support.Slot1_timeLeft, Support.Slot2_timeLeft = UpdateCountdown(Support, window)                                            


    # Selection events
    if event == "-selectTop-":
        selected = "Top"
        selectedSpell_time, selectedSpell = startTimer(TopLaner, selectedSpell_time, selectedSpell)
    
    if event == "-selectJng-":
        selected = "Jng"
        selectedSpell_time, selectedSpell = startTimer(Jungler, selectedSpell_time, selectedSpell)
    
    if event == "-selectMid-":
        selected = "Mid"
        selectedSpell_time, selectedSpell = startTimer(MidLaner, selectedSpell_time, selectedSpell)

    if event == "-selectAdc-":
        selected = "Adc"
        selectedSpell_time, selectedSpell = startTimer(AdcLaner, selectedSpell_time, selectedSpell)
    
    if event == "-selectSupp-":
        selected = "Supp"
        selectedSpell_time, selectedSpell = startTimer(Support, selectedSpell_time, selectedSpell)
        
    if event == "-Flash-":
        selectedSpell_time = Flash_Time
        selectedSpell = "Flash"
        print(selectedSpell)
    
    if event == "-Heal-":
        selectedSpell_time = Heal_Time
        selectedSpell = "Heal"
        print(selectedSpell)

    if event == "-Exhaust-":
        selectedSpell_time = Exhaust_Time
        selectedSpell = "Exhaust"
        print(selectedSpell)
    
    if event == "-Ignite-":
        selectedSpell_time = Ignite_Time
        selectedSpell = "Ignite"
        print(selectedSpell)
    
    if event == "-Barrier-":
        selectedSpell_time = Barrier_Time
        selectedSpell = "Barrier"
        print(selectedSpell)

    if event == "-Teleport-":
        selectedSpell_time = Teleport_Time
        selectedSpell = "Teleport"
        print(selectedSpell)

    if event == "-Cleanse-":
        selectedSpell_time = Cleanse_Time
        selectedSpell = "Cleanse"
        print(selectedSpell)

