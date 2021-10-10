class Lane():
    def __init__(self, name):
        self.name = str(name)

        self.Slot1 = "Flash"
        self.Slot1Time = 0
        self.Slot1_timeLeft = 0
        self.Slot1_currentTime = 0
        self.Slot1_startTime = 0

        self.Slot1Region = ()
        self.Slot2Region = () 

        self.Slot2 = "Heal"
        self.Slot2Time = 0
        self.Slot2_timeLeft = 0
        self.Slot2_currentTime = 0
        self.Slot2_startTime = 0

        self.Timer = False

    def setName(self, n):
        self.name = str(n)
    def setSlot1(self, n):
        self.Slot1 = str(n)
    def setSlot1Time(self, n):
        self.Slot1Time = n
    def setSlot1_timeLeft(self, n):
        self.Slot1_timeLeft = n
    def setSlot1_currentTime(self, n):
        self.Slot1_currentTime = n
    def setSlot1_startTime(self, n):
        self.Slot1_startTime = n
    def setSlot2(self, n):
        self.Slot2 = str(n)
    def setSlot2Time(self, n):
        self.Slot2Time = n
    def setSlot2_timeLeft(self, n):
        self.Slot2_timeLeft = n
    def setSlot2_currentTime(self, n):
        self.Slot2_currentTime = n
    def setSlot2_startTime(self, n):
        self.Slot2_startTime = n
    def setTimer(self, n):
        self.Timer = n

