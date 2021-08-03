class TimeSlot():

    def __init__(self, startTime, recipient):
        self.recipient = recipient
        self.startTime = startTime


    def formatTime(self):
        ##Turn self.startTime into a usable time string
        if self.startTime%1 == 0:
            ##Time is an integer
            return f'{int(self.startTime)} mins'
        else:
            return f'{int(self.startTime)} mins {int((self.startTime%1)*60)} secs'


class MakeSandwich(TimeSlot):

    def __init__(self, startTime, recipient):
        super().__init__(startTime, recipient)
        self.duration = 2.5
        self.endTime = self.startTime + self.duration

    def __str__(self):
        return f'Make sandwich for {self.recipient} at {self.formatTime()}'


class ServeSandwich(TimeSlot):

    def __init__(self, startTime, recipient):
        super().__init__(startTime, recipient)
        self.duration = 1
        self.endTime = self.startTime + self.duration
    
    def __str__(self):
        return f'Serve sandwich to {self.recipient} at {self.formatTime()}'


##Calculate start time
def calculateStartTime(times):
    if len(times) != 0:
        return times[-1].endTime
    else:
        return 0

def addOrder(name,times):
    makeSlot = MakeSandwich(calculateStartTime(TimeSlots), name)
    TimeSlots.append(makeSlot)
    serveSlot = ServeSandwich(calculateStartTime(TimeSlots), name)
    TimeSlots.append(serveSlot)
    outputSchedule(TimeSlots)

##Test output
def outputSchedule(times):
    print("\n")
    for i in range(len(TimeSlots)):
        print(f'{i+1}. {TimeSlots[i]}')
    print("Take a break\n")

##Container for all time slots
TimeSlots = []

##Test on 3 inputs
for _ in range(3):
    name = input("Input name:")
    addOrder(name, TimeSlots)
    

