class TimeSlot():
    """Parent class for all time slots
    """    

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
    """Time slot to make a sandwich, duration = 2.5
    """    

    def __init__(self, startTime, recipient):
        super().__init__(startTime, recipient)
        self.duration = 2.5
        self.endTime = self.startTime + self.duration

    def __str__(self):
        return f'Make sandwich for {self.recipient} at {self.formatTime()}'


class ServeSandwich(TimeSlot):
    """Time slot to serve a sandwich, duration = 1
    """    

    def __init__(self, startTime, recipient):
        super().__init__(startTime, recipient)
        self.duration = 1
        self.endTime = self.startTime + self.duration
    
    def __str__(self):
        return f'Serve sandwich to {self.recipient} at {self.formatTime()}'


##Calculate start time
def calculate_start_time(times):
    if len(times) != 0:
        return times[-1].endTime
    else:
        return 0

def add_order(name,times):
    makeSlot = MakeSandwich(calculate_start_time(times), name)
    times.append(makeSlot)
    serveSlot = ServeSandwich(calculate_start_time(times), name)
    times.append(serveSlot)

##Test output
def output_schedule(times):
    print(generate_string(times))

##Generate string output in one variable
def generate_string(times):
    string = ''
    for i in range(len(times)):
        string += f'{i+1}. {times[i]}\n'
    string += f'{len(times)+1}. Take a break\n'
    return string

    

