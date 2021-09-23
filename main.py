import PySimpleGUI as gui
from Roles import *
from timer import *
import time

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
            [gui.Text("Top", click_submits=True, key="-topCD-")],
            [gui.Text(text="", key="-topSlot1-"), gui.Text("", key="-topSlot2-")],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Jng", click_submits=True, key="-jngCD-")],
            [gui.Text("", key="-jngSlot1-"), gui.Text("", key="-jngSlot2-",)],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Mid", click_submits=True, key="-midCD-")],
            [gui.Text("", key="-midSlot1-"), gui.Text("", key="-midSlot2-")],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Adc", click_submits=True, key="-adcCD-")],
            [gui.Text("", key="-adcSlot1-"), gui.Text("", key="-adcSlot2-")],
            [gui.Text(" ")] # Used for Space
        ],
        [
            [gui.Text("Support", click_submits=True, key="-suppCD-")],
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

# Variables
topTimer = False
jngTimer = False
midTimer = False
adcTimer = False
suppTimer = False

# Time in seconds
Flash_Time = 5
Heal_Time = 180
Exhaust_Time = 210
Ignite_Time = 180
Barrier_Time = 180
Teleport_Time = 315
Cleanse_Time = 210


topSlot1_start_time = 0 # start
topSlot1_current_time = 0 # current
topSlot1_time_left = 0
topSlot2_start_time = 0 # start
topSlot2_current_time = 0 # current
topSlot2_time_left = 0

jngSlot1_start_time = 0 # start
jngSlot1_current_time = 0 # current
jngSlot1_time_left = 0
jngSlot2_start_time = 0 # start
jngSlot2_current_time = 0 # current
jngSlot2_time_left = 0

midSlot1_start_time = 0 # start
midSlot1_current_time = 0 # current
midSlot1_time_left = 0
midSlot2_start_time = 0 # start
midSlot2_current_time = 0 # current
midSlot2_time_left = 0

adcSlot1_start_time = 0 # start
adcSlot1_current_time = 0 # current
adcSlot1_time_left = 0
adcSlot2_start_time = 0 # start
adcSlot2_current_time = 0 # current
adcSlot2_time_left = 0

suppSlot1_start_time = 0 # start
suppSlot1_current_time = 0 # current
suppSlot1_time_left = 0
suppSlot2_start_time = 0 # start
suppSlot2_current_time = 0 # current
suppSlot2_time_left = 0

topSlot1 = 0
topSlot1_name = ""
topSlot2 = 0
topSlot2_name = ""
selectedSpell_time = 0
selectedSpell = ""

#selectedTop, selectedJng, selectedMid, selectedAdc, selectedSupp = False, False, False, False, False
#selections = [selectedTop, selectedJng, selectedMid, selectedAdc, selectedSupp]

# Events and Calls
while True:
    window.Refresh()
    event, values = window.Read(timeout=100)

    if event in (gui.WIN_CLOSED, "EXIT"):
            break

    if topTimer:
        topSlot1_time_left, topSlot2_time_left = UpdateCountdown(topSlot1_current_time, topSlot2_current_time, topSlot1_time_left, 
                                                                    topSlot2_time_left, topSlot1_start_time, topSlot2_start_time, "top", window, topSlot1, topSlot2, topSlot1_name, topSlot2_name)
    if jngTimer:
        topSlot1_time_left, topSlot2_time_left = UpdateCountdown(jngSlot1_current_time, jngSlot2_current_time, jngSlot1_time_left, 
                                                            jngSlot2_time_left, jngSlot1_start_time, jngSlot2_start_time, "jng", window, Flash_Time, Heal_Time)
    if midTimer:
        topSlot1_time_left, topSlot2_time_left = UpdateCountdown(midSlot1_current_time, midSlot2_current_time, midSlot1_time_left, 
                                                            midSlot2_time_left, midSlot1_start_time, midSlot2_start_time, "mid", window, Flash_Time, Heal_Time)                                                          
    if adcTimer:
        topSlot1_time_left, topSlot2_time_left = UpdateCountdown(adcSlot1_current_time, adcSlot2_current_time, adcSlot1_time_left, 
                                                            adcSlot2_time_left, adcSlot1_start_time, adcSlot2_start_time, "adc", window, Flash_Time, Heal_Time)                                                          
    if suppTimer:
        topSlot1_time_left, topSlot2_time_left = UpdateCountdown(suppSlot1_current_time, suppSlot2_current_time, suppSlot1_time_left, 
                                                            suppSlot2_time_left, suppSlot1_start_time, suppSlot2_start_time, "supp", window, Flash_Time, Heal_Time)                                             

    if event == "-selectTop-":
        selected = "Top"
        print(values["-topSlot1-"])

        if window["-topSlot1-"].get() == "":
            topSlot1 = selectedSpell_time
            topSlot1_name = selectedSpell
            topSlot1_start_time = time.time() # start
            topTimer = True            
        elif window["-topSlot2-"].get() == "":
            topSlot2 = selectedSpell_time
            topSlot2_name = selectedSpell
            topSlot2_start_time = time.time() # start
            topTimer = True
        else:
            selectedSpell_time = 0
            selectedSpell = ""
            print("no")
    
    if event == "-Flash-":
        selectedSpell_time = Flash_Time
        selectedSpell = "Flash"
        print(selectedSpell)
        
        #if window["-topSlot1-"] == "" and window["-topSlot2-"] != "Flash: ":
        #    topSlot1 = Flash_Time
        #elif window["-topSlot2-"] == "" and window["-topSlot1-"] != "Flash: ":
        #    topSlot2 = Flash_Time
        #else:
        #    selectedTop = False
        #    print("Either Flash is present or incorrect Spell.")
        #pass
    
        
    
    if event == "-topCD-":
        topSlot1_start_time = time.time() # start
        topSlot2_start_time = time.time() # start
        topTimer = True

    if event == "-jngCD-":
        jngSlot1_start_time = time.time() # start
        jngSlot2_start_time = time.time() # start
        jngTimer = True
    
    if event == "-midCD-":
        midSlot1_start_time = time.time() # start
        midSlot2_start_time = time.time() # start
        midTimer = True

    if event == "-adcCD-":
        adcSlot1_start_time = time.time() # start
        adcSlot2_start_time = time.time() # start
        adcTimer = True

    if event == "-suppCD-":
        suppSlot1_start_time = time.time() # start
        suppSlot2_start_time = time.time() # start
        suppTimer = True

    


# Spells = ["Flash", "Heal", "Exhaust",
#          "Ignite", "Barrier", "Teleport", "Cleanse"]

#TopLaner = Top()
#Jungler = Jungle()
#MiddleLaner = Middle()
#BotLaner = Adc()
#SupportLaner = Support()
